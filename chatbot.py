from flask import Flask, render_template, request
import re
from rules import Rules

app = Flask(__name__)


@app.route('/chatbot', methods=['POST'])
def chatbot_logic(message):
    # Add your chatbot's logic here

    rules = Rules.get_rules()
    if message == '':
        response = "Please ask me something related to Mental Health!"
        return response
    else:
        for pattern, response in rules.items():
            if re.search(message.lower(), pattern.lower()):
                return response
        else:
            response = "Sorry, I am currently unaware about the answer to this question. I am still learning...."
            return response


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    message = request.form['message']
    response = chatbot_logic(message)
    return response


if __name__ == '__main__':
    app.run(debug=True)
