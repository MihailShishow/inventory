import datetime
import re


def str_to_date(date_str):
    '''
    Transforms string in format yyyy-mm-dd into a valid Pythonical date object.

    P.S. It could be done with .split() method, but with unusual date formats split will not work.
    To adapt to a new date format just change regex variable.
    '''
    regex = r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})$'
    year_str, month_str, day_str = re.fullmatch(regex, date_str).groups()
    return datetime.date(year=int(year_str), month=int(month_str), day=int(day_str))

