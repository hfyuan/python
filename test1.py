import time
from time import strftime, strptime

'''
t2 = strptime("12/02/2016", "%d/%m/%Y")
print(t2)

print(strftime("%d %b %y", t2))

t1 = strftime("%Y-%m-%d", time.localtime())
print(t1)
'''
def checkpswd(pswd):
    #check the length of pswd > 6
    print("the input of pswd is :" + pswd)
    print("the lenght is :%d " %len(pswd))
    if len(pswd) <= 6:
        print("the length of the pswd must  > 6")
        return False
    
    #chech the first is alpha
    firstchar = str(pswd[0])
    if False == firstchar.isalpha():
        print("the pswd must beginning by alpha!")
        return False
    #check contain one of character :"_" "*" "#"
    if "_" in pswd:
        return True
    elif "*" in pswd:
        return True
    elif "#" in pswd:
        return True
    else:
        print( " the pswd must contain the character of _ * #")
        return False
    
def checkusername(name):
    #check first char is alpha
    firstchar = str(name[0])
    if firstchar.isalpha():
        return True
    else:
        return False

print('time is ' + strftime("%Y-%m-%d", time.localtime()))
print("please entre your name:")
theinputtxt = str(input())
while False == checkusername(theinputtxt):
    print("the first char must be alpha! pls entre again:")
    theinputtxt = str(input())
else:
    print("your name is :" + theinputtxt)



print("please entre your password:")
yourpw = str(input())

while False == checkpswd(yourpw):
    #print("the first char must be alpha! pls entre again:")
    yourpw = str(input())
else:
    print("your name is :" + yourpw)

    

print("Concratuation " + theinputtxt + " yourpswdis : "+  yourpw)
