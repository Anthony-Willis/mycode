#!/usr/bin/env python3
""" This is a mini quiz project to practice if then logic in python """
#Write it in a notebook first to separate 
#Chadly-won kenobi, here is my attempt at fizzbuzz for the if/elif practice. The Ninja turtle quiz was lost, but you would have been Master Splinter.
  """Write a program which begins by assigning a value to an integer N
If N is divisible by 3 but not 5, print "Fizz"
If N is divisible by 5 but not 3, print "Buzz"
If N is divisible by both, print "FizzBuzz"
If N is divisible by neither, print "Shucks" """

#Improvements that could be made. DRY principle, Write a for loop that goes through different values of n. Run code inside of Main

n = 9
if n % 3== 0 and not (n % 5== 0):
 print("Fizz")
 
elif n % 5== 0 and not (n % 3== 0):
 print("Buzz")
elif n % 5== 0 and (n % 3== 0):
 print("FizzBuzz")
#elif not n % 3==0 and not n % 5== 0:
 # print("shucks") below else statement is cleaner than elif
else:
 print("Shucks")


n = 10
if n % 3== 0 and not (n % 5== 0):
 print("Fizz")

elif n % 5== 0 and not (n % 3== 0):
 print("Buzz")
elif n % 5== 0 and (n % 3== 0):
 print("FizzBuzz")
#elif not n % 3==0 and not n % 5== 0:
 # print("shucks") below else statement is cleaner than elif
else:
 print("Shucks")

n = 15
if n % 3== 0 and not (n % 5== 0):
 print("Fizz")
 
elif n % 5== 0 and not (n % 3== 0):
 print("Buzz")
elif n % 5== 0 and (n % 3== 0):
 print("FizzBuzz")
#elif not n % 3==0 and not n % 5== 0:
 # print("shucks") below else statement is cleaner than elif
else:
 print("Shucks")

n = 14
if n % 3== 0 and not (n % 5== 0):
 print("Fizz")

elif n % 5== 0 and not (n % 3== 0):
 print("Buzz")
elif n % 5== 0 and (n % 3== 0):
 print("FizzBuzz")
#elif not n % 3==0 and not n % 5== 0:
 # print("shucks") below else statement is cleaner than elif
else:
 print("Shucks")
