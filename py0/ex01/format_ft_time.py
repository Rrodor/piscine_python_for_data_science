import datetime
import time

date = datetime.datetime.now()
seconds = round(time.time(), 4)
sciNotSeconds = "{:.2e}".format(seconds)
print("Seconds since January 1, 1970: " + f"{seconds:,}", " or ", sciNotSeconds, " in scientific notation")
print(date.strftime("%b %d %Y"));
