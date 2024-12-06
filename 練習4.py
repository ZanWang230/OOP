# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:59:55 2024

@author: ASUS
"""

class Bucket:
    def __init__(self,full,name=1,fill=False,water_level=0):
        if water_level==0 and fill==False:
            self.water_level=0
        elif fill:
            self.water_level=full
        else:
            self.water_level=water_level
        self.full=full
        self.name=name
        
        
    def __rshift__(self,other):
        if self.water_level>=other.full-other.water_level:
            self.water_level-=(other.full-other.water_level)
            other.water_level=other.full
            self.fill=False
        else:
            other.water_level+=self.water_level
            self.water_level=0
            self.fill=False
        return self
    def __lshift__(self,other):
       if other.water_level>=self.full-self.water_level:
           other.water_level-=(self.full-self.water_level)
           self.water_level=self.full
       else:
           self.water_level+=other.water_level
           other.water_level=0
       return self
    def __str__(self):
       return f'{self.name}:{self.water_level}/{self.full}'
a=Bucket(5,'a')
b=Bucket(3,'b')
c=Bucket(100,'c')
f=Bucket(100,'f',fill=True)
f>>a>>b
print(a,b,c,f,sep=" , ")
a>>(b>>c)
print(a,b,c,f,sep=" , ")
a>>(b>>c)
print(a,b,c,f,sep=" , ")
(a<<f)>>b
print(a,b,c,f,sep=" , ")

            
        
        