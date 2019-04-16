#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


def is_prime_number(number):
    if number > 1:
        for i in range(2, number//2):
            if number%i == 0:
                return False
        return True
    else:
        return False


# In[3]:


def get_prime_number():
    while True:
        integer = random.getrandbits(10)
        #print(integer)
        if is_prime_number(integer):
            return integer


# In[9]:


def get_large_number():
    p=random.getrandbits(10)
    return p


# In[11]:


p=get_prime_number()
q=get_prime_number()


# In[15]:


class device:
    def generate_private_key(self):
        self.private_key = get_large_number()
    def value_to_be_sent(self):
        return (q**self.private_key) % p
    def get_common_key(self, value_received):
        return (value_received ** self.private_key) % p


# In[16]:


alice = device()
alice.generate_private_key()
value_to_be_sent_to_bob = alice.value_to_be_sent()


# In[18]:


bob = device()
bob.generate_private_key()
value_to_be_sent_to_alice = bob.value_to_be_sent()


# In[19]:


value_received_by_bob = value_to_be_sent_to_bob
value_received_by_alcie = value_to_be_sent_to_alice


# In[21]:


alice.get_common_key(value_received_by_alcie)


# In[22]:


bob.get_common_key(value_received_by_bob)


# In[ ]:




