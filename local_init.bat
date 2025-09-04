@echo off
:: Create and activate virtual environment
python -m venv venv
call venv\Scripts\activate

:: Install required dependencies
pip install flask 
pip install requests
pip install urllib
pip install bs4
pip install sentence-transformers

:: Notify user
echo Virtual environment setup complete. Run local_run.bat to start the application.
exit
