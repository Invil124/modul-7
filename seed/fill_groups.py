from database.connect import session
from database.models import Group

LIST_GROUPS = ["Group A", "Group B", "Group C"]


def create_groups(list_groups: list):
    for group in list_groups:
        group = Group(
            group_name=group
        )
        session.add(group)

    session.commit()


if __name__ == "__main__":
    create_groups(LIST_GROUPS)
