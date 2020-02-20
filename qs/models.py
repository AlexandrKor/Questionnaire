from datetime import datetime

from qs.extensions import db


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    "Уникальный идентификатор"
    text = db.Column(db.Text, nullable=False)
    "Текст вопроса"
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    "Дата, когда был задан вопрос"
    author = db.Column(db.String(25), nullable=False)
    "Часть e-mail адреса до знака @ того, кто отправил вопрос"
    likes = db.Column(db.Integer, nullable=False, default=0)
    "Количество лайков не может быть равным null, но может быть равным нулю"
    dislikes = db.Column(db.Integer, nullable=False, default=0)
    "Количество дизлайков не может быть равным null, но может быть равным нулю"
    topic = db.Column(db.String, nullable=True)
    "Название темы. Может быть пустым, и если оно пустое, то вопрос относится к общей теме"
        
