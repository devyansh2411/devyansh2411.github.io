import random
from flask import Flask, render_template, request

app = Flask(__name__)

responses = {
    "hi": ["Hello!", "Hi there!", "Hi!"],
    "how are you": ["I'm doing well, thank you!", "I'm fine, thanks!"],
    "bye": ["Goodbye!", "Bye!", "See you later!"]
}

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    bot_response = ''
    if request.method == 'POST':
        user_input = request.form['user_input']
        for key in responses:
            if user_input.lower() == key:
                bot_response = random.choice(responses[key])
                break
        if bot_response == '':
            bot_response = "I'm sorry, I didn't understand what you said."
    return render_template('chatbot.html', bot_response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)
