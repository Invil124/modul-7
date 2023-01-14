from random import randint
from faker import Faker

from database.connect import session
from database.models import Mark

NUMBER_LESSON = 7
NUMBER_STUDENTS = 31

fake = Faker()


def fill_mark():

    for i in range(1, NUMBER_STUDENTS+1):

        for grades in range(1, randint(18, 20)):
            marks = Mark(
                grade=randint(1, 12),
                date_of=fake.date_between(start_date="-1y"),
                student_id=i,
                lesson_id=randint(1, NUMBER_LESSON)
            )
            session.add(marks)

    session.commit()


if __name__ == "__main__":
    fill_mark()
