def is_safe(report):
    safe = True
    sgn = report[1] > report[0]
    n = len(report)
    if sgn:
        for i in range(n - 1):
            diff = abs(report[i+1] - report[i])
            if report[i+1] < report[i] or diff > 3 or diff == 0:
                safe = False
                break
    else:
        for i in range(n - 1):
            diff = abs(report[i+1] - report[i])
            if report[i+1] > report[i] or diff > 3 or diff == 0:
                safe = False
                break
    return safe

with open("input1.txt", "r") as f:
    reader = f.read().strip().split("\n")

counter = 0
for line in reader:
    report = [int(n) for n in line.strip().split()]

    if is_safe(report):
        counter += 1

print(counter)




