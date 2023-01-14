from random import randint
from faker import Faker

from database.connect import session
from database.models import Student

fake = Faker("uk_UA")


def create_user_student():
    for _ in range(31):
        student = Student(
            name=fake.name(),
            group_id=randint(1, 3)
        )
        session.add(student)

    session.commit()


if __name__ == "__main__":
    create_user_student()
