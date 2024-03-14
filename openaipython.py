from flask import Flask, request
from openai import OpenAI
import os 
# from twilio.twiml.messaging_response import MessagingResponse

# client = OpenAI()

# app = Flask(__name__)
# @app.route('/sms', methods=['GET', 'POST'])

# def sms():
#     inb_msg = request.form['Body'].lower()
#     completion = client.chat.completions.create(
#         model = "gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": inb_msg}
#         ]
#     )
#     resp = MessagingResponse()
#     resp.message(str(completion.choices[0].message.content))
#     return str(resp)

# if __name__ == "__main__":
#     app.run(debug=True)

from twilio.rest import Client 
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token =os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

openaiclient = OpenAI()
completion = openaiclient.chat.completions.create(
model = "gpt-3.5-turbo",
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Greet a friend without saying a question. Give them some positive news."}
]
)
twiml = f'<Response><Say>{completion.choices[0].message.content}</Say></Response>'

call = client.api.account.calls.create(
    to = os.environ['MY_PHONE_NUMBER'],
    from_ = '(855) 302-1845',
    twiml = twiml
)
print(call.sid)

