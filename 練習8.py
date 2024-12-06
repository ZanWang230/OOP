# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 01:27:33 2024

@author: ASUS
"""
import random
class SSP:
    def __init__(self,players):
        self.players=list(players)
    def play(self):
        bets=['剪刀','石頭','布']
        players_bet=[]
        self.bet_str=''
        self.player_str=''
        for n,i in enumerate(self.players):
            players_bet.append(bets[random.randint(0,2)])
            self.bet_str+=f'{players_bet[n]:<3}'
            self.player_str+=f'{i:<3}'
        result=set(players_bet)
        if len(result)==2:
            if bets[0] in players_bet and bets[2] in players_bet:
                while True:
                    del self.players[players_bet.index(bets[2])]
                    del players_bet[players_bet.index(bets[2])]
                    if bets[2] not in players_bet:
                        self.winning_bet= bets[0]
   
                        break
            if bets[1] in players_bet and bets[0] in players_bet:
                while True:
                    del self.players[players_bet.index(bets[0])]
                    del players_bet[players_bet.index(bets[0])]
                    if bets[0] not in players_bet:
                        self.winning_bet= bets[1]

                        break
            if bets[2] in players_bet and bets[1] in players_bet:
                while True:
                    del self.players[players_bet.index(bets[1])]
                    del players_bet[players_bet.index(bets[1])]
                    if bets[1] not in players_bet:
                        self.winning_bet= bets[2]
                        break
        else:
            self.winning_bet='沒勝負'
    def over(self):
        if len(self.players)==1:
            return True
        return False
    def winner(self):
        if len(self.players)==1:
            return self.players[0]
        return None
    def __str__(self):
        return f'{self.player_str}\n{self.bet_str}\n-->{self.winning_bet}'
players = ( "小華", "小明", "小民", "花花", "阿杰" )
game = SSP(players)
while True :
    game.play() # 出拳
    print( game ) # 印出結果
    if game.over() : break
print( game.winner() )
        