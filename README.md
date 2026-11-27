# Timestamp-Generator
Timestamp Generator for PNW Monoliths CS361

# Using Timestamp Microservice
This program uses a Python/Flask Framework 

## Testing Image Microservice

1. Open a terminal and navigate to the project directory:\
`cd Time-Stamp Generator`

2. Create a python virtual environment\
`python3 -m venv .venv`

3. Active the virtual environment\
`source .venv/bin/activate`

4. Install dependencies:\
`python3 -m pip install -r requirements.txt`

5. Start the app: \
Navigate into the src directory and start flask application:
```sh
cd src
python3 app.py
```
The Flask server should now be running at:
http://localhost:5045

### The tester program supports the following operations:

- Generate timestamp: click the get current time button to generate a timestamp with day, date, and time 
