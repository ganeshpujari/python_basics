from calendar import Calendar, monthlen
from datetime import datetime, timedelta
DAILY_WORKING_HOURS = 9


class AttendanceManagement():
    """
        Description : AttendanceManagement class to check avg target
        attendance for remaining days.
        """
    def __init__(self):
        self.today = datetime.now()
        self.current_day = self.today.day
        self.current_month = self.today.month
        self.current_year = self.today.year

    def time_to_minutes(self, time):
        """
        This accepts time format in put and convert it into minutes in integer
         format
        :param time:
        :return: minutes in integer format
        """

        str_time = str(time)
        time_list = str_time.split(":")
        hours, minutes = int(time_list[0]), int(time_list[1])
        ret_minutes = (hours * 60) + minutes
        return ret_minutes

    def get_saturday_sunday_count(self, days):
        """
        This accepts days liost from current month and return total number of
         saturaday and sunday count.
        :param days:
        :return: saturady_sunday_count
        """

        saturady_sunday_count = 0
        for day in days:
            if day[5] != 0:
                saturady_sunday_count += 1
            if day[6] != 0:
                saturady_sunday_count += 1
        return saturady_sunday_count

    def get_total_working_days_remaining(self, curent_month, current_year,
                                         present_days,
                                         number_of_holiday_remaining=0):
        """
        This will return total workinga days in current month after
        removing holiday and saturday-sunday from month days.
        :param curent_month:
        :param current_year:
        :param present_days:
        :param number_of_holiday_remaining:
        :return: total_working_day_remaining
        """

        total_days_in_month = monthlen(current_year, curent_month)
        days = Calendar().monthdayscalendar(current_year, curent_month)
        saturady_sunday_count = self.get_saturday_sunday_count(days)
        saturady_sunday_count += number_of_holiday_remaining
        total_working_day_remaining = \
            (total_days_in_month - (saturady_sunday_count + present_days))
        return total_working_day_remaining

    def get_avarage_working_target(self, average_attendace,
                                   available_working_days, present_days):
        """
        This method do actual attendance calculation.

        :param average_attendace:
        :param available_working_days:
        :param present_days:
        :return:
        """
        if average_attendace == '09:00:00' or\
            average_attendace.startswith('09:00:') or\
                average_attendace.startswith('9:00:'):
            return 9, 00, available_working_days
        avrage_working_time_list = average_attendace.split(":")
        average_attendace_hours = int(avrage_working_time_list[0])
        average_attendace_minutes = int(avrage_working_time_list[1])
        if average_attendace_hours < DAILY_WORKING_HOURS:
            #calculating if avg working time less than avg target time.
            tt = timedelta(hours=DAILY_WORKING_HOURS) - \
                 (timedelta(hours=average_attendace_hours) +
                  timedelta(minutes=average_attendace_minutes))
            res = timedelta(hours=9) +\
                timedelta(minutes=self.time_to_minutes(present_days*tt)) /\
                (available_working_days)
            result_list = str(res).split(":")
            hours, minutes = result_list[0], result_list[1][:2]
            return hours, minutes, available_working_days
        else:
            # calculating if avg working time greter than avg target time.
            tt = (timedelta(hours=average_attendace_hours) +
                  timedelta(minutes=int(average_attendace_minutes))) - \
                 timedelta(hours=DAILY_WORKING_HOURS)
            mins = self.time_to_minutes(tt)
            td = timedelta(minutes=mins * present_days)
            days, hours, minutes = td.days, td.seconds // 3600, td.seconds //\
                60 % 60
            extra_work = timedelta(hours=days * 24) + timedelta(hours=hours) +\
                timedelta(minutes=minutes)
            retData = (timedelta(days=available_working_days) - extra_work) / \
                timedelta(hours=9)
            result_list = str(retData).split(".")
            hours, minutes = result_list[0], result_list[1][:2]
            return hours, minutes, available_working_days


def is_valid_time_format(average_attendace):
    """
    This will check is user entered time is valid or not
    :param average_attendace:
    :return:
    """
    timeformat = "%H:%M:%S"
    try:
        valid_time = datetime.strptime(average_attendace, timeformat)
    except ValueError:
        print("Please enter average present time in hh:mm:ss format")
        attendance()


def is_valid_integer(number, error_message):
    """
    This will check is user entered value is valid integer or not
    :param number:
    :param error_message:
    :return:
    """
    try:
        valid_number = input(number)
    except ValueError:
        print(error_message)
        attendance()


def attendance():
    attendance_management = AttendanceManagement()
    average_attendace = input("Entaer your average attendance in 'hh:mm:ss'"
                              " format. E.g. 8:00:00  ")
    is_valid_time_format(average_attendace)

    present_days = int(input("Enter your present days. E.g. 19  "))
    is_valid_integer(present_days, "Please neter valid INTEGER value for"
                                   " present days")

    leaves = int(input("Enter your leaves taken in current month. E.g. 2  "))
    is_valid_integer(present_days, "Please neter valid INTEGER value for"
                                   " leaves ")

    available_working_days = \
        attendance_management.get_total_working_days_remaining(
            attendance_management.current_month,
            attendance_management.current_year, present_days)
    available_working_days = available_working_days - leaves
    hours, minutes, available_working_days = \
        attendance_management.get_avarage_working_target(
            average_attendace, available_working_days, present_days)

    print("you have to seat {hours} hours and {minutes} minutes"
          " for next {days}"
          " days ".format(hours=hours, minutes=minutes,
                          days=available_working_days))


if __name__ == '__main__':
    attendance()
