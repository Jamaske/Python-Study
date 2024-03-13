base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def to_binary(s):
    return ''.join(format(i, '08b') for i in bytearray(s, encoding='utf-8'))


def encode_base64(s):
    sample_string = s
    b_sample_string = to_binary(sample_string)
    while len(b_sample_string) % 6 != 0:
        b_sample_string += '0'

    result = ""
    for i in range(0, len(b_sample_string), 6):
        result += base64_table[int(b_sample_string[i:i + 6], 2)]
    while len(result) % 4 != 0:
        result += "="
    return result

test_strings = ["7", "my string", "calculate 5 + 1", "1232"]
for t in test_strings:
    print(encode_base64(t))