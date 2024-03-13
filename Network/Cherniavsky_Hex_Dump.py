Bytes = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456/'
#specify number of bytes per dump line

line_len = 16
Dump = '\n'.join([f'{i:05x}:' + ''.join([ f' {Byte:2x}' for Byte in Bytes[i:i+line_len]])  for i in range(0,len(Bytes), line_len)])

print(Dump)