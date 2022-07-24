from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta

Base = declarative_base()


class ListToDo(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())


class DataBaseManager():
    def __init__(self):
        # connect to the database
        self.engine = create_engine("sqlite:///todo.db?check_same_thread=False")
        # to access the database in orm
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        # create the table in the database
        Base.metadata.create_all(self.engine)
        self.today = datetime.today()

    def today_tasks(self):
        print(f"Today {self.today.strftime('%d %b')}:")
        rows = self.session.query(ListToDo).filter(ListToDo.deadline == self.today.date()).all()
        if rows:
            for n, s in enumerate(rows, start=1):
                print(f"{n}. {s.task}")
        else:
            print("Nothing to do!")

    def all_task(self):
        print("\nAll tasks:")
        rows = self.session.query(ListToDo).order_by(ListToDo.deadline).all()
        if rows:
            for n, s in enumerate(rows, start=1):
                print(f"{n}. {s.task}. {s.deadline.strftime('%d %b')}")
        else:
            print("Nothing to do!")

    def week_tasks(self):
        week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for n in range(7):
            delta = timedelta(days=n)
            tomorrow = self.today + delta
            week_day = week_days[tomorrow.weekday()]
            print(f"{week_day} {tomorrow.strftime('%d %b')}:")
            rows = self.session.query(ListToDo).filter(ListToDo.deadline == tomorrow.date()).all()
            if rows:
                for n, s in enumerate(rows, start=1):
                    print(f"{n}. {s.task}")
            else:
                print("Nothing to do!")
            print()

    def missed_tasks(self):
        rows = self.session.query(ListToDo).filter(ListToDo.deadline < self.today.date()).order_by(
            ListToDo.deadline).all()
        print("Missed tasks:")
        if rows:
            for n, s in enumerate(rows, start=1):
                print(f"{n}. {s.task}.{self.today.strftime('%d %b')} ")
        else:
            print("Nothing is missed!")
        print()

    def add_task(self):
        task = input("\nEnter task\n")
        deadline = datetime.strptime(input("Enter deadline\n"), "%Y-%m-%d")
        new_row = ListToDo(task=task, deadline=deadline)
        self.session.add(new_row)
        self.session.commit()
        print("The task has been added!\n")

    def delete_tasks(self):
        print("Choose the number of the task you want to delete:")
        rows = self.session.query(ListToDo).order_by(ListToDo.deadline).all()
        if rows:
            for n, s in enumerate(rows, start=1):
                print(f"{n}. {s.task}. {s.deadline.strftime('%d %b')}")
            delete_task = int(input("\n"))
            self.session.query(ListToDo).filter(ListToDo.id == delete_task).delete()
            self.session.commit()
        else:
            print("Nothing to delete")

    def interface(self):
        while True:
            print(
                "1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit")
            user = input()
            if user == "1":
                self.today_tasks()
            elif user == "2":
                self.week_tasks()
            elif user == "3":
                self.all_task()
            elif user == "4":
                self.missed_tasks()
            elif user == "5":
                self.add_task()
            elif user == "6":
                self.delete_tasks()
            else:
                print("\nBye!")
                break
            print()


action = DataBaseManager()
action.interface()
