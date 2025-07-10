import unittest
from lambda_function import lambda_handler

class TestLambdaHandler(unittest.TestCase):
    def test_reset_password(self):
        mock_event = {
            "sessionState": {
                "intent": {
                    "name": "ResetPassword",
                    "slots": {
                        "email": {
                            "value": {
                                "interpretedValue": "test@example.com"
                            }
                        }
                    }
                }
            },
            "inputTranscript": "I forgot my password"
        }

        response = lambda_handler(mock_event, None)
        self.assertIn("To reset your password", response['messages'][0]['content'])

    def test_plan_info(self):
        mock_event = {
            "sessionState": {
                "intent": {
                    "name": "PlanInfo",
                    "slots": {}
                }
            },
            "inputTranscript": "Tell me about the plans"
        }

        response = lambda_handler(mock_event, None)
        self.assertIn("CloudMate offers", response['messages'][0]['content'])

    def test_unknown_intent(self):
        mock_event = {
            "sessionState": {
                "intent": {
                    "name": "UnknownIntent",
                    "slots": {}
                }
            },
            "inputTranscript": "random"
        }

        response = lambda_handler(mock_event, None)
        self.assertIn("didn’t understand", response['messages'][0]['content'])

if __name__ == '__main__':
    unittest.main()
