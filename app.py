from flask import Flask, render_template
from flask import redirect,url_for,session,request
from flask_mysqldb import MySQL
from wtforms import Form,TextAreaField,validators,PasswordField
from passlib.hash import sha256_crypt

app = Flask(__name__,template_folder="templates")

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "kodland_gorev"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"


mysql = MySQL(app)
mysql.init_app(app)


# Doğru cevaplar
correct_answers = {
    'q1': 'Evet',
    'q2': 'Veri ile',
    'q3': 'Piksel',
    'q4': 'Konuşan bilgisayar programı',
    'q5': 'Veri ile',
    'q6': 'Doğal Dil İşleme',
    'q7': 'Bilgisayar Görüşü',
    'q8': 'NLP',
    'q9': 'Veri ve Algoritmalar ile',
    'q10': 'Görme ve Dinleme'
}

@app.route("/")
def index():

    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/competition")
def competition():

    return render_template("competition.html", )





@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for q, correct_answer in correct_answers.items():
        user_answer = request.form.get(q)
        if user_answer == correct_answer:
            score += 10
    app.config["Score"] = score  
    print(score)
    return render_template('competition.html', Score = app.config["Score"])
    



if __name__ == "__main__":
    app.run(debug=True)
