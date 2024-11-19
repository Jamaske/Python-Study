inp_seq = input()[::-1] #gota how to lazyly flip input
allowed_chars = set(input()) # set for faster query
allowed_chars_len = len(allowed_chars)
max_len = int(input())

# simple solution using map. may need to swith to list[ord(ch)]
# leadinf and realing edges of the sliding window
char_c = {}
trealing = -1
new_window = False
for leading, ch in enumerate(inp_seq):
    if ch not in allowed_chars:#disallowed char => scrap curent window
        new_window = True
    elif new_window:#wait until walid char to create new window
        trealing = leading
        char_c.clear()
        new_window = False
    else:
        char_c[ch] = char_c.get(ch, 0) + 1
        if leading - trealing > max_len:
            trealing += 1# = leading - max_len
            if char_c[inp_seq[trealing]]:
                char_c[inp_seq[trealing]] -= 1
            else:
                char_c.pop(inp_seq[trealing])

        if len(char_c) == allowed_chars_len:#all required characters are in window

            print(inp_seq[trealing+1: leading+1][::-1])# питон слайсы момент
            break
else:
    print(-1)