import sys
input = sys.stdin.read

data = input().splitlines()
N = int(data[0])
work_schedule = dict()

index = 1
for _ in range(N):
    for work_hour in [4, 6, 4, 10]:
        names = data[index].split()
        index += 1
        for name in names:
            if name in work_schedule:
                work_schedule[name] += work_hour
            else:
                work_schedule[name] = work_hour

if '-' in work_schedule.keys():
    work_schedule.pop('-')

if work_schedule:
    max_time = max(work_schedule.values())
    min_time = min(work_schedule.values())
    if max_time - min_time <= 12:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")