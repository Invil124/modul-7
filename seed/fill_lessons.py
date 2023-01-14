from random import randint

from database.connect import session
from database.models import Lesson

LIST_LESSONS = ["Вища математика", "Психологія", "Фінанси", "Статистка", "Філософія", "Мікроекономіка", "Менеджмент"]


def create_lessons(list_lessons: list):
    for lesson in list_lessons:
        lesson_to_db = Lesson(
            name=lesson,
            professor_id=randint(1, 5)
        )
        session.add(lesson_to_db)
    session.commit()


if __name__ == "__main__":
    create_lessons(LIST_LESSONS)
