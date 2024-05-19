#!/bin/bash

# Get the current user
current_user=$(whoami)

# Install Poetry
echo "Installing Poetry..."
curl -sSL https://install.python-poetry.org | python3 -
if [ $? -ne 0 ]; then
    echo "Failed to install Poetry."
    exit 1
fi

# Install Docker
echo "Installing Docker..."
sudo apt install docker.io -y
if [ $? -ne 0 ]; then
    echo "Failed to install Docker."
    exit 1
fi

# Add current user to Docker group
echo "Adding $current_user to Docker group..."
sudo usermod -aG docker $current_user
if [ $? -ne 0 ]; then
    echo "Failed to add $current_user to Docker group."
    exit 1
fi

# Install Python dependencies with Poetry
echo "Installing Python dependencies with Poetry..."
poetry install
if [ $? -ne 0 ]; then
    echo "Failed to install Python dependencies with Poetry."
    exit 1
fi

# Start Docker containers with docker-compose
echo "Starting Docker containers..."
docker-compose --file docker-compose-local.yml up --force-recreate -d
if [ $? -ne 0 ]; then
    echo "Failed to start Docker containers."
    exit 1
fi

# Execute create_database.sh script
echo "Executing create_database.sh script..."
./create_database.sh
if [ $? -ne 0 ]; then
    echo "Failed to execute create_database.sh script."
    exit 1
fi

# Unknown command - almebic head upgrade
# Ensure this is a valid command and it's supposed to be here
almebic head upgrade
