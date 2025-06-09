from datetime import date
import time

epoch = time.strftime("Seconds since %B %d, %Y: ", time.gmtime(0))
sec = time.time()

print(epoch, sec, " or ", f"{sec:.2e}", " in scientific notation")
print(date.today().strftime('%b %d %Y'))