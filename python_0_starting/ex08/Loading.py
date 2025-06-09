from tqdm import tqdm
from time import sleep

def ft_tqdm(lst: range) -> None:
    for i in range(101):
        yield print(f'{i}%')

for i in ft_tqdm(range(333)):
    sleep(0.005)

for i in tqdm(range(1000)):
    sleep(0.005)