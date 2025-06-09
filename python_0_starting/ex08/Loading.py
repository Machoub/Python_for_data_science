
import time
from time import sleep
import os

def calculate_percentage(part: int, whole: int):
    """
    Calculate the percentage of 'part' relative to 'whole'.
    """
    if whole == 0:
        return "Division by zero is not allowed."
    return round((float(part) / float(whole)) * 100)

def progressBar(barlen: int, curr: int, total_items: int) -> str:
    progress = int(round(barlen) * (curr + 1) / float(total_items))

    progress_str = str()
    progress_str += f"{calculate_percentage(curr + 1, total_items):3d}"

def ft_tqdm(lst: range) -> None:
    total_items = len(lst)
    size = os.get_terminal_size()
    reqChar = 8 + (len(str(total_items )) * 2) + 26
    barlen = size.columns - reqChar
    starttime = time.time()

    for curr in lst:
        display = str()
        display += progressBar(barlen, curr, total_items)
        ##display += timesstamp(starttime, curr, total_items)
        print(display, end='\r')
        yield
    
    return

for i in ft_tqdm(range(333)):
    sleep(0.005)