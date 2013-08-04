from common import format_2digit_number


def format_hour(t):
    """ 1 -> 01:00"""
    if t < 10:
        t = "0" + str(t)
    return str(t) + ":00"


def month_lengths(year):
    """
    returns an array with all the month lengths and 0 prepending it
    """
    #pprint(month_lengths(1998))
    #pprint(month_lengths(1999))
    #pprint(month_lengths(2000))
    #pprint(month_lengths(2004))
    #pprint(month_lengths(1900))

    ml = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0) and ((not (year % 100 == 0)) or (year % 400 == 0)):
        ml[2] = 29
    return ml


def iso2dict(date):
    parts = date.split("-")
    d = {"year": int(parts[0]), "month": int(parts[1]), "day": int(parts[2])}
    return d


def dict2iso(date_obj):
    y = date_obj["year"]
    m = format_2digit_number(date_obj["month"])
    d = format_2digit_number(date_obj["day"])
    return "%s-%s-%s" % (y, m, d)


def date_add(date, amount):
    date = iso2dict(date)
    ml = month_lengths(date["year"])
    x = 0
    while x < amount:
        date["day"] = date["day"] + 1
        if date["day"] > ml[date["month"]]:
            date["day"] = 1
            date["month"] += 1
            if date["month"] >= 13:
                date["month"] = 1
                date["year"] += 1
        x += 1
    return dict2iso(date)
