#!/usr/bin/python
# coding=utf-8

# dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
#
#
# print "dict:" ,dict
# print dict.items()
#
# print "字典值 : %s" % dict.items()
#
# # 遍历字典列表
# for key, values in dict.items():
#     print key,'|' ,values


# from bs4 import BeautifulSoup
# import urllib
#
# html = urllib.request.urlopen("http://www.baidu.com")
# bs_obj = BeautifulSoup(html, 'html.parser',from_encoding='utf-8')
# print("title tag: ", bs_obj.text)


# phone_number = '1386-666-0006'
# hiding_number = phone_number.replace(phone_number[:9],'*' * 9)
# print(hiding_number)

# search = '168'
# num_a = '1386-168-0006'
# num_b = '1681-222-0006'
#
# print num_b.find(search)


# print('{} a word she can get what she {} for.'.format('With','came'))
# print('{preposition} a word she can get what she {verb} for'.format(preposition = 'With',verb = 'came'))
# print('{0} a word she can get what she {1} for.'.format('With','came'))



# print('{} for mac'.format('numpy'))


# city = input("write down the name of city:")
# url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
# print url

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
#
# listsrt = list(enumerate(seasons))
# for no,li in listsrt:
#     print no,li
#
# x = [1,2,3]
# y = [4,5,6]
# ziplist = zip(x,y)
# print ziplist
# print list(ziplist)
#
# x2,y2 = zip(*ziplist)
# print x2,y2


# squares = []
# for i in range(10):
#     squares.append(i**2)
#
# for a in squares:
#     print a
#
# squares = [x**2 for x in range(10)]
# print squares

# print {a:a*2 for a in range(10)}
#
# print type({a:a*2 for a in range(10)})

# dicts = {a:a*2 for a in range(10)}
# print dicts
# for x,y in dicts.items():
#     print x,y

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
#
# for i in sorted(set(basket)):
#     print i


# x = int(input("Please enter an integer: "))
# if x < 0 :
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print ('Single')
# else:
#     print ('More')


# for i in range(1,10):
#     for j in range(1,10):
#         print ('{} * {} = {}'.format(i,j,i*j))


# print [(i,j,i*j) for i in range(1,10) for j in range(1,10)]


class CocaCola():
    formula = ['caffeine','sugar','water','soda']
    def __init__(self):
        self.local_logo = '可口可乐'
    def drink(self):
        print('Energy!')
coke = CocaCola()
print (coke.local_logo)