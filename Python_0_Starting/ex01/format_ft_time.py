from datetime import date
import time

print(f"Seconds since {time.strftime('%B %d, %Y', time.gmtime(0))} : {time.time():,.4f} or {time.time():.2e} in scientific notation\n{date.today().strftime('%b %d %Y')}")
