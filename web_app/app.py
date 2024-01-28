#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <form action="/echo_user_input" method="POST">
         <label for="city_input">Enter City:</label>
         <input id="timeframe_input" name="city" required>
         <br>
         <label for="timeframe_dropdown">Select Timeframe:</label>
         <select id="timeframe_dropdown" name="selected_timeframe">
             <option value="next week">Next Week</option>
             <option value="next month">Next Month</option>
             <option value="next 6 months">Next 6 Months</option>
             <!-- Add more cities as needed -->
         </select>
         <br>
         <input type="submit" value="Submit!">
     </form>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    city = request.form.get("city", "")
    selected_timeframe = request.form.get("selected_timeframe", "")
    return f"Searching for events in {city} in the {selected_timeframe}!"


