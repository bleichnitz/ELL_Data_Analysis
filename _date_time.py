from datetime import date


def today_date():
    d = date.today()
    today = d.timetuple()
    year = today[0]
    month = today[1]
    if month < 10:
        month = str(0) + str(month)
    day = today[2]
    if day < 10:
        day = str(0) + str(day)
    t_date = str(year)+"/" + str(month)+"/" + str(day)
    date_object = [t_date, str(year), str(month), str(day)]
    return date_object
