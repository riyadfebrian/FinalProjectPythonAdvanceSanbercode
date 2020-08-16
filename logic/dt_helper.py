from datetime import datetime as dt
import datetime

TIME_FORMAT = '%Y-%m-%d'


def convert_from_str(args):
    return [dt.strptime(x, TIME_FORMAT) for x in args]


def convert_to_str(args):
    return [x.strftime(TIME_FORMAT) for x in args]


def next_date(args, idx):
    norm = convert_from_str(args)
    n_date = [x for x in norm if x >= norm[idx]]
    return convert_to_str(n_date)


def list_date(args):
    return [x[0] for x in args]


def minus_one(args):
    norm = convert_from_str([args])
    norm = norm[0] - datetime.timedelta(days=1)
    return convert_to_str([norm])[0]


# Dynamic generated submenu
def endDate(all_date, args):
    idx = [index for index, val in enumerate(all_date) if val == args]
    return next_date(all_date, idx[0])


def dayBefore(count):
    now = datetime.date.today()
    delta = datetime.timedelta(days=count)
    date_since = now - delta
    return date_since
