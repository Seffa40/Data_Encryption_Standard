
initial_permutation_table = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

final_permutation_table = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

expansion_table = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

s_boxes = {
    0: [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    1: [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    2: [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    3: [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    4: [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    5: [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    6: [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    7: [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
}

p_box_table = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

def initial_permutation(text, table):
    return ''.join(text[i - 1] for i in table)

def expansion(text, table):
    return ''.join(text[i - 1] for i in table)

def xor(bits1, bits2):
    return ''.join('0' if bit1 == bit2 else '1' for bit1, bit2 in zip(bits1, bits2))

def substitute(expanded_half_block, s_boxes):
    output = ''
    for i in range(8):
        block = expanded_half_block[i*6:(i+1)*6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        s_box_value = s_boxes[i][row][col]
        output += f'{s_box_value:04b}'
    return output

def p_box_permutation(text, table):
    return ''.join(text[i - 1] for i in table)

def des_function(right, key):
    expanded_right = expansion(right, expansion_table)
    xor_result = xor(expanded_right, key)
    substituted = substitute(xor_result, s_boxes)
    return p_box_permutation(substituted, p_box_table)

def process_block(block, keys):
    block = initial_permutation(block, initial_permutation_table)
    left, right = block[:32], block[32:]
    for key in keys:
        new_right = xor(left, des_function(right, key))
        left, right = right, new_right
    final_block = initial_permutation(right + left, final_permutation_table)
    return final_block

def des_encrypt(plain_text, keys):

    binary_text = ''.join(format(ord(char), '08b') for char in plain_text)
    while len(binary_text) % 64 != 0:
        binary_text += '0'  # Padding with zeros
    cipher_text = ''
    for i in range(0, len(binary_text), 64):
        block = binary_text[i:i+64]
        cipher_text += process_block(block, keys)
    return cipher_text

def des_decrypt(cipher_text, keys):
    plain_text = ''
    for i in range(0, len(cipher_text), 64):
        block = cipher_text[i:i+64]
        plain_text += process_block(block, keys[::-1])
    plain_text = ''.join(chr(int(plain_text[i:i+8], 2)) for i in range(0, len(plain_text), 8))
    return plain_text.rstrip('\x00')


key = '0001001100110100010101110111100110011011101111001101111111110001'
keys = [key for _ in range(16)]
print()
plain_text = ('I remember as a child, and as a young budding naturalist, spending all my time observing and testing\n'
              'the world around me moving pieces, altering the flow of things, and documenting ways the world \n'
              'responded to me. Now, as an adult and a professional naturalist, I’ve approached language in the \n'
              'same way, not from an academic point of view but as a curious child still building little mud dams \n'
              'in creeks and chasing after frogs. So this book is an odd thing: it is a naturalist’s walk through \n'
              'the language-making landscape of the English language, and following in the naturalist’s tradition \n'
              'it combines observation, experimentation, speculation, and documentation activities we don’t normally \n'
              'associate with language. This book is about testing, experimenting, and playing with language. It is \n'
              'a handbook of tools and techniques for taking words apart and putting them back together again in ways\n'
              ' that I hope are meaningful and legitimate (or even illegitimate). This book is about peeling back \n'
              'layers in search of the language-making energy of the human spirit. It is about the gaps in meaning \n'
              'that we urgently need to notice and name the places where our dreams and ideals are no longer fulfilled\n'
              ' by a society that has become fast-paced and hyper-commercialized. Language is meant to be a playful,\n'
              ' ever-shifting creation but we have been taught, and most of us continue to believe, that language must\n'
              'obediently follow precisely prescribed rules that govern clear sentence structures, specific word orders,\n'
              ' correct spellings, and proper pronunciations. If you make a mistake or step out of bounds there are \n'
              'countless, self-appointed language experts who will promptly push you back into safe terrain and scold \n'
              'you for your errors. And in case you need reminding, there are hundreds of dictionaries and grammar books\n'
              ' to ensure that you remember the “right” way to use English.')
print()
cipher_text = des_encrypt(plain_text, keys)
decrypted_text = des_decrypt(cipher_text, keys)
print()
print("Plain text: ", plain_text)
print()
print()
print("Cipher text: ","\n", cipher_text)

print()
print()
print("Decrypted text: ", decrypted_text)
print()

def brute_force_decrypt(cipher_text):
    for i in range(2 ** 56):
        key = format(i, '056b')
        decrypted_text = des_decrypt(cipher_text, [key]*16)
        if decrypted_text.isprintable():
            print("hacked successful with key:", key)
            print("hacked text:", decrypted_text)
            return
    print("Brute-force decryption failed. No meaningful text found.")

brute_force_decrypt(cipher_text)
