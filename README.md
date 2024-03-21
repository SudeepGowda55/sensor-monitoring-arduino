Follow this steps before starting the server

1. Change the serial port in the code (Line 41) i.e in the start_monitoring function according to your OS 

2. Makesure arduino is connected and your user account has permission to connect to the serial port.

3. Activate Virtual Environment (Optional)
    
    python3 -m venv venv 
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate      # Windows

4. Install Dependencies from requirements.txt
    
    pip install -r requirements.txt

5. start the server 

    uvicorn main:app --reload

    Go to http://127.0.0.1:8000/ 
