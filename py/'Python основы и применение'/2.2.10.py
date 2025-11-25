# Алиса владеет интересной информацией, которую хочет заполучить Боб.
# Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
# У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.
#
# Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой
# из паролей ему нужен. Помогите ему решить эту проблему.
#
# Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
# Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.
#
# Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать,
# какой из паролей служит ключом для расшифровки файла с интересной информацией.
#
# Ответом для данной задачи служит расшифрованная интересная информация Алисы.
#
#Файл с информацией: https://stepik.org/media/attachments/lesson/24466/encrypted.bin
#Файл с паролями: https://stepik.org/media/attachments/lesson/24466/passwords.txt

import time
import simplecrypt
from simplecrypt import decrypt

start_time = time.time()
with open('encrypted.bin', "rb") as inp:  # read encrypted data
    encrypted = inp.read()
    with open('passwords.txt') as inp_pass:  # read passwords
        password = inp_pass.read().split()
        for item in password:
            try:  # try to decrypt data
                answer = decrypt(item, encrypted).decode('utf-8')
            except simplecrypt.DecryptionException:  # if it's not succeed then skip it
                continue
with open('answer.txt', 'w') as out_inf:
    out_inf.write(answer)
print('Time: %s seconds' % (time.time()-start_time))

