
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Service layer for business logic separation
def delete_user_data_service(user_id):
    # Logic to delete user data, ensuring GDPR-compliance
    # This should include deleting records from all databases, backups, logs, third-party services, etc.
    # Placeholder logic, actual application logic may involve multiple steps and verification
    return True  # return True if successful, False otherwise

@app.route('/api/user/forget', methods=['POST'])
def forget_user():
    user_id = request.args.get('userId')

    # Input validation
    if user_id is None:
        return jsonify({"error": "userId is required"}), 400

    try:
        deletion_successful = delete_user_data_service(user_id)
    except Exception as e:
        # Proper error handling, ensuring no sensitive user data is logged
        return jsonify({"error": "An error occurred while processing the request"}), 500

    if deletion_successful:
        # Respond with the user ID to confirm the deletion has been processed
        return jsonify({"userId": user_id})
    else:
        # Handle the deletion error properly
        return jsonify({"error": "An error occurred while processing the request"}), 500

if __name__ == '__main__':
    # Use environment variable for configuration
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')
