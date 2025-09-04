#!/bin/bash

# Activate virtual environment and run the Flask app
source venv/bin/activate
python app.py

# Notify user
echo "Application is running. Press Ctrl+C to stop."
exit 0
