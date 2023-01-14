
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    group_name = Column(String(255), nullable=False)

    students = relationship("Student", back_populates="group")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column("student_name", String(255), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"))

    group = relationship("Group", back_populates="students")
    marks = relationship("Mark", back_populates="students")


class Professor(Base):
    __tablename__ = "professors"
    id = Column(Integer, primary_key=True)
    name = Column("professor_name", String(255), nullable=False)

    lessons = relationship("Lesson", back_populates="professors")


class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True)
    name = Column("lesson_name", String(255), nullable=False)
    professor_id = Column(Integer, ForeignKey("professors.id"))

    professors = relationship("Professor", back_populates="lessons")
    marks = relationship("Mark", back_populates="lessons")


class Mark(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_of = Column(Date, nullable=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))

    students = relationship("Student", back_populates="marks")
    lessons = relationship("Lesson", back_populates="marks")