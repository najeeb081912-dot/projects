import random
import os
import datetime as dt
import time

name = str(input("what's your name? "))
print("hello, ", name)
time.sleep(1) 
os.system("clear")
score = 0
attempts = 0

while True:
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    os.system("clear")
    num = int(random.randint(1,100 ))
    print("score",str(score))
    start = dt.datetime.now()
    guess = int(input("enter guess 1-100 "))
    while guess != num:
     if guess > num:
         print('to high')
     elif guess < num:
           print('to low')
     attempts += 1
     guess = int(input("enter guess 1-100 "))
    end = dt.datetime.now()
    os.system("clear")
    score += 1
    print("your right", end - start)
    print("score", score)
    print("attempts", attempts)
    time.sleep(1)
    awns = int(input("are you ready? "))
    attempts = 0
    while awns == 2:
        awns = int(input("are you ready? "))
    else:
        os.system("clear")

    
