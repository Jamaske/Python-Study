N = int(input())

best_string: str = ''
unique_chars: int = 0

for _ in range(N):
    string: str = input()
    chars_num: int = len(set(string))
    if chars_num > unique_chars:
        best_string = string
        unique_chars = chars_num
        
print(unique_chars, best_string)


