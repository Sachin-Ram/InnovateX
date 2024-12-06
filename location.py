from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Skyscanner API URL and headers


@app.route('/flights', methods=['GET'])
def get_flights():
    # Set up query parameters using request.args.get() to fetch from URL
    query = request.args.get("city", default="new")  # Default to 'new' if 'city' is not passed
    querystring = {"query": query, "locale": "en-US"}

    # Make the request to the Skyscanner API
    response = requests.get(url, headers=headers, params=querystring)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()  # Get the JSON data from the response
        
        try:
            # Extract the first entry's skyId and entityId
            first_entry = data.get('data', [])[0]  # Get the first item from the 'data' list
            skyId = first_entry.get('skyId', 'N/A')  # Get the skyId
            entityId = first_entry.get('entityId', 'N/A')  # Get the entityId

            # Return the extracted data in JSON format
            return jsonify({
                'skyId': skyId,
                'entityId': entityId
            })
        except (IndexError, KeyError) as e:
            return jsonify({"error": "Error parsing response data", "message": str(e)}), 500
    else:
        return jsonify({"error": "Failed to fetch data from the API"}), 500

if __name__ == '__main__':
    app.run(debug=True)
