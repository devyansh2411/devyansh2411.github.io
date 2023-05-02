from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/talkassist')
def talkassist():
    # Add your talk assist code here
    return redirect(url_for('home'))

@app.route('/camera')
def camera():
    # Add your camera code here
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
