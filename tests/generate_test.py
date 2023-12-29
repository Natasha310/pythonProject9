import string
import random


class GenerateEmailPassword:

    @staticmethod
    def generate_email():
        letters2 = string.ascii_lowercase
        email_length2 = 8
        rand_string2 = [''.join(random.choice(letters2))]
        new_email = None
        for i in letters2:
            rand_string2.append(i)
            if email_length2 == len(rand_string2):
                break
            else:
                continue
        new_email = ''.join(rand_string2) + '@mail.ru'
        print(new_email)
    generate_email()

    @staticmethod
    def generate_pas():
        letters = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
        rand_string = [''.join(random.choice(letters))]
        password_length = 8
        new_pas = None
        for i in letters:
            rand_string.append(i)
            if password_length == len(rand_string):
                break
            else:
                continue
        new_pas = ''.join(rand_string)
        print(new_pas)
    generate_pas()
