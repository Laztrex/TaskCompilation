from caesar_encryptor import CaesarEncrypt
from vijener_encryptor import VijenerEnc

import argparse


class NotMethodEncError(Exception):
    def __init__(self):
        self.name = 'NotMethodEncError'

    def __str__(self):
        return f'Такого метода кодирования пока что не существует: {self.name}'


def main(method, **kwargs):
    if method == 'цезарь':
        young_encryptor = CaesarEncrypt(**kwargs)
        young_encryptor.run()
    elif method == 'виженер':
        young_encryptor = VijenerEnc(**kwargs)
        young_encryptor.run()
    else:
        raise NotMethodEncError


if __name__ == '__main__':
    my_cipher = argparse.ArgumentParser(prog='main_encryption',
                                        description='Шифровщик Цезаря, Виженера',
                                        epilog='Наслаждайтесь программой!')

    my_cipher.add_argument('method_encrypt', help='Метод шифрования - цезарь/виженер')
    my_cipher.add_argument('word', help='Введите ваше слово')
    my_cipher.add_argument('key', help='Введите ключ')
    my_cipher.add_argument('-m', '--mode', help='Режим кодирования/декодирования', default='encode')
    my_cipher.add_argument('-a', '--alphabet', help='Используемый алфавит', default='ru')

    args = my_cipher.parse_args()
    main(method=args.method_encrypt, word=args.word, key=args.key, mode=args.mode, alphabet=args.alphabet)

