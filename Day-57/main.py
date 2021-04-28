from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)


@app.route('/guess/<name>')
def guess_me(name):
    parameters = {
        'name': {name}
    }

    gender_res = requests.get(url="https://api.genderize.io", params=parameters)
    gender_data = gender_res.json()['gender']
    age_res = requests.get(url="https://api.agify.io", params=parameters)
    age_data = age_res.json()['age']
    return render_template('guess.html', person_name=name, age=age_data, gender=gender_data)

    # print(f"Hey {name},")
    # print(f"I think you are {gender_data['gender']},\n And you are {age_data}")
@app.route('/blog')
def get_blog():
    blog_link = "https://api.npoint.io/5abcca6f4e39b4955965"
    blog_res = requests.get(url=blog_link)
    blog_data = blog_res.json()
    return render_template("blog.html", posts=blog_data)



if __name__ == "__main__":
    app.run(debug=True)
