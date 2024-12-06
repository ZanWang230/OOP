# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:11:58 2024

@author: ASUS
"""


class Score:
    def __init__(self,file_name):
        with open(file_name,'r',encoding='utf-8') as file:
            data=file.read()
            data=data.split('\n')
            datas={}
            for i in data:
                datas[i.split('     ')[0].strip()]=i.split('     ')[1].split('    ')
                if len(datas[i.split('     ')[0].strip()])!=3:
                    datas[i.split('     ')[0].strip()]=i.split('     ')[1].split('    ')+i.split('     ')[2].split('    ')
                if len(datas[i.split('     ')[0].strip()])!=3:
                    datas[i.split('     ')[0].strip()]=i.split('     ')[1].split('    ')+i.split('     ')[3].split('    ')
                total=0
                for i2 in datas[i.split('     ')[0].strip()]:
                    total+=eval(i2)
                datas[i.split('     ')[0].strip()].append(f'{total/3:.1f}')
        self.datas=datas
    def find_score_between(self,a,b):
        res=[]
        for i in self.datas:
            if eval(self.datas[i][3]) >= a and eval(self.datas[i][3]) <= b:
                res.append(i.split(' ')[1]+f': {self.datas[i][3].strip()} ({self.datas[i][0].strip()},{self.datas[i][1].strip()},{self.datas[i][2].strip()})')
        return res
    def get_records(self,res):
        self.sorted_res=[]
        for i in res:
            self.sorted_res.append(i.split(': ')[1].split(' ')[0])
        self.sorted_res.sort(reverse=True)
        whole_sorted_res=[]
        c=1
        for i in self.sorted_res:
            for i2 in res:
                if i == i2.split(': ')[1].split(' ')[0]:
                    whole_sorted_res.append(f'{c} {i2}')
                    c+=1
        print_res=''
        for i in whole_sorted_res:
            print_res+=i+'\n'    
        return print_res
score = Score("score.dat")
while True :
    a , b = [ int(x) for x in input("> ").split() ]
    # 取得平均成績在 [a,b] 間的所有名單
    names = score.find_score_between(a,b)
    # 列印名單的成績資料,且由高分到低分排列
    print( score.get_records( names ) )
                
                
                  