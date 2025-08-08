import subprocess

def uninstall():
	subprocess.run(["rm", "-rf", "build"])
	subprocess.run(["rm", "-rf", "dist"])
	subprocess.run(["rm", "-rf", "ft_package.egg-info"])
	subprocess.run(["rm", "-rf", "ft_package/__pycache__"])
	subprocess.run(["pip3", "uninstall", "ft_package"])

if __name__ == "__main__":
	uninstall()