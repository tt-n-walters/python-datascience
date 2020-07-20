import time

seconds = 0
print(time.time())

while True:
    time.sleep(1)

    seconds += 1
    print(f"\t{seconds}\t\t{seconds // 60:02}:{seconds % 60:02}", end="\r")
