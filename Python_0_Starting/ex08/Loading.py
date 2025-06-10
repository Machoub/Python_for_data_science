import time
from time import sleep
from tqdm import tqdm
import os

def calculate_percentage(part: int, whole: int):
    """
    Calculate the percentage of 'part' relative to 'whole'.
    """
    if whole == 0:
        return "Division by zero is not allowed."
    return round((float(part) / float(whole)) * 100)

def timesstamp(starttime: int, curr: int, total_items: int) -> str:
    tim = time.time() - starttime
    speed = curr / tim if tim > 0 else 0
    remaining_time = (total_items - curr) / speed if speed > 0 else 0

    elapsed_minutes, elapsed_seconds = divmod(tim, 60)
    remaining_minutes, remaining_seconds = divmod(remaining_time, 60)

    result = str()
    result += f' [{elapsed_minutes:02.0f}:{elapsed_seconds:02.0f}<'
    result += f'{remaining_minutes:02.0f}:{remaining_seconds:02.0f}, '
    result += f'{speed:05.02f}it/s]'

    return result

def progressBar(barlen: int, curr: int, total_items: int) -> str:
    progress = int(round(barlen) * (curr + 1) / float(total_items))

    progress_str = str()
    progress_str += f"{calculate_percentage(curr + 1, total_items):3d}"
    progress_str += '%'
    progress_str += '|'
    progress_str += '█' * progress + ' ' * (barlen - progress)
    progress_str += '| '
    progress_str += f'{(curr + 1):3d}/{total_items}'

    return progress_str

def ft_tqdm(lst: range) -> None:
    total_items = len(lst)
    size = os.get_terminal_size()
    reqChar = 8 + (len(str(total_items )) * 2) + 26
    barlen = size.columns - reqChar
    starttime = time.time()

    for curr in lst:
        display = str()
        display += progressBar(barlen, curr, total_items)
        display += timesstamp(starttime, curr, total_items)
        print(display, end='\r')
        yield
    
    return

for i in ft_tqdm(range(1000)):
    sleep(0.005)

for i in tqdm(range(1000)):
    sleep(0.005)