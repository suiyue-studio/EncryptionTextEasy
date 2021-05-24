# EncryptionText & EncryptionText.key 文本加密算法
两个简单的文本加密算法，可以对字符串进行简单的加密，提供两种算法

接下来将简单介绍两个算法文件

# 1.EncryptionText.py
## 替换规则
### 简介
EncryptionText.py是一个简单的文本加密算法，该算法将传入的文本转换为二进制文本串，EncryptionText.py中预置了一个替换规则，此规则说明了二进制文本串中的‘0’‘1’‘ ’三种字符的替换规则***replaceTextGroup***，此规则是一个**dict**变量。

EncryptionText.py中的函数‘Encryption’会根据规则将二进制文本串中的‘0’‘1’‘ ’三种字符替换为规则中对应的字符。你可以自由修改、添加、删减规则中的字符。
### 修改规则组
EncryptionText.py 的原始规则组：**replaceTextGroup = {"0":["a","b","c","d"],"1":["e","f","g","h"]" ":["m","n","o","p"]}**

你可以将‘0’‘1’‘ ’三种字符对应的**list**修改来实现修改规则组，你可以添加、删除或者修改，如同下面的操作：

**replaceTextGroup = {"0":["a","b","c"],"1":["e","f","g","h","q"]," ":["m","o","p"]}**

“0”和“ ”所删除的字符不会出现在加密后的文本中

“1”中添加到字符“q”将出现在加密后的文本中
 
