import numbers
import string
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha
from random import choice

numbers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def get_random_string(length=int):
    str = ''
    for i in range(length):
        str += choice(numbers)
    return str

def get_captcha_image(length=int):
    image = ImageCaptcha(546, 144, fonts=['\assets\fonts\OpenSans-Regular.ttf'])
    s = get_random_string(length)
    image.write(s, 'out.jpg')
    return s
    # print(s)
    # return image.generate(s)
    # data = image.generate(s)
