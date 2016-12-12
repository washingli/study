# #coding=utf-8

import time
import datetime
oneday=datetime.timedelta(days=1)
today=datetime.date.today()
yesterday=today-oneday
tommorrow=today+oneday
print(yesterday,today,tommorrow)