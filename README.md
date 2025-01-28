# **Edge TTS Add-On for Home Assistant**

The **Edge TTS Add-On** enables seamless integration of Microsoft's Edge Text-to-Speech (TTS) service into your Home Assistant setup. Generate high-quality neural speech directly from your Home Assistant environment and enjoy fast, cached responses for frequently used text.

---

## **Features**
- **Microsoft Edge Neural Voices**: Leverage the power of high-quality neural TTS voices.
- **Caching**: Store previously generated audio files to improve performance and reduce processing time.
- **Configurable**: Set a default voice and customize cache behavior.
- **Ingress Support**: Access the add-on directly from the Home Assistant UI.

---

## **Installation**
1. **Add the Repository**:
   - In Home Assistant, go to **Settings > Add-ons > Add-on Store**.
   - Click the three dots in the top-right corner and select **Repositories**.
   - Add this repository URL:  
     `https://github.com/<your-username>/ha-edge-tts-addon`.

2. **Install the Add-On**:
   - Locate the **Edge TTS Add-On** in the store.
   - Click **Install**.

3. **Start the Add-On**:
   - Go to **Settings > Add-ons** and start the Edge TTS Add-On.
   - Configure the add-on as needed via the settings.

4. **Test the Integration**:
   - Use the provided API to ensure everything is working properly.

---

## **Configuration Options**
The add-on includes the following configuration options:

| **Option**        | **Type** | **Default**           | **Description**                                   |
|--------------------|----------|-----------------------|---------------------------------------------------|
| `default_voice`    | string   | `en-US-AriaNeural`    | The default voice for TTS if none is specified.   |
| `cache_enabled`    | boolean  | `true`                | Enables or disables caching of generated audio.   |
| `cache_max_size`   | integer  | `50`                 | Maximum size of the cache directory in MB.        |

---

## **Example Usage**
Once the add-on is running, you can interact with it via the `/tts` endpoint.

### **Example API Request**
Make a POST request to the TTS API using your Home Assistant server's IP address:
```bash
POST http://<HA_IP>:5000/tts
Content-Type: application/json

{
  "text": "Hello, Home Assistant!",
  "voice": "en-US-AriaNeural"
}
