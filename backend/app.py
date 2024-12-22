from flask import Flask, request, jsonify
from stock_utils import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

@app.route("/get-asset-price", methods=["POST"])
def get_asset_price():
    try:
        # Parse JSON from the request
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Example of processing the data
        tickers = data.get("tickers")
        result = get_current_price_for_a_list_of_assets(tickers)

        if not tickers:
            return jsonify({"error": "Missing 'name' or 'age' in the payload"}), 400

        # Respond with a success message
        return jsonify({
            "message": "Data received successfully",
            "data": {
                "currentPrices": result
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="localhost", port=2000, debug=True)
