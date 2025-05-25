def is_safe(report):
    safe = True
    flag = -1
    sgn = report[1] >= report[0]
    n = len(report)
    if sgn:
        for i in range(1,n):
            diff = abs(report[i] - report[i-1])
            if report[i] < report[i-1] or diff > 3 or diff == 0:
                safe = False
                flag = i-1
                break
    else:
        for j in range(1,n):
            diff = abs(report[j] - report[j-1])
            if report[j] > report[j-1] or diff > 3 or diff == 0:
                safe = False
                flag = j-1
                break
    return safe, flag 

with open("input1.txt", "r") as f:
    reader = f.read().strip().split("\n")

counter = 0
for line in reader:
    report = [int(n) for n in line.strip().split()]
    value, index = is_safe(report)
    if value: 
        counter += 1
    else:
        left, right = report.copy(), report.copy()
        left.pop(index)
        right.pop(index+1)
        left_value, _ = is_safe(left)
        right_value, _ = is_safe(right)
        if left_value: 
            counter += 1
        elif right_value:
            counter += 1
        elif index == 1 and report[1] != report[0]:
            wo_first = report.copy()
            wo_first.pop(0)
            counter += 1 if is_safe(wo_first)[0] else 0

print(counter)

