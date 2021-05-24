###
# 这是一个稍微复杂一些的加解密算法，这套算法将不再拥有确定的规则组，替换规则将基于所关联的密码生成，不提供密码将无法解密文本。
# 该算法安全性相对更高，但也需要更复杂的处理程序。
###
import random

def PasswordHandle(password):#将密码处理生成唯一的替换规则

    replaceTextGroup = {"0":[],"1":[]," ":[]}
    passwordGroup = []
    num = 0
    for i in password:
        num += 1

        addASCIINum = (len(password) * 3) - (num * 2)
        passwordGroup.append(chr(ord(i) + addASCIINum))
        addASCIINum = (len(password) * 4) - (num * 3)
        passwordGroup.append(chr(ord(i) + addASCIINum))

    passwordGroup = list(set(passwordGroup))
    passwordGroup.sort()

    num1 = 1
    for a in passwordGroup:
        if(num1 % 3 == 0):
            replaceTextGroup["0"].append(a)
        elif(num1 % 2 == 0):
            replaceTextGroup["1"].append(a)
        else:
            replaceTextGroup[" "].append(a)
        num1 += 1

    return replaceTextGroup

def Encryption(text,password):#加密函数
    handleText_bin = ' '.join([bin(ord(c)).replace('0b', '') for c in text])#将传入文本处理成二进制形式
    handleText_temp = ""

    replaceTextGroup = PasswordHandle(password)
    for i in handleText_bin:#将处理完的二进制文本以replaceTextGroup内设定规则进行替换
        handleText_temp += i.replace(i,random.sample(replaceTextGroup[i], 1)[0])

    return(handleText_temp)

def Decrypt(text,password):#解密函数

    replaceTextGroup = PasswordHandle(password)

    handleText_temp = ""
    for i in text:#将传入的密文逐一提取根据replaceTextGroup内设定规则进行替换
        
        if i in replaceTextGroup["0"]:
            handleText_temp += "0"
            continue
        if i in replaceTextGroup["1"]:
            handleText_temp += "1"
            continue
        if i in replaceTextGroup[" "]:
            handleText_temp += " "
            continue

    handleText_string = ''.join([chr(i) for i in [int(b, 2) for b in handleText_temp.split(' ')]])#将转换完毕的二进制文本还原
    return(handleText_string)

#以下是用来演示系统的代码
while True:
    if(input("请选择模式（加密1，解密2）：") == "1"):
        text = input("请输入加密文本:")
        password = input("请输入密码：")
        print(Encryption(text,password))
    else:
        text = input("请输入解密文本:")
        password = input("请输入密码：")
        print(Decrypt(text,password))
    


