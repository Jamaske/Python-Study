N, Q = map(int, input().split())
words = []
for i in range(N):
    words.append(input())




def binserch(prefix):
    global words, N
    l = 0
    h = N - 1
    while l < h:
        m = (l+h) // 2
        if words[m] < prefix:
            l = m + 1
        else:
            h = m
    if (l != h):print("ERROR")
    return l
        



def isPrefix(prefix, word):
    return prefix == word[:len(prefix)]



parse = lambda x: (int(x[0]), x[1])
for i in range(Q):
    shift, prefix = parse(input().split())
    idx = binserch(prefix)
    #print(f'bin: {idx=}: {words[idx]}')
    idx += shift - 1
    if idx < N:
        #print(f'shifted: idx={idx}: {words[idx]}')
        word = words[idx]
        if isPrefix(prefix,word):
            print(idx + 1,)
        else: print(-1,)
    else: print(-1,)
    #print()



'''
10 3
aa
aaa
aab
ab
abc
ac
ba
daa
dab
dadba
3 aa
2 da
4 da


'''