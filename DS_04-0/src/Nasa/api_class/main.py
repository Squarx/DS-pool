from datetime import datetime
from API import Api_Nasa

# def validtor(self):
# tt = datetime.strptime(self.__params['date'], "%Y-%m-%d").date()
# date_min = datetime.strptime("1995-06-16", "%Y-%m-%d").date()
# count = self.__params['count']
# start_date = self.__params['start_date']
# end_date = self.__params['end_date']
# if tt < date_min:
#     return 1
# elif self.__params['date'] != "":
#     self.__params['count'] = ""
#     self.__params['start_date'] = ""
#     self.__params['end_date'] = ""
#     return 0
# else:
#     return 0


def valid(date):
    tt = ""
    date_min = datetime.strptime("1995-06-16", "%Y-%m-%d").date()
    try:
        tt = datetime.strptime(date, "%Y-%m-%d").date()
        date_min = datetime.strptime("1995-06-16", "%Y-%m-%d").date()
        if tt < date_min:
            tt = date_min
    except ValueError:
        tt = date_min
    return str(tt)


tmp = Api_Nasa(count=1)
print(tmp.get_response())
