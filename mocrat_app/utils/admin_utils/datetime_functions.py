import datetime

def get_next_day_strings():
    today = datetime.datetime.today()
    next_day = today + datetime.timedelta(days=1)
    next_day = next_day.strftime("%Y/%m/%d")

    return next_day
