"""Application initialization module."""

#from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_babel import Babel

# init database
engine = create_engine('sqlite:///books.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
babel = Babel()

class Book(Base):
    """
    Base class for book items. 
    Describes fields structure.
    """

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    author = Column(String(150))
    pages = Column(Integer)

#from app import views

def check_db():
    """
    Function checks database availability
    """

    try:
        rows = session.query(func.count(Book.id)).scalar()
    except Exception:
        return False
    else:
        return True

def create_app(config_filename=None):
    """
    Function to creating instance of application.
    """
 
    from flask import Flask
    app = Flask(__name__)

    if config_filename is not None:
        app.config.from_pyfile(config_filename)

    from app.books.views import books
    app.register_blueprint(books)

    babel.init_app(app)
    
    return app
