# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:55:29 2024

@author: ASUS
"""

class Toy_Car:
    def __init__(self,x,y,speed=2,direction=0):
        self.x=x
        self.y=y
        self.speed=speed
        self.direction=direction
    def drive(self,sec,turn):
        self.direction+=turn
        if self.direction >= 360:
            self.direction=self.direction-360
        if self.direction==0:
            self.x+=self.speed*sec
        elif self.direction==90:
            self.y+=self.speed*sec
        elif self.direction==180:
            self.x-=self.speed*sec
        elif self.direction==270:
            self.y-=self.speed*sec
    
    def forward(self,sec):
        if self.direction >= 360:
            self.direction=self.direction-360
        if self.direction==0:
            self.x+=self.speed*sec
        elif self.direction==90:
            self.y+=self.speed*sec
        elif self.direction==180:
            self.x-=self.speed*sec
        elif self.direction==270:
            self.y-=self.speed*sec
    def __str__(self):
        return f'車子位置 ({self.x:.1f}, {self.y:.1f}) 朝向{self.direction}度方向'
car = Toy_Car(0,1,speed=2,direction=0)
car.forward(10) # 行進 10 秒
print( car )
car.drive(5,90) # 左轉 90 後行進 5 秒
print( car )
car.drive(15,90) # 左轉 90 後行進 10 秒
print( car )
    
    