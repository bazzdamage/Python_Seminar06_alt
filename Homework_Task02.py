# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных файлах
# (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста).
from itertools import groupby


def rle_enc(filename: str, out: str):
    with open(filename, 'r') as f:
        text = f.read()
    # encoded = [[list(group) for k, group in groupby(text)]]
    with open(out, 'w+') as f:
        f.write(''.join(['{}{}'.format(k, sum(1 for _ in group)) for k, group in groupby(text)]))


# не особо заморачивался с цифрами более 9, так бы прописал поиск первого вхождения "нецифры" в подстроку наверное :)
def rle_dec(filename: str, out: str):
    with open(filename, 'r') as f:
        text = f.read()
    with open(out, 'w+') as f:
        f.write(''.join([int(text[i + 1]) * text[i] for i in range(0, len(text), 2)]))


rle_enc('rle_text_for_enc.txt', 'rle_encoded_text.txt')
rle_dec('rle_encoded_text.txt', 'rle_decoded_text.txt')
