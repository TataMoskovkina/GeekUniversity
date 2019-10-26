from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///vacancy.db',echo=True)
Base = declarative_base()

class Vacancy(Base):
    __tablename__='vacancys'
    id = Column(Integer, primary_key=True, unique=True,autoincrement=True)
    vacancy_name = Column(String(255))
    requirements = Column(String)
    salary_min = Column(Integer)
    salary_max = Column(Integer)
    currency = Column(String)
    town = Column(String)
    vacancy_url = Column(String)
    base_url = Column(String)

    def __init__(self, vacancy_name, requirements, salary_min, salary_max, currency, town, vacancy_url, base_url):
        self.vacancy_name = vacancy_name
        self.requirements = requirements
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.currency = currency
        self.town = town
        self.vacancy_url = vacancy_url
        self.base_url = base_url
