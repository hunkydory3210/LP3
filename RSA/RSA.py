#!/usr/bin/env python
# coding: utf-8

# In[218]:


import random


# In[219]:


def is_prime_number(number):
    if number > 1:
        for i in range(2, number//2):
            if number%i == 0:
                return False
        return True
    else:
        return False


# In[220]:


def get_prime_number():
    while True:
        integer = random.getrandbits(10)
        #print(integer)
        if is_prime_number(integer):
            return integer


# In[221]:


# 269280, 3
def find_gcd(a, b):
    if a > b: 
        small = b 
    else: 
        small = a
    for i in range(1, small+1): 
        if((a % i == 0) and (b % i == 0)): 
            gcd = i 
              
    return gcd 


# In[222]:


def are_coprimes(a, b):
    if find_gcd(a, b) == 1:
        return True
    else:
        return False


# In[223]:


def get_coprime(phi, nth):
    count = 0
    coprime = 2
    while True:
        
        if are_coprimes(coprime, phi):
            count = count + 1
            if count == nth:
                return coprime
            else:
                coprime = coprime+1
        else:
            coprime = coprime+1


# In[224]:


def get_decryption_key(encryption_key, phi, nth):
    decryption_key = 0
    i = 1
    count = 0
    while True:
        decryption_key = ((phi * i) + 1) / encryption_key
        if decryption_key.is_integer():
            count += 1
            if count == nth:
                return decryption_key
            else:
                i += 1
        else:
            i = i + 1


# In[225]:


a = 0
b = 0
while a == b:
    a = get_prime_number()
    b = get_prime_number()

print(a, b)


# In[226]:


n = a*b
phi = (a-1)*(b-1)
phi


# In[227]:


encryption_key = get_coprime(phi, 1)
encryption_key


# In[228]:


decryption_key = int(get_decryption_key(encryption_key, phi, 1))
decryption_key


# In[229]:


def encrypt_message(message, encryption_key, n):
    return (message**encryption_key)%n
    


# In[230]:


def decrypt_message(cipher, d, n1):
    return (cipher**d)%n1


# In[231]:


encrypt_message(10, encryption_key, n)


# In[233]:


decrypt_message(100000, decryption_key, n)


# In[ ]:




