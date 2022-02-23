import requests
import random
import os


def otp_gen():
    num = 9903010323
    requests.post(os.environ['BLOWERIO_URL'] + '/messages',
                  data={'to': '+919903010323', 'message': 'Hello from Blower.io'})


if __name__ == "__main__":
    otp_gen()
