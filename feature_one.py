from flask import Flask, jsonify, request
import os

app = Flask(__name__)

def get_total_online_time_service(user_id):

    return 2344242223423

@app.route('/api/stats/user/total', methods=['GET'])
def user_total_time():
    user_id = request.args.get('userId')


    if user_id is None:
        return jsonify({"error": "userId is required"}), 400

    try:
        total_time = get_total_online_time_service(user_id)
    except Exception as e:

        return jsonify({"error": "An error occurred while retrieving data"}), 500

    return jsonify({"totalTime": total_time})

if __name__ == '__main__':

    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')
