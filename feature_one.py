
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Service layer to separate the business logic.
def get_total_online_time_service(user_id):
    # Logic to retrieve user's total online time (in seconds) goes here
    # This is just a placeholder. In an actual application, you would retrieve this information from your data source.
    return 2344242223423  # placeholder value

@app.route('/api/stats/user/total', methods=['GET'])
def user_total_time():
    user_id = request.args.get('userId')

    # Input validation
    if user_id is None:
        return jsonify({"error": "userId is required"}), 400

    try:
        total_time = get_total_online_time_service(user_id)
    except Exception as e:
        # Proper error handling
        return jsonify({"error": "An error occurred while retrieving data"}), 500

    return jsonify({"totalTime": total_time})

if __name__ == '__main__':
    # Use environment variable for configuration
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')
