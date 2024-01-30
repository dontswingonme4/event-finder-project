# data_collector.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/collect_data", methods=["POST"])
def collect_data():
    city = request.form.get("city", "")

    # Replace this with your actual implementation to fetch event data
    # For now, just returning a success message
    success_message = f"Data collected successfully for {city}!"

    return success_message

if __name__ == "__main__":
    app.run(debug=True, port=5001)
