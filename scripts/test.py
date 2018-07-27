from datetime import datetime, timedelta

today=datetime.now()
current_day=today.day
current_month=today.month
current_year=today.year

d = datetime(current_year, current_month, 1)
print (d.weekday())


import calendar
from datetime import datetime,timedelta


class AttendanceSystem(object):

    def __init__(self):
        self._today=datetime.now()
        self._current_month=self._today.month
        self._current_year=self._today.year
        self._calender=calendar.Calendar()
        self._total_sundays=


