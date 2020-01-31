#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дан русский алфавит.

import alphabet_settings


# Необходимо написать программу, шифрующее слово с помощью Шифра Цезаря(https://is.gd/rcGAsp).
# Программа должна принимать на вход от пользователя слово и число сдвигов.
#
# Допускается:
#    - Использование цикла for;
#    - Операции со списками;
#    - Ввод только строчными буквами (НЕ использовать пробелы, прописные буквы);
#    - Слово должно состоять из букв русского алфавита.
#
# На выходе программа должна выдавать только результат.
#
# Для примера:
# [
# абвгдеёжзийклмнопрстуфхцчшщъыьэюя,
# бвгдеёжзийклмнопрстуфхцчшщъыьэюяа,
# вгдеёжзийклмнопрстуфхцчшщъыьэюяаб,
# вгдеёжзийклмнопрстуфхцчшщъыьэюяаб,
# ]
#
# Слово:          скиллбокс
# Число сдвигов:  3
# Вывод:          фнлоодснф

# --------------------------------------------------------------------------------


class CaesarEncrypt:

    def __init__(self, word, shift, mode=None, alphabet=None):
        self.state = mode
        self.alphabet = alphabet  # temporarily hard decision
        self.user_word = word.replace(' ', '')
        self.shift = shift

    def run(self):
        self._check_alphabet()
        if self.state == 'decode':
            self.shift = 0 - self.shift
        self.encoder()

    def encoder(self):
        secret_word = ''

        for letter in self.user_word.lower():
            secret_word += self._secret_permutation(letter)

        print(secret_word)

    def _check_alphabet(self, check_letter=None):
        if check_letter:
            if check_letter.isalpha():
                if check_letter not in self.alphabet:
                    self.alphabet = alphabet_settings.ru if check_letter in alphabet_settings.ru \
                        else alphabet_settings.eng
                    return False
            else:
                return True

        if self.alphabet == 'ru':
            self.alphabet = alphabet_settings.ru
        else:
            self.alphabet = alphabet_settings.eng

    def _secret_permutation(self, letter):
        for num, char in enumerate(self.alphabet):
            if char == letter:
                return self.alphabet[(num + self.shift) % len(self.alphabet)]
            else:
                continue
        else:
            if not self._check_alphabet(letter):
                return self._secret_permutation(letter=letter)
            return ''


if __name__ == "__main__":
    young_encryptor = CaesarEncrypt(word=input('Введите слово: '),
                                    shift=int(input('Введите сдвиг: ')),
                                    alphabet='ru')
    young_encryptor.run()


# Пояснения
# DECODER.
# Необходимо написать программу, которая расшифровывает заданное зашифрованное слово силами Шифра Цезаря
# Подробнее о шифре Цезаря - (https://is.gd/rcGAsp).
# Дано зашифрованное сообщение, число сдвигов и русский алфавит

# """
#  Пример:
# # message_encrypt = 'фхнжйч'
# # shift_encrypt = 5
# # Вывод: Зашифрованным словом было - привет
# """
