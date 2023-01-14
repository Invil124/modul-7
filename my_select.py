from sqlalchemy import func, desc, and_

from database.connect import session
from database.models import Student, Professor, Group, Mark, Lesson


def select_1():
    result = session.query(Student.name, func.round(func.avg(Mark.grade), 2).label("avg_grade")) \
        .select_from(Mark).join(Student).group_by(Student.id).order_by(desc("avg_grade")).limit(5).all()
    return result


def select_2():
    result = session.query(Student.name, func.round(func.avg(Mark.grade), 2).label("avg_grade"), Lesson.name) \
        .select_from(Mark).join(Student, Lesson).filter(Lesson.id == 3).group_by(Student.id, Lesson.id) \
        .order_by(desc("avg_grade")).limit(1).all()
    return result


def select_3():
    result = session.query(func.round(func.avg(Mark.grade), 2).label("avg_grade"), Group.group_name, Lesson.name) \
        .select_from(Mark).join(Student, Lesson, Group).filter(Lesson.id == 1)\
        .group_by(Group.group_name, Lesson.name).order_by(desc("avg_grade")).all()
    return result


def select_4():
    result = session.query(func.round(func.avg(Mark.grade), 2).label("avg_grade")).\
        select_from(Mark).all()
    return result


def select_5():
    result = session.query(Lesson.name)\
        .select_from(Lesson).join(Professor).filter(Professor.name == "Єлисавета Баклан").all()
    # Також можна відфільтрувати за допомогогою Professor.id
    return result


def select_6():
    result = session.query(Student.name, Group.group_name)\
        .select_from(Student).join(Group).filter(Group.id == 2).all()
    return result


def select_7():
    result = session.query(Group.group_name, Student.name, Mark.grade, Lesson.name)\
        .select_from(Mark).join(Student, Group, Lesson).filter(and_(Group.id == 1, Lesson.id == 1))\
        .group_by(Student.name, Group.group_name, Mark.grade, Lesson.name).all()
    #або filter(Lesson.name == "LESSON_NAME", Group.name == "GROUP_NAME)
    return result


def select_8():
    result = session.query(Lesson.name, Professor.name, func.round(func.avg(Mark.grade), 2))\
        .select_from(Mark).join(Lesson, Professor)\
        .filter(Professor.id == 2).group_by(Lesson.name, Professor.name).all()
    return result


def select_9():
    result = session.query(Student.name, Lesson.name)\
        .select_from(Mark).join(Student, Lesson).filter(Student.id == 2).all()
    return result


def select_10():
    result = session.query(Student.name, Lesson.name, Professor.name)\
        .select_from(Mark).join(Lesson, Student, Professor).filter(and_(Student.id == 1, Professor.id == 3))\
        .group_by(Lesson.name, Student.name, Professor.name).all()
    #Також можна фільтрувати не по ід а по іменам.
    return result


def select_11():
    result = session.query(Student.name, func.round(func.avg(Mark.grade), 2), Professor.name)\
        .select_from(Mark).join(Student, Lesson, Professor).filter(and_(Professor.id == 3, Student.id == 3))\
        .group_by(Professor.name, Student.name).all()
    return result


def select_12():
    last_date_list_tuples = session.query(Mark.date_of).select_from(Mark).join(Student, Group)\
        .filter(and_(Mark.lesson_id == 6, Group.id == 3)).order_by(desc(Mark.date_of)).limit(1).all()
    last_date = last_date_list_tuples[0][0]

    result = session.query(Lesson.name, Group.group_name, Student.name, Mark.date_of, Mark.grade)\
        .select_from(Mark).join(Student, Lesson, Group)\
        .filter(and_(Lesson.id == 6, Group.id == 3, Mark.date_of == last_date))\
        .order_by(desc(Mark.date_of)).all()

    return result


if __name__ == '__main__':
    print(select_12())
