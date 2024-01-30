# data_collector.py
from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/collect_data", methods=["POST"])
def collect_data():
    city = request.form.get("city", "")

    # Replace this with your actual implementation to fetch event data from Ticketmaster API
    # For now, just returning a success message
    success_message = f"Data collected successfully for {city}!"

    return success_message

if __name__ == "__main__":
    # Use the environment variable for the port, or default to 5001
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, port=port)

