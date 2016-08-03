import datetime
import time


def java_date_to_direct_long_rounded_to_minutes(date_string):
    date = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
    return date.year * 100000000 + date.month * 1000000 + date.day * 10000 + date.hour * 100 + date.minute


def java_date_to_unix_long_rounded_to_minutes(date_string):
    date = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
    date_rounded_to_minutes = datetime.datetime(date.year, date.month, date.day, date.hour, date.minute)
    return time.mktime(date_rounded_to_minutes.timetuple())


def date_to_unix_long(year, month, day):
    d = datetime.datetime(year, month, day)
    return int(time.mktime(d.timetuple()))
