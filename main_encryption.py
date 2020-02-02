from caesar_encryptor import CaesarEncrypt
from vijener_encryptor import VijenerEnc

import argparse

if __name__ == '__main__':
    my_cipher = argparse.ArgumentParser(prog='main_encryption',
                                        description='Шифровщик Цезаря, Виженера',
                                        epilog='Наслаждайтесь программой!')

    my_cipher.add_argument('method_encrypt', help='Метод шифрования - цезарь/виженер')
    my_cipher.add_argument('your_word', help='Введите ваше слово')
    my_cipher.add_argument('key', help='Введите ключ')
    my_cipher.add_argument('-m', '--mode', help='Режим кодирования/декодирования')
    my_cipher.add_argument('-a', '--alphabet', help='Используемый алфавит')

    args = my_cipher.parse_args()

    if args.method_encrypt == 'цезарь':
        young_encryptor = CaesarEncrypt(word=args.your_word, shift=int(args.key), mode=args.mode,
                                        alphabet=args.alphabet)
        young_encryptor.run()
    else:
        young_encryptor = VijenerEnc(user_word=args.your_word, key_word=args.key, mode=args.mode,
                                     alphabet=args.alphabet)
        young_encryptor.run()
