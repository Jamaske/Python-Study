def encode1(text)->str:
    base64 = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
        ]
    CharIdx = 0
    code = []
    BitBuffer = 0
    BitStored = 0
    while True:
        if BitStored < 6: #хватит ли бит в буффере на следующий символ base64
            if CharIdx >= len(text):break
            BitBuffer = BitBuffer << 8 | ord(text[CharIdx]) #добавляем биты справа от уже имеющихся
            CharIdx += 1
            BitStored += 8
        code.append(base64[BitBuffer >> BitStored - 6]) #переводим левые (более старые) 6 в base64
        BitStored -= 6
        BitBuffer &= ~(0b111111 << BitStored) # обнуляем левые 6 бит

    if BitStored:
        code.append(base64[BitBuffer << 6 - BitStored])# к оставшимся битам нули слева
    code.append('='*(3-(len(code)+3)%4)) #padding
    
    return ''.join(code)

def encode2(text)->str:
    base64 = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
        ]
    idx = 0
    code = []
    BitHolder = 0
    while idx < (len(text) - 2):
        BitHolder = ( ord(text[idx]) << 16 | ord(text[idx + 1]) << 8 | ord(text[idx + 2]))
        code.extend([base64[BitHolder >> 18], base64[BitHolder >> 12 & 0b111111], base64[BitHolder >> 6 & 0b111111], base64[BitHolder & 0b111111]])
        idx += 3
    
    if idx < len(text):
        code.append(base64[(BitHolder := ord(text[idx])) >> 2])
        if idx:= idx + 1 < len(text):
            BitHolder = BitHolder << 8 & 0x30 | ord(text[idx])
            code.extend([base64[BitHolder >> 4], base64[BitHolder & 0b1111], '='])
        else: code.extend([base64[BitHolder << 4 & 0b110000], '=', '='])    
    return ''.join(code)



print(encode2('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/') , encode1('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'))