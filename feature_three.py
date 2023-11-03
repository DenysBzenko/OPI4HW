from flask import Flask, request, jsonify
import os

app = Flask(__name__)


def delete_user_data_service(user_id):

    return True

@app.route('/api/user/forget', methods=['POST'])
def forget_user():
    user_id = request.args.get('userId')

   
    if user_id is None:
        return jsonify({"error": "userId is required"}), 400

    try:
        deletion_successful = delete_user_data_service(user_id)
    except Exception as e:
        
        return jsonify({"error": "An error occurred while processing the request"}), 500

    if deletion_successful:
        
        return jsonify({"userId": user_id})
    else:
       
        return jsonify({"error": "An error occurred while processing the request"}), 500

if __name__ == '__main__':
  
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')
