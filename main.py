import subprocess

if __name__ == "__main__":
    for i in range(int(input("Choose number of clients: "))):
        subprocess.call("start python3 cli.py", shell=True)
