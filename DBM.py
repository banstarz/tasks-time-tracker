
from requests import Session
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from Models import Base, TrackedTime

class DBM:

    def __init__(self):
        self.engine = create_engine(f"sqlite:///tracked_time.db")
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()
        self.create_tables()
        self.query_tt = self.session.query(TrackedTime)

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def get_all_tasks_for_date(self, date):
        return self.query_tt.filter_by(date=date).all()

    def if_exists(self, date, title):
        similar_task = TrackedTime.query.filter_by( date=date,
                                                    title=title)
        if similar_task:
            return True

        return False

    def create_new_task(self, date, title, description, tracked_seconds):
        task = TrackedTime( date=date,
                            title=title,
                            description=description,
                            tracked_seconds=tracked_seconds)
        self.session.add(task)
        self.session.commit()

    def update_tracked_time(self, date, title, tracked_time):
        current_task = TrackedTime.query.filter_by( date=date,
                                                    title=title)
        current_task.tracked_seconds = tracked_time
        self.session.commit()

    def delete_task(self, date, title):
        current_task = TrackedTime.query.filter_by( date=date,
                                                    title=title)
        current_task.delete()
        self.session.commit()

    def print_first_task(self):
        print(self.session.query(TrackedTime).first())

    def delete_all(self):
        self.query_tt.delete()
        self.session.commit()


if __name__=='__main__':
    from datetime import datetime
    dbm = DBM()
    dbm.create_new_task(date=datetime.now(), 
                        title='1st task', 
                        description='my first task', 
                        tracked_seconds=0)
    dbm.create_new_task(date=datetime.now(), 
                        title='2nd task', 
                        description='my second task', 
                        tracked_seconds=0)