# -*- coding: utf-8 -*-
"""vigenere.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GUN0RpN1y0x-TqKT4lzxwzdhVm-e-vq4
"""

x1 = 0

def poly(key,plain):
  plain=ord(plain)-96
  key=ord(key)-96
  temp=plain+key-1
  if temp>26:
    temp=temp-26
  temp=temp+96
  temp=chr(temp)
  return temp

plain_t = str(input("Enter the string : ")).lower()
key_input = input("Enter the key : ").lower()
cipher_t=[]
key=[]
temp=0
buffer=""

for i in plain_t:
  key.append(key_input[temp])
  temp=temp+1
  if temp==len(key_input):
    temp=0

plain_t=plain_t.split(" ")
pt="".join(plain_t)

for i in range(len(pt)):
  buffer=poly(pt[i],key[i])
  cipher_t.append(buffer)
print("".join(cipher_t))