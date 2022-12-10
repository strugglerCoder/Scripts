import math
import random

digit = "0123456789"
otp = ""

for i in range(6):
    otp += digit[math.floor(random.random()*10)]

print(otp)
