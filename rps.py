import time 
import os
import datetime as dt
import random
x = 0
score = 0
while x == 0:
    gennum = int(random.randrange(1, 4))
    r = 1
    p = 2
    s = 3
    awns = int(input("r1 p2 s3 "))
    if awns == r and gennum == s:
        os.system("clear")
        print("you win rock x scissors")
        score += 1
        print(score) 
    if awns == s and gennum == p:
        os.system("clear")
        print("you win scissors x paper")
        score += 1
        print(score) 
    if awns == p and gennum == r:
        os.system("clear")
        print("you win paper x rock")
        score += 1
        print(score) 

    if awns == s and gennum == r:
        os.system("clear")
        print("you lose scissors x rock")
        print(score)
    if awns == p and gennum == s:
        os.system("clear")
        print("you lose paper x scissors")
        print(score)
    if awns == r and gennum == p:
        os.system("clear")
        print("you lose rock x paper")
        print(score)
    
    if awns == gennum:
        os.system("clear")
        print("tie")
        print(score) 
   


