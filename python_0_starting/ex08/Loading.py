
import time
from time import sleep
import os

def progressBar(barlen: int, curr: int, total_items: int) -> str:
     

def ft_tqdm(lst: range) -> None:
    total_items = len(lst)
    size = os.get_terminal_size()
    reqChar = 8 + (len(str(total_items )) * 2) + 26
    barlen = size.columns - reqChar
    starttime = time.time()

    for curr in lst:
        display = str()
        display = progressBar(barlen, curr, total_items)
        display = timesstamp(starttime, curr, total_items)
        print(display, end='\r')
        yield
    
    return

for i in ft_tqdm(range(333)):
    sleep(0.005)