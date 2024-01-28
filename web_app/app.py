#!/usr/bin/env python3

from flask import Flask, request
import requests

app = Flask(__name__)
data_collector_url = "http://localhost:5001/collect_data" #POST request to the data collector app

@app.route("/")
def main():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Event Finder Web Application</title>
    </head>
    <body>
        <h1>Event Finder Web Application</h1>
        <form action="/echo_user_input" method="POST">
            <label for="city_input">Enter City:</label>
            <input id="city_input" name="city" required>
            <br>
            <label for="timeframe_dropdown">Select Timeframe:</label>
            <select id="timeframe_dropdown" name="selected_timeframe">
                <option value="next week">Next Week</option>
                <option value="next month">Next Month</option>
                <option value="next 6 months">Next 6 Months</option>
                <!-- Add more timeframes as needed -->
            </select>
            <br>
            <input type="submit" value="Submit!">
        </form>
    </body>
    </html>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    city = request.form.get("city", "")
    selected_timeframe = request.form.get("selected_timeframe", "")

    # Make a POST request to the data_collector app to fetch event data
    data_collector_payload = {"city": city}
    response = requests.post(data_collector_url, data=data_collector_payload)

    # Extract event data from the response
    event_data = response.text

    return f"Searching for events in {city} in the {selected_timeframe}!\n\nEvent Data: {event_data}"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
