from flask import Flask,request
import replicate
import os
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])

def sms():
    resp = MessagingResponse()
    inb_msg = request.form['Body'].lower().strip()
    output = replicate.run(
        "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
        input = {"prompt": inb_msg}
    )
    res_prompt = "prompt was " + inb_msg
    msg = resp.message(res_prompt)
    img = output[0]
    msg.media(img)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)