

print(int('55055', 9) + 1)



'''
#2
print('x y z w')
for x in range(2):
   for y in range(2):
      for z in range(2):
         for w in range(2):
            if (not(y<=x) or (z<=w) or not(z))==False:
               print(x, y, z, w)


from itertools import product
print('x y z w')
nums=product('01',repeat=4)
for i in nums:
    x,y,z,w=i[0],i[1],i[2],i[3]
    if (not(y<=x) or (z<=w) or not(z))==False:
        print(x, y, z, w)
''',
'''
for i in range(1,100):
    num=(bin(i)[2:])
    if num.count('1')%2==0:
        chislo='10'+num[2:]+'0'

    if num.count('1')%2!=0:
        chislo='11'+num[2:]+'1'
    if int(chislo,2)>40:
        print (i, int(chislo,2))
        break
''', 
'''
#6
from turtle import *
left(90)
for i in range(7):
    forward(300)
    right(120)
pu()
for x in range(1,9):
    for y in range(1,10):
        goto(x*30,y*30)
        dot(2)
done()
''',
'''
#8
count=0
for a in range (1,8):
    for b in range (8):
        for c in range (8):
            for d in range (8):
                for e in range (8):
                    s=str(a)+str(b)+str(c)+str(d)+str(e)
                    if s.count('6')==1:
                        if s.index('6')==len(s)-1 and int(s[len(s)-2])%2==0:
                            count+=1
                        if s.index('6')==0 and int(s[1])%2==0:
                            count+=1
                        if s.index('6')<len(s)-1 and s.index('6')>0 and int(s[s.index('6')-1])%2==0 and int(s[s.index('6')+1])%2==0:
                            count+=1
print(count)


#8(2)
from itertools import product
k=0
n='16 36 56 76 61 63 65 67'
nn=n.split()
nums=product('01234567',repeat=5)
for n in nums:
    numb=''.join(n)
    if numb.count('6')==1 and numb[0]!='0':
        if all(not(x in numb) for x in nn):
            k+=1
print(k)
''',
'''
# загрузка текста из txt
text=t.split(";")
#result = [int(item) for item in text]
result = list(map(int, text))
x=0
y=x+6
counter=double_num=0

while True:
   n=0
   res6=result[x:y]
   for element in res6:
      if res6.count(element)>2:
         for yy in range(res6.count(element)): res6.remove(element) 
         # удаление значений больше 2 штук
      if res6.count(element)==2:
         n+=2   
         double_num=element 
         res6.remove(element)
         res6.remove(element)

   if n==2 and len(res6)==4:  
      if (sum(res6)/len(res6))<=(double_num*2): counter+=1

   print(counter)
   if y>=len(result):break         
   x=x+6
   y=x+6
''',
'''
spisok=[]
for num in range(2,1000):
    if all(num%delit!=0 for delit in range(2,num)):
        spisok.append(num)
        
for y in range (100):
    if y*4+117 in spisok:
        print(y)
        break
''',
'''
#14
alph='0123456789abcde'
for x in alph:
    f=int(f'123{x}5',15)+int(f'1{x}233',15)
    if  f%14 ==0:
        print(x,f//14)
        break
''',
'''
#15
for a in range(1,100):
    if all(((x%2==0) <= (x%3!=0)) or (x+a>=100) for x in range(1,1000)):
        print(a)
        break
''',
'''
#16
itog1=itog2=1
for x1 in range(1,2024):
    itog1=itog1*x1
for x2 in range(1,2021):
    itog2=itog2*x2
print(itog1/itog2)
''',
'''
#17
with open('17.txt') as f:
    nums=[int(x) for x in f]
    maxi=[]
    s=[]
   
    for i in range(len(nums)):
      if nums[i]%10==3:
         maxi.append(nums[i])
    maximum=0
    for i in range(len(nums)-1):
        a=abs(nums[i])%10
        b=abs(nums[i+1])%10
        if ((a==3) and (b!=3)) or ((a!=3) and (b==3)):
        if (nums[i]**2+nums[i+1]**2) >= max(maxi)**2: 
            s.append(nums[i]+nums[i+1])
            if nums[i]**2+nums[i+1]**2>maximum:
                maximum=nums[i]**2+nums[i+1]**2
print(len(s), maximum)
''',
'''
#23
from itertools import product
def f23(x,y,z):
    count=0
    for i in range(1,z):
        nums=product('12',repeat=i)
        for numb in nums:
            #numb=''.join(n)
            a=x
            if x==10 and numb.count('2')>1:continue
            for ii in numb:
                if a==17: break 
                if ii=='1':a+=1
                elif ii=='2' :a*=2

            if a==y: count+=1
    return count
                
print(f23(1,10,10)*f23(10,35,25))
''',
'''
#24
with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('D','S').replace('F','S')
    s=s.replace('A','G').replace('O','G')
    s=s.replace('SG','*')
    k=kmax=0
    for i in s:
        if i=='*'
            k+=1
            kmax=max(k,kmax)
        else:k=0
print(kmax)
''',
'''
#25
for i in range(2023,10**10,2023):
    num=str(i)
    if num[0]=='1' and num[2:6]=='2139' and num[-1]=='4':
        print(i,i//2023)
''',
'''
#26
with open('26.txt') as f:
    s=[int(x) for x in f]
    s=sorted(s[1:],reverse=True)
    k,mini=1,s[0]

    for i in range(1,len(s)):
        if s[i]+3<=mini:
            mini=s[i]
            k+=1
print(k,mini)
''',
'''
None
'''


















