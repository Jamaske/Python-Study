#Чернявский Дмитрий МО-201
#Задача №2 кодировка в Base64

from functools import reduce

class Base64:
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" #Base64 -> Ascii
    @staticmethod
    def encode(text)->str:
        code = []
        text += '\x00'*(padding:=(-len(text))%3)
        for idx in range(0, len(text), 3):
            Block = ord(text[idx]) << 16 | ord(text[idx + 1]) << 8 | ord(text[idx + 2])
            code.extend([Base64.base64[Block >> shift & 0x3F] for shift in (18,12,6,0)])
        return ''.join(code[:len(code) - padding] + ['='] * padding)

    table = [0]*43+[62]+[0]*3+[63]+list(range(52,62))+[0]*7+list(range(26))+[0]*6+list(range(26,52))  #Ascii -> Base64
    @staticmethod
    def decode(code)->str:   
        text = []
        for idx in range(0, len(code), 4):
            Block = reduce(lambda acc, next: acc << 6 | next, map(lambda ch: Base64.table[ord(ch)], code[idx : idx + 4]))
            text.extend([chr(Block >> shift & 0xFF) for shift in (16,8,0)])
        return ''.join(text[:len(text) - code.count("=", -2)])



def test():
    msgs = ['12345', 'Base64', 'static_cast<Buffer*>']
    codes = list(map(Base64.encode, msgs))
    results = list(map(Base64.decode, codes))
    for msg, code ,res in zip(msgs, codes, results):
        print(f'"{msg}" -> {code} -> "{res}"')
        print(f'equal: {msg==res}\n')


test()