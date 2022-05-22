
from datetime import datetime, timedelta
from DBM import DBM


class Task:

    def __init__(self, db_task):
        self.date = db_task.date
        self.title = db_task.title
        self.description = db_task.description
        self.tracked_seconds = self.seconds_to_time(db_task.tracked_seconds)

        self.dbm = DBM()

    def pause_task(self):
        self.tracked_seconds = self.calculate_result_time()
        self.dbm.update_tracked_time(   self.date,
                                        self.title,
                                        self.tracked_seconds)

    def unpause_task(self):
        self.start_datetime = datetime.now()

    def calculate_result_time(self):
        datetime_now = datetime.now()
        return self.tracked_seconds + (datetime_now - self.start_datetime)

    def __del__(self):
        #questionable
        self.tracked_seconds = self.calculate_result_time()
        self.dbm.update_tracked_time(   self.date,
                                        self.title,
                                        self.tracked_seconds)

    @staticmethod
    def time_to_seconds(t):
        d = datetime.strptime(t, '%H:%M:%S')
        h = d.hour
        m = d.minute
        s = d.second
        td = timedelta( hours=h,
                        minutes=m,
                        seconds=s)
        return td.total_seconds()

    @staticmethod
    def seconds_to_time(sec):
        return timedelta(seconds=sec)