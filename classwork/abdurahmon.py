# 1/4 =================================================

lst =['AA', 'aa', 'bb' , 'BB', 'CC', 'cc']
while True:
    what = int(input('Что вы хотите сделать : \n1)Добавить \n2)Посмотреть \n3)Удалить \n4)Очистить плейлист : (1/2/3/4) :'))
    if what == 1:
        musicUser = input('Введите свои любимые песни : ')
        lst.append(musicUser)
        print(f'===================================\n{musicUser} Добавлено список ваших песен \nВаш список {lst}\n=====================================')
    elif what == 2:
        print(f'===================================\nСписок ваших песех {lst}\n=====================================')
    elif what == 3:
        delet = input(f'Введите название музыки которую хотите удалить :')
        if delet in lst:
            lst.remove(delet)
            print(f'===================================\nМузыка {delet} Удалено \nСписок Ваших песен {lst}\n=====================================')
        else:
            print('===================================\nУ вас нету таких песен\n=====================================')
    elif what == 4:
        lst.clear()
        print(f'Список пуст {lst}')


# 2 =====================================================================
# print(set([i.lower() for i in lst]))


# 3 ===================================================================== 
# for i in enumerate(lst):
#     print(i)


# 5 =====================================================================
# def num(x): 
#       print(str(x) if type(x) == int or type(x) == float else "Принимаю только числа")

# 6 =====================================================================

# sp = {
#     0:'zero',
#     1:'one',
#     2:'two',
#     3:'three',
#     4:'four',
#     5:'five',
#     6:'six',
#     7:'seven',
#     8:'eight',
#     9:'nine',
# }
# lst=[]
# def number(a):
#     s = list(str(a))
#     for i in s:
#         if int(i) in sp:
#             lst.append(sp[int(i)])
# number(731)
# print('.'.join(lst)+'!')


# 7 =====================================================================
# sp = [i for i in range(10)]
# print(sp[::-1])

# 8 =====================================================================
# print(set(["a", "b", "a", "c", "c"]))

# 9 =====================================================================
# x = lambda a : a*2
# print(x(2))

# 10 =====================================================================
# f = lambda a,b: a+b
# print(f(2,3))


#11 ===================================================================== 
# from helloWorld import hello
# hello()
        
#12 =====================================================================
# def fact(x):  3 628 800
#     a = 1
#     while x > 1:
#         a *= x
#         x -= 1
#     print(a)
# fact(3)

#13 =====================================================================
# year = int(input('Год :'))
# print("Високосный" if year  % 4 == 0 and year % 100 != 0  or year % 400 == 0 else "невисокосный")


#14 =====================================================================
# def show_stars (rows):
#     if rows == 5:
#         for i in range(rows+1):
#             x ='*'
#             print(i*x)
#     else:
#         print('error')
    
# show_stars(5)

#15 =====================================================================
# def fizz_buzz(x):
#     if x % 3 == 0 and x % 5 ==0:
#         print('FizzBuzz')
#     elif x % 3 == 0:
#         print('Fizz')
#     elif x % 5 ==0 :
#         print('Buzz')
#     else:
#         print(x)

# fizz_buzz(32)

#16 =====================================================================
# def square(s):
#     print(tuple([s*s,s*4]))

# square(5)

# #17 =====================================================================


#18 =====================================================================

# n = 0
# while True:
#     try:
#         num = input("Введите число : ").split(' ')
#         for i in num:
#             a = int(i)
#             if isinstance(a, int):
#                 n+=a
#         print(n)
#     except ValueError:
#         print('error')
#         exit()

#19 ===================================================================== 

# num = input('Введите число : ')
# print(True if num == num[::-1] else False)

#20 =====================================================================

# def fact(x):
#     a = 1
#     while x > 1:
#         a *= x
#         x -= 1
 
#     print(a)
# fact(4)    



"""
Ответ:

def is_prime(n):

   if n < 2:

       return False

   if n == 2:

       return True

   limit = n**(1/2)

   i = 2

   while i <= limit:

       if n % i == 0:

           return False

       i += 1

   return True
"""
