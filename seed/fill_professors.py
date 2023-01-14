from faker import Faker

from database.connect import session
from database.models import Professor

fake = Faker("uk_UA")


def create_professors():
    for _ in range(5):
        professor = Professor(
            name=fake.name(),
        )
        session.add(professor)

    session.commit()


if __name__ == "__main__":
    create_professors()
