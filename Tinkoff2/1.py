coma_seq = input().split(",")
ans = []
for entry in coma_seq:
    if '-' in entry:
        a, b = map(int,entry.split("-"))
        for i in range(a, b+1):
            ans.append(str(i))

    else:
        ans.append(entry)
print(' '.join(ans))