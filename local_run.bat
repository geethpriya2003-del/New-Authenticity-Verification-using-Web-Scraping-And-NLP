@echo off
:: Activate virtual environment and run the Flask app
call venv\Scripts\activate
python app.py

:: Notify user
echo Application is running. Press Ctrl+C to stop.
exit