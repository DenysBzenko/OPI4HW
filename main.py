from flask import Flask, jsonify  
import os
import logging
from logging.handlers import RotatingFileHandler 
from feature_one import user_total_time
from feature_two import user_average_time
from feature_three import forget_user

app = Flask(__name__)


app.add_url_rule('/api/stats/user/total', view_func=user_total_time, methods=['GET'])
app.add_url_rule('/api/stats/user/average', view_func=user_average_time, methods=['GET'])
app.add_url_rule('/api/user/forget', view_func=forget_user, methods=['POST'])


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

if __name__ == '__main__':

    
    env = os.environ.get('APP_ENV', 'development')
    if env == 'production':
        app.run(debug=False)
    else:
        app.run(debug=True)
