from flask import Flask, render_template, request
import requests

link = "https://api.npoint.io/43644ec4f0013682fc0d"

res = requests.get(link)
posts = res.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact_me():
    if request.method == 'POST':
        username = request.form["username"]
        email = request.form['email']
        phone_number = request.form['phone']
        message = request.form['message']
        return render_template("contact.html", msg_sent=True)

    else:
        return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:index>')
def get_post(index):
    requested_blog = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_blog = blog_post
    return render_template("post.html", post=requested_blog)


if __name__ == "__main__":
    app.run(debug=True)
