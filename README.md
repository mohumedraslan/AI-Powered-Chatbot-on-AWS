# 🤖 AI-Powered Chatbot on AWS (CloudMateBot)

A fully serverless, AI-powered chatbot that handles real user requests such as password resets, subscription cancellations, and plan information — all built on **AWS Lex, Lambda, DynamoDB, and Cognito**, with monitoring via CloudWatch.

---

## 🏗️ Architecture

![Architecture](architecture_diagram.png)

1. **Amazon Lex** – NLP-based chatbot with 3 intents (`ResetPassword`, `PlanInfo`, `CancelSubscription`)
2. **AWS Lambda** – Serverless backend that processes input, handles logic, logs responses
3. **Amazon DynamoDB** – Stores interaction history
4. **Amazon Cognito** – Authenticates guest users via the frontend
5. **Amazon CloudWatch** – Logs invocations, creates dashboards & alarms

---

## 💡 Features

- 🎯 Intent recognition & slot filling
- 🔐 Secure password reset guidance
- 💬 Plan description & upgrade guidance
- 📩 Subscription cancellation via email
- 📊 CloudWatch monitoring dashboard + alarms
- 🔗 Web interface with Cognito guest access

---

## 🧪 Test Intents

| Intent             | Example Input                  |
|--------------------|--------------------------------|
| `ResetPassword`    | "I forgot my password"         |
| `PlanInfo`         | "What plans do you offer?"     |
| `CancelSubscription` | "Cancel my subscription"     |

---

## 🚀 How to Run

### 🛠️ Prerequisites

- AWS Account
- IAM role for Lambda with `dynamodb:PutItem`
- Lex V2 bot deployed with intents and Lambda attached
- DynamoDB table `ChatbotInteractions`
- Cognito Identity Pool with guest access + Lex permission
- Static website hosted via S3 or local `index.html`

### 📂 Folder Structure

