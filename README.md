# TaskCompilation
Plan: a collection of different tasks for encrypting / constructing artificial languages. Later merge into one global related project
> Globally: everything here is the forerunner for the artificial language generator Ro

---
## Caesar Encryptor
Цель: Необходимо написать программу, шифрующее слово с помощью [Шифра Цезаря](https://is.gd/rcGAsp).
Программа должна принимать на вход от пользователя слово и число сдвигов. 

Example:  
- Encoding
~~~
Слово:         скиллбокс  
Число сдвигов: 3  
Вывод:         фнлоодснф
~~~
~~~
main_enc.py цезарь скиллбокс 3 [-m enc -a ru]
~~~
- decoding
~~~
Слово:         фнлоодснф  
Число сдвигов: 3  
Вывод:         скиллбокс
~~~
~~~
main_enc.py цезарь скиллбокс 3 -m dec [-a ru]
~~~

## Vijener Encryptor
Цель: Необходимо написать программу, шифрующее слово с помощью [Шифра Виженера](https://is.gd/WEVeME).
Программа должна принимать на вход от пользователя слово и слово-ключ.

Example:  
- Encoding
~~~
Слово:         скиллбокс  
Слово-ключ:    привет  
Вывод:         быснруюыъ
~~~
~~~
main_enc.py виженер скиллбокс привет [-m enc -a ru]
~~~
- decoding
~~~
Слово:         быснруюыъ  
Число сдвигов: привет  
Вывод:         скиллбокс
~~~
~~~
main_enc.py виженер быснруюыъ привет -m dec [-a ru]
~~~