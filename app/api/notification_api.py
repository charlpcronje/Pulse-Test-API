# /app/api/notification_api.py-1-A+
from flask import Blueprint, request, jsonify
from ..services.firebase_service import FirebaseService
from ..models.user import User

notification_api_blueprint = Blueprint('notification_api', __name__)
firebase_service = FirebaseService()

@notification_api_blueprint.route('/send_notification', methods=['POST'])
def send_notification():
    """
    Endpoint for sending push notifications. Expects user_id and message details in the request data.
    """
    data = request.json
    if not data:
        return jsonify({'error': 'No request data provided'}), 400

    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID not provided'}), 400

    title = data.get('title')
    body = data.get('body')

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    for device in user.devices:
        firebase_service.send_notification(device.device_id, title, body)

    return jsonify({'message': 'Notification sent successfully'}), 200

