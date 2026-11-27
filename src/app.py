#Written by: Christina Rusu
#Date: 11/26/2026

from datetime import datetime
from flask import Flask, jsonify, render_template
from zoneinfo import ZoneInfo

app = Flask(__name__)

# Define the timezone 
TIMEZONE = ZoneInfo("America/Los_Angeles")

def format_timestamp(tmstp):
    return {
        "day": tmstp.strftime("%A"), 
        "date": tmstp.strftime("%Y-%m-%d"),
        "time": tmstp.strftime("%I:%M:%S %p") 
    }

@app.route("/")
def home():
    return render_template("timetest.html") 

@app.route("/timestamp", methods=["GET"])
def get_current_timestamp():
    # Generate the current time
    curr_time = datetime.now(TIMEZONE)
    return jsonify(format_timestamp(curr_time))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5045, debug=True)
