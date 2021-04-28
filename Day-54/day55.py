from flask import Flask
app = Flask(__name__)

@app.route('/')
def main_page():
    return '<h1 style="text-align: center"> Welcome to my personal page</h1>'



def make_bold(function):
    def bold_text():
        return '<b>' + function() + '</b>'

    return bold_text
def make_emphasis(function):
    def emphasis_text():
        return '<em>' + function() + '</em>'
    return emphasis_text
def make_underline(function):
    def underline_text():
        return '<u>' + function() + '<u>'
    return underline_text




@app.route('/rfm')
@make_bold
@make_emphasis
@make_underline
def intro():
    return "My name is Raphael Mulenda and Im a father of little son Marcel Mulenda"

if __name__=="__main__":
    app.run(debug=True)