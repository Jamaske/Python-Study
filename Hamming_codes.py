TEXT_ENCODING_SIZE = 8


def TextToBin(text):
    """
    produce binary representation of any text
    :param text: string with text
    :return: string with bits
    """
    binary = ''
    for char in text:
        char_code = ord(char)  # get ascii code of a character
        char_code_binary = bin(char_code)[2:]  # get string with binary representation of the code
        binary = binary + char_code_binary
    return binary


def BinToText(binary):
    """
    reconstruct text from its binary representation
    :param binary: string with bits
    :return: string with text
    """
    text = ''
    text_len = len(binary) / TEXT_ENCODING_SIZE
    for i in range(text_len):
        slice_start = i * TEXT_ENCODING_SIZE
        slice_end = (i + 1) * TEXT_ENCODING_SIZE
        char_code_binary = binary[slice_start: slice_end]
        '''
        it is "slice syntax"   your_list[from:to:step]
        it is simular to regular indexing   your_list[index]
        it give you sublist from one you use it on
        starting from first index (included) and ending on second index (excluded)
        third number is a step. it is rarely used and i don't feel like explaining it.
        run code like [1,2,3,4,5,6,7,8,9,10][3:8:2] your self.
        '''
        char_code = int(char_code_binary, 2)  # convert string with binary to int
        char = chr(char_code)  # get char from its code
        text = text + char
    return text


def EncodeBinSequence(binary):
    """
    encode binary sequence to Hamming code
    more info https://www.youtube.com/watch?v=X8jsijhllIA&ab_channel=3Blue1Brown
    :param binary: string with binary sequence
    :return: string with the code (binary too)
    """
    data_index = 0
    code_index = next_power_of_2 = 1
    parity_bits = []
    # write bits from the binary sequence to non powers of 2 indexes of code
    # power of 2 places are required for additional information
    while data_index < len(binary):
        if code_index == next_power_of_2:
            code_index += 1  # this is equivalent to code_index = code_index + 1
            next_power_of_2 *= 2
            continue
            # it is special command to end this iteration of a loop (while)
            # and start next one prematurely

        bit = binary[data_index]
