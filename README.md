# 🤖 AI-Powered Chatbot on AWS (CloudMateBot)

A serverless chatbot powered by **Amazon Lex**, **AWS Lambda**, and **DynamoDB** that automates customer support tasks like:
- Resetting passwords 🔐
- Explaining subscription plans 💳
- Canceling user subscriptions ❌

---

## 📦 Architecture

- **Amazon Lex**: Natural Language Understanding (NLU)
- **AWS Lambda (Python)**: Intent logic & DynamoDB integration
- **Amazon DynamoDB**: Logs interactions
- **Amazon CloudWatch**: Monitors performance & errors

---

## 🧪 Local Testing

Run unit tests for all intents:

```bash
python test_lambda.py
