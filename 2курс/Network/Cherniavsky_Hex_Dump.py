def Dump(Bytes: bytearray)->str: return '\n'.join(['{0:05X}: {1:<48}  |{2:<16}|'.format(i, *map(''.join,zip(*((f' {el:2X}', chr(el) if 31 < el < 255 else ".") for el in Bytes[i:i+16]))))for i in range(0, len(Bytes), 16)])

data = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456/'
print(Dump(data))