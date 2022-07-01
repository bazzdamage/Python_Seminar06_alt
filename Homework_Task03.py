# ROT13 - это простой шифр подстановки букв, который заменяет букву буквой,
# которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 .
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть.
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений).
import string

text_1 = 'Regular expressions can be concatenated to form'


def rot_n_enc(text: str, n: int):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    upper_start = ord(upper[0])
    lower_start = ord(lower[0])
    out = ''
    for letter in text:
        if letter in upper:
            out += chr(upper_start + (ord(letter) - upper_start + n) % 26)
        elif letter in lower:
            out += chr(lower_start + (ord(letter) - lower_start + n) % 26)
        else:
            out += letter
    return out


def rot_n_dec(text: str, n: int):
    return rot_n_enc(text, -n)


print(rot_n_dec(text_1, 13))
print(rot_n_dec(rot_n_enc(text_1, 13), 13))
