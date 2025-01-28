ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
ARG BUILD_ARCH

# Use the Home Assistant base image
FROM ${BUILD_FROM}

# Set environment variables
ENV LANG C.UTF-8

# Install Python 3, pip, and required system dependencies
RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-wheel \
    py3-setuptools \
    py3-cryptography \
    build-base \
    libffi-dev \
    musl-dev \
    gcc \
    libc-dev

# Upgrade pip to the latest compatible version
RUN python3 -m ensurepip && \
    pip3 install --no-cache-dir --upgrade pip

# Install required Python packages
RUN pip3 install --no-cache-dir edge-tts flask

# Copy necessary files into the container
WORKDIR /usr/src/
COPY edge_tts_server.py /usr/src/
COPY run.sh /usr/src/

# Expose the port used by the add-on
EXPOSE 5000

# Make run.sh executable and set it as the entrypoint
RUN chmod +x /usr/src/run.sh
ENTRYPOINT ["/usr/src/run.sh"]
