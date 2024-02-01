i#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
     """
    data: list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    num_leading_one = 0

    for byte in data:
        if num_leading_one > 0:
            if (byte >> 6) != 0b10:
                return False
            num_leading_one -= 1
        else:
            while (byte >> (7 - num_leading_one)) & 1 == 1:
                num_leading_one += 1

            if num_leading_one == 1 or num_leading_one > 4:
                return False
    return num_leading_one == 0
