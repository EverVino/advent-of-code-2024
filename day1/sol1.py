with open("input1.txt", "r") as f:
    reader = f.readlines()
A = []
B = []
for line in reader:
    if line.strip():
        a, b = line.strip().split()
        A.append(int(a))
        B.append(int(b))

A.sort()
B.sort()
n = len(A)
d = 0
for i in range(n):
    d += abs(A[i] - B[i])
print(d)
