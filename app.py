from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'azazel225229@gmail.com'
app.config['MAIL_PASSWORD'] = 'azazelia225229'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/send_message', methods=['POST'])
def send_newsletter():
    subject = request.get_json()['subject']
    message = request.get_json()['message']
    sender = request.get_json()['sender_mail']
    recipients = request.get_json()['recipients_mail']
    send_request = Message(f'{subject}', sender = f'{sender}', recipients = recipients)
    send_request.body = f"{message}"
    mail.send(send_request)
    return "Message envoyé aux abonnés de la newsletter"

if __name__ == '__main__':
    app.run(debug=True)
