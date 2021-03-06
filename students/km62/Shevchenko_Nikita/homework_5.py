#Задача №1 ------------------------------------------------------------------------
"""
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
Считайте четыре действительных числа и выведите результат работы этой функции.
"""


#input------------------------------------------------------------------
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
#main-------------------------------------------------------------------
import math
def distance(x1,y1,x2,y2):
    print(round((math.sqrt((x2-x1)**2 + (y2-y1)**2)),5))
#output-----------------------------------------------------------------
distance(x1,y1,x2,y2)

#-----------------------------------------------------------------------------------


#Задача №2--------------------------------------------------------------------------
"""
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя.
"""


#input------------------------------------------------------------------
x = float(input())
y = int(input())
#main-------------------------------------------------------------------
import math
def power(x,y):
    z = 1
    for i in range(abs(y)):
        z = z*x
    if(y>=0):
        print(z)
    else:
        print(1/z)
#output-----------------------------------------------------------------
power(x,y)

#----------------------------------------------------------------------------------


#Задача №3-------------------------------------------------------------------------
"""
Дано действительное положительное число a и целое неотрицательное число n.
Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(), а используя рекуррентное соотношение an=a⋅an-1.

Решение оформите в виде функции power(a, n).
"""


#input------------------------------------------------------------------
a = float(input())
n = int(input())
#main-------------------------------------------------------------------
def power(a,n):
    ans=1
    for i in range(n):
        ans=ans*a
    print(ans)
#output-----------------------------------------------------------------
power(a,n)

#-----------------------------------------------------------------------


#Задача №4--------------------------------------------------------------
"""
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
В этой задаче нельзя использовать циклы — используйте рекурсию.
"""


#input------------------------------------------------------------------
n = int(input())
#main-------------------------------------------------------------------
import math
def fib(n):
    koren = math.sqrt(5)
    sech = (koren + 1) / 2
    return int(sech ** n / koren + 0.5)
#output-----------------------------------------------------------------
print(fib(n))

#-----------------------------------------------------------------------------------
