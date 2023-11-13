from itertools import product
from collections import OrderedDict
import random


def caesarCipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ''
    for char in text:
        if char == ' ':
            result += char
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


text = 'Isyuk'
shift = 8
encrypt = caesarCipher(text, shift)
decrypt = caesarCipher(encrypt, shift, decrypt=True)
print(f'''
Шифр Цезаря     (ключ: {shift})    
Исходный текст:        {text}
Зашифрованный текст:   {encrypt}
Дешифрованный текст:   {decrypt}
''')


def keywordCipher(text, key, decrypt=False):
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shiftedAlphabet = ''.join(
        OrderedDict.fromkeys(key.lower() + alphabet.lower()))

    for char in text:
        charIsLower = char.islower()
        charIndex = ord(char) - 97 if charIsLower else ord(char) - 65
        if decrypt:
            charIndex = shiftedAlphabet.find(
                char) if charIsLower else shiftedAlphabet.upper().find(char)
            result += alphabet[charIndex] if charIsLower else alphabet[charIndex].upper()
            continue
        result += shiftedAlphabet[charIndex] if charIsLower else shiftedAlphabet[charIndex].upper()
    return result


text = 'Isyuk'
key = 'cipher'
encrypt = keywordCipher(text, key)
decrypt = keywordCipher(encrypt, key, decrypt=True)
print(f'''
Лозунговый шифр (ключ: {key})
Исходный текст:        {text}
Зашифрованный текст:   {encrypt}
Дешифрованный текст:   {decrypt}
''')


def polybiusSquareCipher(text, decrypt=False):
    result = ''
    alphabet = {
        'a': '11', 'b': '12', 'c': '13', 'd': '14', 'e': '15',
        'f': '21', 'g': '22', 'h': '23', 'i': '24', 'j': '24',
        'k': '25', 'l': '31', 'm': '32', 'n': '33', 'o': '34',
        'p': '35', 'q': '41', 'r': '42', 's': '43', 't': '44',
        'u': '45', 'v': '51', 'w': '52', 'x': '53', 'y': '54',
        'z': '55'
    }
    text = text.lower()
    if decrypt:
        return ''.join([list(alphabet.keys())[list(alphabet.values()).index(text[i:i+2])] for i in range(0, len(text), 2)])
    return ''.join([alphabet[char] for char in text])


text = 'Isyuk'
encrypt = polybiusSquareCipher(text)
decrypt = polybiusSquareCipher(encrypt, decrypt=True)
print(f'''
Полибианский квадрат
Исходный текст:        {text}
Зашифрованный текст:   {encrypt}
Дешифрованный текст:   {decrypt}
''')


def trithemiusCipher(text, step=1, initialShift=3, isAscending=True, decrypt=False):
    if decrypt:
        isAscending = not isAscending
    result = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(len(text)):
        char = text[i]
        if char.upper() in alphabet:
            charIndex = alphabet.index(char.upper())
            shift = initialShift + i * step
            if isAscending:
                encrypterIndex = (charIndex + shift) % len(alphabet)
            else:
                encrypterIndex = (charIndex - shift) % len(alphabet)
            encryptedChar = alphabet[encrypterIndex] if char.isupper(
            ) else alphabet[encrypterIndex].lower()
            result += encryptedChar
        else:
            result += char
    return result


text = 'Isyuk'
encrypt = trithemiusCipher(text)
decrypt = trithemiusCipher(encrypt, decrypt=True)
print(f'''
Шифрующая система Трисемуса
Исходный текст:        {text}
Зашифрованный текст:   {encrypt}
Дешифрованный текст:   {decrypt}
''')


def playfairCipher(text, key, shift=1, decrypt=False):
    if decrypt:
        shift = -shift
    result = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    text = text.upper().replace(' ', '').replace('J', 'I')

    key = key.upper()
    key = ''.join(sorted(set(key), key=key.index)).replace('J', 'I')
    key += ''.join(ch for ch in alphabet if ch not in key)
    matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]

    if len(text) % 2 != 0:
        text += 'X'

    for i in range(0, len(text), 2):
        ra, ca = getPosition(matrix, text[i])
        rb, cb = getPosition(matrix, text[i + 1])

        if ra == rb:
            result += matrix[ra][(ca+shift) % 5] + matrix[rb][(cb+shift) % 5]
        elif ca == cb:
            result += matrix[(ra+shift) % 5][ca] + matrix[(rb+shift) % 5][cb]
        else:
            result += matrix[ra][cb] + matrix[rb][ca]

    return result


def getPosition(matrix, ch):
    for i, j in product(range(5), repeat=2):
        if matrix[i][j] == ch:
            return i, j


text = 'Isyuk'
key = 'cipher'
encrypt = playfairCipher(text, key, shift=3)
decrypt = playfairCipher(encrypt, key, shift=3, decrypt=True)
print(f'''
Шифр Playfair   (ключ: {key})
Исходный текст:        {text}
Зашифрованный текст:   {encrypt}
Дешифрованный текст:   {decrypt}
''')


def homophoneCipher(text, decrypt=False):
    result = ''
    dictionary = {
        'a': ['@', '4', 'а', 'Δ'],
        'b': ['8', '6', 'ß', 'β'],
        'c': ['(', '[', '{', '©'],
        'd': [')', ']', '}', '∂'],
        'e': ['3', '€', '£', '℮'],
        'f': ['=', '+', '♭', 'ƒ'],
        'g': ['9', 'q', 'ɢ', 'ɡ'],
        'h': ['#', '4', 'ħ', 'ʜ'],
        'i': ['1', '|', '!', 'ı'],
        'j': ['j', 'ʝ', 'ɉ', 'ɟ'],
        'k': ['<', 'k', 'κ', 'ҝ'],
        'l': ['7', 'l', 'λ', 'ℓ'],
        'm': ['m', 'µ', 'ɱ', '₥'],
        'n': ['n', 'η', 'ɲ', '₦'],
        'o': ['0', 'o', 'ο', '○'],
        'p': ['p', 'ρ', '¶', '₱'],
        'q': ['q', '9', 'ɋ', 'ℚ'],
        'r': ['r', '2', '®', 'ɾ'],
        's': ['5', 's', 'σ', '§'],
        't': ['t', '7', 'τ', '†'],
        'u': ['u', 'υ', 'μ', '∪'],
        'v': ['v', 'ν', '∨', '⋁'],
        'w': ['w', 'ω', 'ψ', '₩'],
        'x': ['x', 'χ', '×', '⊗'],
        'y': ['y', 'γ', '¥', 'ɣ'],
        'z': ['z', 'ζ', 'ℨ', 'ƶ']
    }

    if decrypt:
        for char in text:
            matches = []
            for letter in dictionary:
                if char in dictionary[letter]:
                    matches.append(letter)
            if matches:
                result += random.choice(matches)
            else:
                result += char
        return result

    for char in text.lower():
        if char in dictionary:
            result += random.choice(dictionary[char])
        else:
            result += char
    return result


text = 'Isyuk'
encrypt = homophoneCipher(text)
decrypt = homophoneCipher(encrypt, decrypt=True)
print(f'''
Система омофонов
Исходный текст:        {text}
Зашифрованный текст:   {encrypt}
Дешифрованный текст:   {decrypt}
''')


def visionersCipher(text, seed=1, decrypt=False):
    result = ''
    alphabets = getAlphabets(len(text), seed)

    index = 0
    for char in text:
        if char.isalpha():
            islower = char.islower()
            alphabet = alphabets[index]
            index += 1
            if decrypt:
                charIndex = alphabet.index(char.lower())
                result += (chr(charIndex + ord('a'))
                           if islower else chr(charIndex + ord('A')))
            else:
                charIndex = ord(char) - (ord('a') if islower else ord('A'))
                result += (alphabet[charIndex]
                           if islower else alphabet[charIndex].upper())
        else:
            result += char

    return result


def getAlphabets(quantity, seed):
    result = []
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for i in range(0, quantity):
        random.seed(seed + i)
        random.shuffle(alphabet)
        result.append(''.join(alphabet))

    return result


text = 'Isyuk'
encrypt = visionersCipher(text, seed=45)
decrypt = visionersCipher(encrypt, seed=45, decrypt=True)
print(f'''
Шифр Вижинера
Исходный текст:        {text}
Зашифрованный текст:   {encrypt}
Дешифрованный текст:   {decrypt}
''')
