# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:29:02 2024

@author: ASUS
"""
import random
class Random_Shuffle():
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def len(self):
        if type(self.start)==int and type(self.end)==int:
            return self.end-self.start+1
        elif type(self.start)==str and type(self.end)==str:
            return ord(self.end)-ord(self.start)+1
    def get(self):
        if type(self.start)==int and type(self.end)==int:
            x=random.randint(self.start,self.end)
            return x
        elif type(self.start)==str and type(self.end)==str:
            x=chr(random.randint(ord(self.start),ord(self.end)))
            return x
foo=Random_Shuffle(8,11)
bar=Random_Shuffle('a','e')
for i in range(4*foo.len()):
    print(foo.get(),end=' ')
print()
for i in range(2*bar.len()):
    print(bar.get(),end=' ')
print()


            
        
    