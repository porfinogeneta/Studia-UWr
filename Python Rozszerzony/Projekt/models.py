from sqlalchemy import (create_engine, Column,
                        Integer, String, Float, DateTime,
                        Enum, ForeignKey, update, delete)
from sqlalchemy.orm import (declarative_base, sessionmaker,
                            validates, relationship,
                            mapped_column, Mapped)
from datetime import datetime
import enum
from typing import List


class LendingStates(enum.Enum):
    LENT = "lent"
    ON_SHELF = "on_shelf"
    LOST = "lost"


# wyznaczamy styl kodu
Base = declarative_base()


# jedna książka może mieć wiele wypożyczeń, relacja jeden do wielu
class Lending(Base):
    # SCHEMA
    __tablename__ = 'lendings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    friend_id = mapped_column(Integer,
                              ForeignKey('Friends.id'),
                              nullable=False)
    friend = relationship("Friend", back_populates="lending")

    lend_date = mapped_column(DateTime, nullable=False)
    return_date = mapped_column(DateTime, nullable=True)

    book_id = mapped_column(Integer, ForeignKey('books.id'), nullable=False)
    book = relationship("Book", back_populates="lendings")

    # VALIDATIONS
    @validates('return_date')
    def validate_return_date(self, key, return_date):
        if return_date and return_date > datetime.now():
            raise ValueError("Lending should be before Returning!")
        return return_date


class Book(Base):
    # SCHEMA
    __tablename__ = 'books'
    id = mapped_column(Integer,
                       primary_key=True,
                       autoincrement=True,
                       nullable=False)
    author = mapped_column(String(20), nullable=False)
    title = mapped_column(String(30), nullable=False)
    year = mapped_column(Integer, nullable=False)
    genre = mapped_column(String(20), nullable=False)

    # chcemy żeby były przetrzymywane nazwy zdefiniowane stringiem
    lend_state = Column(Enum(LendingStates,
                             values_callable=lambda x:
                             [str(member.value) for member in LendingStates]),
                        default='on_shelf')

    lendings: Mapped[List[Lending]] = relationship(
            "Lending",
            back_populates="book")

    # VALIDATIONS
    @validates('year')
    def validate_year(self, key, year):
        if year > datetime.now().year:
            raise ValueError("Book cannot be published in the future!")
        return year

    def __str__(self):
        return


class Friend(Base):
    # SCHEMA
    __tablename__ = 'Friends'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(20), nullable=False)
    surname = mapped_column(String(30), nullable=False)
    email = mapped_column(String(30), nullable=False)

    # wypożyczenia
    # pierwszy argument to kto stoi po drugiej stronie relacji,
    # drugi to gdzie relacja jest 'zaczepiona'
    lending: Mapped[List[Lending]] = relationship(
            "Lending",
            back_populates="friend"
        )

    # VALIDATIONS
    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("Email should contain '@'!")
        return email
