#!/bin/bash

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required dependencies

pip install flask requests difflib

# Notify user
echo "Virtual environment setup complete. Run ./local_run.sh to start the application."
exit 0
