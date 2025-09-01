import string
import time

text = f'Nice to meet you, I\'m Kunal'
temp = ""

for ch in text:
    for i in string.printable:
        if i == ch: 
            time.sleep(0.05)
            print(temp + i)
            temp += ch
            break
        else:
            time.sleep(0.001)
            print(temp + i)
