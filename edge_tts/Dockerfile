ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
ARG BUILD_ARCH

# Set up base image
FROM ${BUILD_FROM}

# Set environment variables
ENV LANG C.UTF-8

# Copy necessary files
WORKDIR /usr/src/
COPY edge_tts_server.py /usr/src/
COPY run.sh /usr/src/

# Install required Python packages
RUN apk add --no-cache python3 py3-pip && \
    pip3 install --no-cache-dir edge-tts flask

# Expose the port used by the add-on
EXPOSE 5000

# Make run.sh executable and set it as the entrypoint
RUN chmod +x /usr/src/run.sh
ENTRYPOINT ["/usr/src/run.sh"]
