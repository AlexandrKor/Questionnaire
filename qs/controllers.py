from qs.extensions import db
from qs.models import Question

def add_question(text: str, author: str, topic: str):
    """Добавляет текст,автора и тему вопроса в БД и возвращает значение ID нового вопроса"""
    new_question = text
    new_author = author
    new_topic = topic
    question = Question(text=new_question, author=new_author, topic=new_topic)
    db.session.add(question)
    db.session.commit()
    return question.id

def del_question(question_id: int):
    """Удаление вопроса из БД"""
    question = Question.query.get(id=question_id)
    db.session.delete(question)
    db.session.commit()
    
def dislike_question(question_id:int):
    """Увеличивает количество дизлайков на единицу для определенного вопроса"""
    question = Question.query.filter_by(id=question_id).first()
    current_dislikes = question.dislikes
    question.dislikes = current_dislikes + 1
    db.session.add(question)
    db.session.commit()

def like_question(question_id:int):
    """Увеличивает количество лайков на единицу для определенного вопроса"""
    question = Question.query.filter_by(id=question_id).first()
    current_likes = question.likes
    question.likes = current_likes + 1
    db.session.add(question)
    db.session.commit()
    
