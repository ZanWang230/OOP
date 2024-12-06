# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:02:50 2024

@author: ASUS
"""
import re
class Longtitude:
    def __init__(self,foo):
        self.foo=foo
    def shift(self,n):
        self.n=n
        pattern=re.compile('\d+[e,w]\d+')
        if pattern.match(self.foo):
            if 'e' in self.foo:
                if int(self.foo.split('e')[0])+n==180 and int(self.foo.split('e')[1])==0:
                    return '180e0'
                elif int(self.foo.split('e')[0])+n>=180 and int(self.foo.split('e')[1])>0:
                    return str(180-((int(foo.split('e')[0])+n+1)-180))+'w'+str(60-int(foo.split('e')[1]))
                elif int(self.foo.split('e')[0])+n>=0:
                    return str(int(self.foo.split('e')[0])+n)+'e'+self.foo.split('e')[1]
                else:
                    return str(abs(int(self.foo.split('e')[0])+n)-1)+'w'+str(60-int(self.foo.split('e')[1]))
            else:
                n=-n
                if int(self.foo.split('w')[0])+n==180 and int(self.foo.split('w')[1])==0:
                    return '180e0'
                elif int(self.foo.split('w')[0])+n>=180 and int(self.foo.split('w')[1])>0:
                    return str(180-((int(self.foo.split('w')[0])+n+1)-180))+'w'+str(60-int(self.foo.split('w')[1]))
                elif int(self.foo.split('w')[0])+n>=0:
                    return str(int(self.foo.split('w')[0])+n)+'w'+self.foo.split('w')[1]
                else:
                    return str(abs(int(self.foo.split('w')[0])+n)-1)+'e'+str(60-int(self.foo.split('w')[1]))
        else:
            return self.wrong_spell()
    def wrong_spell(self):
        self.foo=input('re-enter again')
        return self.shift(self.n)
while True :
    foo = input("> ")
    bar = Longtitude(foo)
    for i in range(-2,3) :
        print( bar.shift(i*10) , end=" " )
    print("\n")
