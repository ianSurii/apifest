#!/bin/bash

# Navigate to your project directory
cd .

poetry shell

# Install dependencies using Poetry
poetry install

# Run the app using uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 80
