# -*- coding: utf-8 -*-
"""Monoalphabetic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FnODQBRGKE_zUdxsKybK4Bj1vauVNirl
"""

import random
input_string = input("Enter the string : ")
cipher_text=[]
number=[]
lower_number=[]
low_case=[]
upr_case=[]
for i in range(200):
  temp1=random.randrange(0, 26, 1)
  if temp1 not in number:
    number.append(temp1)
for i in number:
  i=i+97
  low_case.append(chr(i))
for j in range(200):
  temp2=random.randrange(0,26,1)
  if temp2 not in lower_number:
    lower_number.append(temp2)
for i in lower_number:
  i=i+65
  upr_case.append(chr(i))
for i in(input_string):
  temp=ord(i)
  if temp > 96 and temp<123:
    temp=temp-97
    cipher_text.append(low_case[temp])
  elif temp>64 and temp<91:
    temp=temp-65
    cipher_text.append(upr_case[temp])
print(low_case)
print(upr_case)
print("".join(cipher_text))

