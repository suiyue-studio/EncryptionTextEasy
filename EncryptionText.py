###
# 这是一个简单加解密算法，将直接将文本处理成加密文本，无法关联密码，整体加密安全性不及基于密码的加密算法。
# 但该算法加密速度更快，可以极短时间完成加密。
###
import random

replaceTextGroup = {"0":["a","b","c","d"],"1":["e","f","g","h"],"2":["i","j","k","l"]," ":["m","n","o","p"]}#加解密所用规则组

def Encryption(text):#加密函数
    handleText_bin = ' '.join([bin(ord(c)).replace('0b', '') for c in text])#将传入文本处理成二进制形式
    handleText_temp = ""

    for i in handleText_bin:#将处理完的二进制文本以replaceTextGroup内设定规则进行替换
        handleText_temp += i.replace(i,random.sample(replaceTextGroup[i], 1)[0])

    return(handleText_temp)

def Decrypt(text):#解密函数

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
        print(Encryption(text))
    else:
        text = input("请输入解密文本:")
        print(Decrypt(text))