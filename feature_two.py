
from flask import Flask, jsonify, request
import os

app = Flask(__name__)


def get_weekly_online_time_service(user_id):

    return 119000

def get_daily_online_time_service(user_id):

    return 3200

@app.route('/api/stats/user/average', methods=['GET'])
def user_average_time():
    user_id = request.args.get('userId')


    if user_id is None:
        return jsonify({"error": "userId is required"}), 400

    try:
        total_weekly_time = get_weekly_online_time_service(user_id)
        total_daily_time = get_daily_online_time_service(user_id)
    except Exception as e:

        return jsonify({"error": "An error occurred while retrieving data"}), 500


    weekly_average = total_weekly_time // 7
    daily_average = total_daily_time // 1

    return jsonify({"weeklyAverage": weekly_average, "dailyAverage": daily_average})

if __name__ == '__main__':

    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')
