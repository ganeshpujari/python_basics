from calendar import Calendar,monthlen
from datetime import datetime,timedelta
DAILY_WORKING_HOURS=9
average_attendace='09:44:00'
present_days=19


today=datetime.now()
current_day=today.day
current_month=today.month
current_year=today.year

def time_to_minutes(time):
    str_time=str(time)
    time_list=str_time.split(":")
    hours, minutes=int(time_list[0]), int(time_list[1])
    ret_minutes=(hours * 60) + minutes
    print("LLLLLLLLLLLL",ret_minutes)
    return ret_minutes


def get_saturday_sunday_count(days):
    saturady_sunday_count = 0
    for day in days:
        if day[5] != 0:
            saturady_sunday_count += 1
        if day[6] != 0:
            saturady_sunday_count += 1
    return saturady_sunday_count

def get_total_working_days_remaining(curent_month, current_year, present_days, number_of_holiday_remaining=0):
    total_days_in_month=monthlen(current_year, curent_month)
    days = Calendar().monthdayscalendar(current_year, curent_month)
    saturady_sunday_count=get_saturday_sunday_count(days)
    saturady_sunday_count += number_of_holiday_remaining
    total_working_day_remaining= (total_days_in_month - (saturady_sunday_count + present_days))
    return total_working_day_remaining

def get_avarage_working_target(average_attendace, available_working_days,present_days):
    avrage_working_time_list=average_attendace.split(":")
    average_attendace_hours=int(avrage_working_time_list[0])
    average_attendace_minutes=avrage_working_time_list[1]
    if average_attendace_hours < DAILY_WORKING_HOURS:
        tt = timedelta(hours=DAILY_WORKING_HOURS) - (timedelta(hours=average_attendace_hours) + timedelta(minutes=int(average_attendace_minutes)))
        res = timedelta(hours=9) + timedelta(minutes=time_to_minutes(present_days*tt)) / (available_working_days)
        result_list=str(res).split(":")
        hours, minutes = result_list[0], result_list[1][:2]
        print("you have to seat {hours} hours and {minutes} minutes for next {days}"
              " days ".format(hours=hours, minutes=minutes, days=available_working_days))

    else:
        tt = (timedelta(hours=average_attendace_hours) + timedelta(minutes=int(average_attendace_minutes)))-timedelta(hours=DAILY_WORKING_HOURS)
        mins=time_to_minutes(tt)
        td=timedelta(minutes=mins * present_days)
        days, hours, minutes = td.days, td.seconds // 3600, td.seconds // 60 % 60
        extra_work=timedelta(hours=days*24)+timedelta(hours=hours)+timedelta(minutes=minutes)
        retData= (timedelta(days=available_working_days)-extra_work)/timedelta(hours=9)
        result_list = str(retData).split(".")
        hours, minutes = result_list[0], result_list[1][:2]

        print("you have to seat {hours} hours and {minutes} minutes for next {days}"
              " days ".format(hours=hours, minutes=minutes, days=available_working_days))


available_working_days=get_total_working_days_remaining(current_month,current_year, present_days)
print(available_working_days)
print("UUUUUUUUUUU")
get_avarage_working_target(average_attendace,available_working_days, present_days)
