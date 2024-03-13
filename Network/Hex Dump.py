Bytes = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456/'
line_len = 8
Dump = '\n'.join([f'{i:05x}:' + ''.join([ f' {Byte:2x}' for Byte in Bytes[i:i+line_len]])  for i in range(0,len(Bytes), line_len)])

print(Dump)