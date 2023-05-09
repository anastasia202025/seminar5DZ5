 #Посчитать факториал (произведение 1 до N) и треугольное число 
 #(сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def sum (a,b):
     if b==0:
        return a
     return sum(a,b-1)+1

n = int(input()) 
m = int(input()) 
print(sum(n,m))

def fact(number):
     if number == 1:
         return 1
     return fact(number-1)+ number      