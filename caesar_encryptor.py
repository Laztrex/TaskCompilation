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

    def __init__(self, word, shift, mode='encode', alphabet='ru'):
        self.state = mode
        self.alphabet = alphabet  # temporarily hard decision
        self.user_word = word.replace(' ', '')
        self.shift = shift

    def check_alphabet(self, check_letter=None):
        if check_letter:
            if check_letter not in self.alphabet:
                self.alphabet = alphabet_settings.ru[0] if check_letter in alphabet_settings.ru[0] \
                    else alphabet_settings.eng[0]
                return False
        # else Exc

        if self.alphabet == 'ru':
            self.alphabet = alphabet_settings.ru
        else:
            self.alphabet = alphabet_settings.eng

    def run(self):
        self.check_alphabet()
        if self.state == 'encode':
            self.encoder()
        elif self.state == 'decode':
            self.decoder()
        else:
            if '-' in self.shift:
                self.decoder()
            else:
                self.encoder()

    def encoder(self):
        # if self.shift > 31:
        #
        # for element in range(self.shift):
        #     shift_alphabet = self.alphabet[0][element + 1:] + self.alphabet[0][:element + 1]
        #     if element > 31:
        #         if element == 32:  # Не нравится мне этот метод решения проблемы shift > числа элементов списка :(
        #             self.alphabet.append(shift_alphabet)  # ух как не нравится!
        #         else:
        #             shift_alphabet = self.alphabet[0][(element % 32):] + self.alphabet[0][:(element % 32)]  # фууу
        #             self.alphabet.append(shift_alphabet)
        #             continue
        #     self.alphabet.append(shift_alphabet)

        secret_word = ''

        for letter in self.user_word.lower():
            secret_word += self._secret_permutation(letter)

        print(secret_word)

        # for num, char in enumerate(self.alphabet[0]):
        #     if char == letter:
        #         new_message = self.alphabet[0][abs((num + self.shift)) % len(self.alphabet[0])]
        #         secret_word += new_message
        #         break
        #     else:
        #         continue

    def _secret_permutation(self, letter):

        for num, char in enumerate(self.alphabet[0]):

            if char == letter:
                return self.alphabet[0][abs((num + self.shift)) % len(self.alphabet[0])]
            else:
                continue

        # else:
        #     if not self.check_alphabet(letter):
        #         result = self._secret_permutation(letter=letter)
        #         return result

    def decoder(self):
        # DECODER.
        # Необходимо написать программу, которая расшифровывает заданное зашифрованное слово силами Шифра Цезаря
        # Подробнее о шифре Цезаря - (https://is.gd/rcGAsp).
        # Дано зашифрованное сообщение, число сдвигов и русский алфавит

        """
         Пример:
        # message_encrypt = 'фхнжйч'
        # shift_encrypt = 5
        # Вывод: Зашифрованным словом было - привет
        """

        # for element in range(self.shift):
        #     shift_alphabet = self.alphabet[0][element + 1:] + self.alphabet[0][:element + 1]
        #     self.alphabet.append(shift_alphabet)

        # secret_word = ''
        # for letter in self.user_word.lower():
        #     for num, char in enumerate(self.alphabet[0]):
        #
        #         if char == letter:
        #             new_message = self.alphabet[0][abs((num - self.shift)) % len(self.alphabet[0])]
        #             secret_word += new_message
        #             break
        #         else:
        #             continue
        #     else:
        #         if self.check_alphabet(check_letter=letter):
        #
        #
        # print('Зашифрованным словом было -', secret_word)


if __name__ == "__main__":
    young_encryptor = CaesarEncrypt(word=input('Введите слово: '),
                                    shift=int(input('Введите сдвиг: ')),
                                    mode='encode',
                                    alphabet='ru')
    young_encryptor.run()

# TODO ввести проверку принадлежности символа алфавиту
# TODO включить возможность ввода целого предложения с пробелами и знаками препинания (которые тоже будут шифроваться)
# TODO добавить английский алфавит
