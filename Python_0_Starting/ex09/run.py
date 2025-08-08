import subprocess
from tqdm import tqdm

def build():
    with tqdm(total=100, desc= "Build ") as pbar:
          subprocess.run(["python3", "setup.py", "sdist bdist_wheel > /dev/null 2>&1"])
          pbar.update(100)

def install():
    with tqdm(total=100, desc= "Install ") as pbar:
        subprocess.run(["pip3", "install", "./dist/ft_package-0.0.1.tar.gz > /dev/null 2>&1"])
        pbar.update(100)

def show():
    with tqdm(total=100, desc= "Show ") as pbar:
        subprocess.run(["pip3", "show", "-v", "ft_package"])
        print()
        pbar.update(100)
        print()

def test():
    with tqdm(total=100, desc="Tester ") as pbar:
        pbar.update(100)
    print()
    subprocess.run(["python3", "tester.py"])

if __name__ == "__main__":
    build()
    install()
    show()
    test()
