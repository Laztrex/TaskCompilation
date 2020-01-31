from caesar_encryptor import CaesarEncrypt

import argparse

if __name__ == '__main__':
    my_cipher = argparse.ArgumentParser()

    my_cipher.add_argument('your_word', help='Введите ваше слово')
    my_cipher.add_argument('shift', help='Введите сдвиг')
    my_cipher.add_argument('-m', '--mode', help='Режим кодирования/декодирования')
    my_cipher.add_argument('-a', '--alphabet', help='Используемый алфавит')

    args = my_cipher.parse_args()

    young_encryptor = CaesarEncrypt(word=args.your_word, shift=int(args.shift), mode=args.mode, alphabet=args.alphabet)
    young_encryptor.run()
