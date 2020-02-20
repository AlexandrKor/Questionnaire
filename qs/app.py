from flask import Flask 
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

from qs.extensions import db
from qs.controllers import add_question
from qs.controllers import like_question
from qs.controllers import dislike_question

from qs.models import Question


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:////{app.root_path}/questions.db'
  
    db.init_app(app)
    return app

app = create_app()

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

@app.route("/")
def index():
    db.create_all()
    return render_template("index.html")
    
@app.route("/ping")
def ping():
    return "pong"

@app.route("/question")
def question():
    return render_template("question.html")

@app.route("/rating")
def rating():
    question_list = Question.query.all()
    return render_template("rating.html", question_list=question_list)
     
@app.route("/actions/question/add", methods=['POST'])
def question_add():
    """Добавление вопроса"""
    text = request.form.get("text")
    author = request.form.get("author")
    topic = request.form.get("topic")
    if not (text and author and topic):
        return'Поля с текстом и email не могут быть пустыми'
    else:
        add_question(text, author, topic)
    return redirect(url_for("rating"))

@app.route("/actions/question/<question_id>/like")
def question_like(question_id:int):
    """Добавление лайка"""
    like_question(question_id)
    return redirect(url_for("rating"))

@app.route("/actions/question/<question_id>/dislike")
def question_dislike(question_id:int):
    """Добавление дизлайка"""
    dislike_question(question_id)
    return redirect(url_for("rating"))

@app.route("/actions/question/<question_id>/delete")
def question_delete(question_id:int):
    del_question(question_id)
    return redirect(url_for('rating'))
