from flask import Flask, request, jsonify, send_file
import edge_tts
import os
import hashlib
import asyncio
import json

# Initialize Flask app
app = Flask(__name__)

# Load configuration options
CONFIG_FILE = "/data/options.json"
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE) as f:
        config = json.load(f)
else:
    config = {"default_voice": "en-US-AriaNeural", "cache_enabled": True, "cache_max_size": 50}

CACHE_DIR = "/app/cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def clean_cache(max_size):
    """Delete old files if the cache size exceeds the limit (in MB)."""
    files = [(f, os.path.getsize(os.path.join(CACHE_DIR, f))) for f in os.listdir(CACHE_DIR)]
    total_size = sum(f[1] for f in files) / (1024 * 1024)
    if total_size > max_size:
        files.sort(key=lambda x: os.path.getctime(os.path.join(CACHE_DIR, x)))
        while total_size > max_size:
            oldest = files.pop(0)
            os.remove(os.path.join(CACHE_DIR, oldest[0]))
            total_size -= oldest[1] / (1024 * 1024)

@app.route('/tts', methods=['POST'])
def tts():
    text = request.json.get("text", "")
    voice = request.json.get("voice", config.get("default_voice"))
    
    if not text:
        return jsonify({"error": "Text is required"}), 400

    # Hash the text and voice combination for caching
    file_hash = hashlib.sha256(f"{text}{voice}".encode()).hexdigest()
    output_file = os.path.join(CACHE_DIR, f"{file_hash}.mp3")

    # Return cached file if it exists
    if config.get("cache_enabled") and os.path.exists(output_file):
        return send_file(output_file, mimetype="audio/mpeg")

    # Generate TTS using Edge TTS
    async def generate_tts():
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)

    try:
        asyncio.run(generate_tts())
        if config.get("cache_enabled"):
            clean_cache(config.get("cache_max_size"))
        return send_file(output_file, mimetype="audio/mpeg")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8099)  # Ingress uses this port
