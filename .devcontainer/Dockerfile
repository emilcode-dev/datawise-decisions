# Use Ubuntu 24.04 LTS as the base image
FROM ubuntu:20.04
LABEL maintainer="emilcode-dev"

# Set DEBIAN_FRONTEND to noninteractive to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install dev tools
RUN apt-get update && apt-get install -y --no-install-recommends\
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*