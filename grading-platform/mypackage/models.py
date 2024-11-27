from . import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Students(db.Model):
    __tablename__ = 'students'
    student_id: Mapped[Integer] = mapped_column(primary_key=True)
    student_name: Mapped[str] = mapped_column(String(255), nullable=False)

class Grades(db.Model):
    __tablename__ = 'grades'
    grade_id: Mapped[Integer] = mapped_column(primary_key=True)
    student_id: Mapped[Integer] = mapped_column(db.ForeignKey('students.student_id'), nullable=False)
    grade: Mapped[Integer] = mapped_column(nullable=False)