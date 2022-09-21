import random


class DatabusUtilities:

    @staticmethod
    def get_license_plate():
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s_chars = 'abcdefghijklmnopqrstvuwxyz'
        nums = '0123456789'
        alpha = ""
        for i in range(3):
            alpha += random.choice(chars)
        for i in range(3):
            alpha += random.choice(nums)
        for i in range(3):
            alpha += random.choice(s_chars)
        return alpha