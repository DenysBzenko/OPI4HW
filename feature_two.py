
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Service layer for business logic separation
def get_weekly_online_time_service(user_id):
    # Logic to retrieve user's total online time for the last 7 days
    # Placeholder logic, actual application logic may involve database operations
    return 119000  # e.g., total seconds of online time for the last 7 days

def get_daily_online_time_service(user_id):
    # Logic to retrieve user's total online time for the last 24 hours
    # Placeholder logic, actual application logic may involve database operations
    return 3200  # e.g., total seconds of online time for the last 24 hours

@app.route('/api/stats/user/average', methods=['GET'])
def user_average_time():
    user_id = request.args.get('userId')

    # Input validation
    if user_id is None:
        return jsonify({"error": "userId is required"}), 400

    try:
        total_weekly_time = get_weekly_online_time_service(user_id)
        total_daily_time = get_daily_online_time_service(user_id)
    except Exception as e:
        # Proper error handling
        return jsonify({"error": "An error occurred while retrieving data"}), 500

    # Calculate averages, adjusting depending on exact requirements
    weekly_average = total_weekly_time // 7
    daily_average = total_daily_time // 1  # assuming "daily" means "last 24 hours"

    return jsonify({"weeklyAverage": weekly_average, "dailyAverage": daily_average})

if __name__ == '__main__':
    # Use environment variable for configuration
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')
