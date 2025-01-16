from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    sno = Column(Integer, nullable=False)

    groups = relationship('Group', secondary='student_group', back_populates='students')

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    students = relationship('Student', secondary='student_group', back_populates='groups')

# 中间表，用于多对多关系
class StudentGroup(Base):
    __tablename__ = 'student_group'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id'), primary_key=True)

