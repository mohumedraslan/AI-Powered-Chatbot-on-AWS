import json
import boto3
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ChatbotInteractions')

def lambda_handler(event, context):
    intent = event['sessionState']['intent']['name']
    slots = event['sessionState']['intent'].get('slots', {})
    user_input = event['inputTranscript']
    timestamp = datetime.utcnow().isoformat()

    # Log to CloudWatch
    logger.info(f"Intent: {intent}, Input: {user_input}")

    # Process intents
    if intent == "ResetPassword":
        email = slots.get('email', {}).get('value', {}).get('interpretedValue', 'N/A')
        response_text = f"To reset your password, click 'Forgot Password' on the login page and follow the instructions sent to {email}."
    elif intent == "PlanInfo":
        response_text = "CloudMate offers Free, Pro ($10/month), and Enterprise ($50/month) plans. Visit our website for details."
    elif intent == "CancelSubscription":
        email = slots.get('email', {}).get('value', {}).get('interpretedValue', 'N/A')
        response_text = f"To cancel your subscription, go to your billing dashboard or email support with {email}."
    else:
        response_text = "Sorry, I didn’t understand that. Can you rephrase?"

    # Save interaction to DynamoDB
    try:
        table.put_item(Item={
            'id': context.aws_request_id,
            'intent': intent,
            'user_input': user_input,
            'bot_response': response_text,
            'timestamp': timestamp
        })
    except Exception as e:
        logger.error(f"Error saving to DynamoDB: {str(e)}")

    # Return response to Lex
    return {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {"name": intent, "state": "Fulfilled"}
        },
        "messages": [{
            "contentType": "PlainText",
            "content": response_text
        }]
    }