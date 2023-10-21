#Oilaga bo'lgan muhabbat
# erkak=False
# ayol=False

# print(erkak | ayol)
#if else elif(else if) barchasi BOOL ga qaratiladi

# x=int(input('x= '))
# # if(-3<=x and x<3):
# #   y=x*x
# # elif(x<-3):
# #   y=x*x+4*x
# # else:
# #   y=3-x
# # print(y)
# print('Musbat' if(x>0) else  'Manfiy'if(x<0) else '0 ga teng')
# print(x*x if(-3<=x and x<3) else x*x+4*x if(x<-3) else 3-x)

# weatherA = 'spring'
# weatherB = 'summer'
# weatherC = 'autumn'
# weatherD = 'winter'

# go=0
# year=2
# while(go<year):
#   print('%s %s %s %s'%(weatherA,weatherB, weatherC,weatherD))
#   go+=1


















#123 dan kichik juft sonlarni teskari tartibda chiqarish dasturi
# home = 123
# end = 0
# i=0
# print(home<end)
# while(home>end):
#   if(home%2==0):
#      print(home)
#      i+=1
#   home-=1
# print('Bunday sonlar',i)





#Ax^3 + Bx = 0 x-? Butun yechimini topamiz

A=int(input('A = '))
B=int(input('B = '))

for i in range(1,1000):
  if(A*i**3+B*i==0):
    print(i)
  # else: print('Topilmadi')











