from datetime import datetime, timedelta, date, time, timezone


custom_date = date(2025, 12, 30)
# datetime.date.today()


# print("Day", custom_date.day)
# print("Month", custom_date.month)
# print("Year", custom_date.year)


custom_time = time(20, 10, 50)
# print(custom_time.hour, custom_time.minute, custom_time.second)


custom_datetime = datetime.now(tz=timezone.utc)
# print(custom_datetime)


# custom_timedelta = timedelta(days=2, hours=5)
# print(custom_datetime + custom_timedelta)

# https://acode.com.ua/method-strftime-python/ - Всі коди до .strftime
# print(custom_datetime.strftime("%Y %B-%d %H:%M:%S (%A)"))

utc_now = datetime.now(timezone.utc)
# print("utc_now (aware):", utc_now)

kyiv_offset = timezone(timedelta(hours=2))
kyiv_time_fixed = utc_now.astimezone(kyiv_offset)
# print("kyiv_time_fixed (UTC+2):", kyiv_time_fixed)


# ЗАДАЧІ

def get_all_black_fridays(year):
    for i in range(1, 13):
        my_date = date(year, i, 13)
        if date.weekday(my_date) == 4:
            yield my_date.strftime("%B %d")




for _date in get_all_black_fridays(2026):
    print(_date)