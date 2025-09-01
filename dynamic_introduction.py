import string
import time
import sys

text = f'Nice to meet you, I\'m Kunal'
temp = ""

for ch in text:
    for i in string.printable:  
        if i == ch:
            time.sleep(0.05)
            sys.stdout.write("\r" + temp + i)
            sys.stdout.flush()
            temp += ch
            break
        else:
            time.sleep(0.001)
            sys.stdout.write("\r" + temp + i)
            sys.stdout.flush()
