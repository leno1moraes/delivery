#!/bin/bash

apt-get update -y
apt-get upgrade -y

# Install prerequisites
apt-get install -y apt-transport-https ca-certificates curl software-properties-common

# Install Docker
curl -fsSL https://get.docker.com | sh
usermod -aG docker vagrant

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Install Node.js 14
#curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
# Install Node.js 16 using NodeSource
#curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
# Install Node.js 18 using NodeSource
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
apt-get install -y nodejs

# Install Npm
apt-get install -y npm

# Install pip
apt-get install python3-pip -y

# Install libcairo2-dev
apt-get install libcairo2-dev -y

# Criar pasta do projeto
mkdir -p /projeto

chmod -R 777 /projeto