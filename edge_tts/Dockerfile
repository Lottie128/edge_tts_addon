ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
ARG BUILD_ARCH

FROM ${BUILD_FROM}

# Set environment variables
ENV LANG C.UTF-8

# Install Python 3, pip, and build dependencies
RUN apk add --no-cache \
    python3 \
    py3-pip \
    build-base \
    gcc \
    musl-dev \
    libffi-dev \
    libc-dev \
    openssl-dev \
    zlib-dev

# Forcefully ensure pip works and is updated
RUN python3 -m ensurepip && \
    pip3 install --no-cache-dir --upgrade pip setuptools wheel

# Install required Python packages
RUN pip3 install --no-cache-dir edge-tts flask

# Copy add-on files
WORKDIR /usr/src/
COPY edge_tts_server.py /usr/src/
COPY run.sh /usr/src/

# Expose port used by the add-on
EXPOSE 5000

# Make the run script executable
RUN chmod +x /usr/src/run.sh
ENTRYPOINT ["/usr/src/run.sh"]
