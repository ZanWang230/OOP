# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:12:49 2024

@author: ASUS
"""
import random
class Dice:
    def __init__(self,nam):
        self.nam=nam
        self.rolls=[]
        self.record=[]
        self.result=0
    def throw_dices(self):
        for i in range(3):
            roll=random.randint(1,6)
            if roll in self.rolls:
                self.rolls.remove(roll)
            else:
                self.rolls.append(roll)
            self.record.append(roll)
        if len(self.rolls)!=3:
            self.result=self.rolls[0]
        else:
              self.result=0       
    def val(self):
        return self.result
    def name(self):
        return self.nam
    def __str__(self):
        return f'{self.nam} {self.record[0]} {self.record[1]} {self.record[2]} --> {self.result}'
a , b = Dice("小明") , Dice("小華")
# print(a.name())
while True :
    a.throw_dices()
    b.throw_dices()
    print(a, b, sep="\n", end="\n\n")
    if a.val() != b.val() : break
print( ( a.name() if a.val() > b.val() else b.name() ) + "贏" )