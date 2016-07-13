"""Application launching module."""

from app import create_app, check_db
from flask_script import Manager, Command

app = create_app('..\config.py')
manager = Manager(app)

class runserver(Command):
    """
    Provides application launching.
    """

    def run(self):
        if not check_db():
            print('Please create database first with \"init\" argument!')
        else:
            app.run()

class init(Command):
    """
    Creates database structure.
    """

    def run(self):
        from app import Base, engine
        Base.metadata.create_all(engine)
        print("Database created.")

if __name__ == "__main__":
    manager.add_command("init", init())
    manager.add_command("runserver", runserver())
    manager.run()