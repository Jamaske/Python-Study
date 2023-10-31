def head(lines, filepath):
    with open(filepath) as file:
        for line in range(lines):
            yield file.readline()

for i in head(10, "./third.py"):
    print(i, end='')