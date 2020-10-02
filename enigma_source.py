from string import ascii_uppercase


class EnigmaEngine:

    _ALPHABET = ascii_uppercase
    _B_REFLECTOR = ['AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW']
    _RDICT = {1: ('AELTPHQXRU', 'BKNW', 'CMOY', 'DFG', 'IV', 'JZ', 'S'),
             2: ('FIXVYOMW', 'CDKLHUP', 'ESZ', 'BJ', 'GR', 'NT', 'A', 'Q'),
             3: ('ABDHPEJT', 'CFLVMZOYQIRWUKXSG', 'N'),
             4: ('AEPLIYWCOXMRFZBSTGJQNH', 'DV', 'KU'),
             5: ('AVOLDRWFIUQ', 'BZKSMNHYC', 'EGTJPX'),
             6: ('AJQDVLEOZWIYTS', 'CGMNHFUX', 'BPRK'),
             7: ('ANOUPFRIMBZTLWKSVEGCJYDHXQ'),
             8: ('AFLSETWUNDHOZVICQ', 'BKJ', 'GXY', 'MPR'),
             'beta': ('ALBEVFCYODJWUGNMQTZSKPR', 'HIX'),
             'gamma': ('AFNIRLBSQWVXGUZDKMTPCOYJHE'),
             }
    _STEPS = {1: 17, 2: 5, 3: 22, 4: 10, 5: 0}

    def __init__(self, reflector, rotors, shifts):
        self.shifts = shifts  # [shift1, shift2, shift3]
        self.rotors = rotors
        self.reflector_type = reflector

        self.reverse = False

    def _forward_pass(self, symbol_in_work, rots_fwd, rots_back):
        self.reverse = False
        while rots_fwd:
            rot = rots_fwd.pop()
            rots_back.append(rot)
            symbol_in_work = self.rotor_move(symbol_in_work, rot)
        return self.reflector(symbol_in_work, self.reflector_type)

    def _backward_pass(self, symbol_in_work, rots_back):
        self.reverse = True
        while rots_back:
            symbol_in_work = self.rotor_move(symbol_in_work, rots_back.pop())
        return symbol_in_work

    def enigma_start(self, symbol):
        self.shifts[-1] += 1

        rots_fwd = [(self.rotors[0], self.shifts[0]), (self.rotors[1], self.shifts[1]),
                    (self.rotors[2], self.shifts[2])]
        rots_back = []

        symbol_in_work = self._forward_pass(symbol, rots_fwd, rots_back)
        symbol_in_work = self._backward_pass(symbol_in_work, rots_back)

        self.move_disks()

        return symbol_in_work

    def move_disks(self):
        for idx, (rot, val) in enumerate(zip(self.rotors[1:], self.shifts[1:]), start=1):
            if val == 26:
                self.shifts[idx] = 0
            if self._STEPS[rot] == val + 1:
                self.shifts[idx - 1] += 1
                if idx == 1:
                    self.shifts[idx] += 1

    def run_encode(self, text):
        try:
            return ''.join([self.enigma_start(symbol) for symbol in text.upper().replace(' ', '')])
        except ValueError as e:
            return e

    def rotor_move(self, symbol, n):
        if not n[0]:
            return symbol
        symbol = self.caesar(symbol, key=n[1])
        for alphabet in self._RDICT[n[0]]:
            if symbol in alphabet:
                index = alphabet.find(symbol)
                if index > -1:
                    dd = alphabet[(index + (1, -1)[self.reverse]) % len(alphabet)]
                    return self.caesar(dd, key=n[1] * -1)
        return ''

    def reflector(self, symbol, n):
        if n:
            return {(symbol in v): v for v in self._B_REFLECTOR}[True].replace(symbol, '') if symbol.isalpha() else ''
        return symbol

    def caesar(self, text, key, alphabet=ascii_uppercase):
        secret_word = ''
        for letter in text.upper():
            if letter in alphabet:
                secret_word += alphabet[(alphabet.find(letter) + key) % len(alphabet)]
        return secret_word


if __name__ == '__main__':
    enigma = EnigmaEngine(1, [1, 2, 1], [0, 0, 0])
    print(enigma.run_encode(text='AAAAA AAAAA'))
