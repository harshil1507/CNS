# -*- coding: utf-8 -*-
"""hill.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EO7pHNgWfSJ11yumq4EyLszGN2V1aI_T
"""

import numpy as np
import random
input_string = input("Enter the string : ").lower()
plaintext=[]
cipher_text=[]
rand=[]
for i in range(10):
  temp1=random.randrange(1, 100, 1)
  if temp1 not in rand:
    rand.append(temp1)
for i in (input_string):
  temp=ord(i)
  temp=temp-97
  plaintext.append(temp)
plain_t=np.array(plaintext)

print(rand)
a=np.array([[1+rand[1],2+rand[2],3+rand[3]], [4+rand[4],5+rand[5],6+rand[6]], [7+rand[7],8+rand[8],9+rand[9]]])
c= a.dot(plain_t)
print(c)

cipher_text

c=c.tolist()
print(c)
for i in c:
  i=i%26
  i=i+96
  cipher_text.append(chr(i))
print(cipher_text)

