from flask import Flask
import random

rand_num = random.randint(0, 9)

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1 style="text-align: center"> ' \
           'Guess a number between 0 and 9</h1> <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"' \
           'margin-left:auto margin-right:auto>'

@app.route('/<int:guess>')
def guess_number(guess):
    if rand_num > guess:
        return '<h1 style="text-align: center" color:orange> ' \
               'Too high, Try Again! 🤓 </h1> ' \
               '<img src="https://media.giphy.com/media/8fgwop8fhah9K/giphy.gif" >'
    elif rand_num < guess:
        return '<h1 style="text-align: center" color:red> ' \
               'Too Low, Try Again! 🙄 </h1> ' \
               '<img src="https://media.giphy.com/media/sqajHVw58WRLW/giphy.gif" >'
    else:
        return '<h1 style="text-align: center" color:green> '\
               'You found me 🤑🤑 </h1> <img src="https://media.giphy.com/media/xUySTUZ8A2RJBQitEc/giphy.gif" >'


if __name__ == "__main__":
    app.run(debug=True)
