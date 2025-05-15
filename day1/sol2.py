with open("input1.txt", "r") as f:
    reader = f.read().strip().split("\n")

A, B = [], []

for line in reader:
    a, b = line.split()
    A.append(int(a))
    B.append(int(b))

counter = {}
for number in B:
    if number not in counter:
        counter[number] = 0
    counter[number] += 1
d = 0
for number in A:
    if number not in counter:
        continue
    d += number*counter[number]

print(d)

