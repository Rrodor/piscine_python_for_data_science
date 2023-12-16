import datetime
import time

date = datetime.datetime.now()
seconds = time.time()
sciNotSeconds = "{:.2e}".format(seconds)
print("Seconds since January 1, 1970: ", seconds, " or ", sciNotSeconds, " in scientific notation")
print(date.strftime("%b %d %Y"));
