##String Type

<https://blog.ansheng.me/article/python-full-stack-way-string-data-type/>

###字符串方法

`center(self, width, fillchar=None):` 
内容居中，width：字符串的总宽度；fillchar：填充字符，默认填充字符为空格。

`count(self, sub, start=None, end=None):`
统计字符串里某个字符出现的次数,可选参数为在字符串搜索的开始与结束位置。

`decode(self, encoding=None, errors=None):`
解码

```
# 定义一个变量内容为中文
temp = "中文"
# 把变量的字符集转化为UTF-8
temp_unicode = temp.decode("utf-8")
```

`encode(self, encoding=None, errors=None):`
编码，针对unicode

```
# 定义一个变量内容为中文,字符集为UTF-8
temp = u"中文"
# 编码，需要指定要转换成什么编码
temp_gbk = temp_unicode.encode("gbk")
```

`endswith(self, suffix, start=None, end=None):`
判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。

`expandtabs(self, tabsize=None):`
把字符串中的tab符号(‘\t’)转为空格，tab符号(‘\t’)默认的空格数是8。

`find(self, sub, start=None, end=None):`
检测字符串中是否包含子字符串str，如果指定beg(开始)和end(结束)范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。

`format(args, *kwargs):`
字符串格式

`index(self, sub, start=None, end=None):`
检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。

`isalnum(self):`
检测字符串是否由字母和数字组成，如果string至少有一个字符并且所有字符都是字母或数字则返回True,否则返回False

`isalpha(self):`
检测字符串是否只由字母组成。

`isdigit(self):`
检测字符串是否只由数字组成

`islower(self):`
检测字符串是否由小写字母组成

`isspace(self):`
检测字符串是否只由空格组成

`istitle(self):`
检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。

`isupper(self):`
检测字符串中所有的字母是否都为大写。

`join(self, iterable):`
将序列中的元素以指定的字符连接生成一个新的字符串。

`ljust(self, width, fillchar=None):`
返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。

`lower(self):`
转换字符串中所有大写字符为小写。

`lstrip(self, chars=None):`
截掉字符串左边的空格或指定字符

`partition(self, sep):`
用来根据指定的分隔符将字符串进行分割，如果字符串包含指定的分隔符，则返回一个3元的tuple，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。

`replace(self, old, new, count=None):`
把字符串中的 old(旧字符串)替换成new(新字符串)，如果指定第三个参数max，则替换不超过max次

`rfind(self, sub, start=None, end=None):`
返回字符串最后一次出现的位置，如果没有匹配项则返回-1。

`rindex(self, sub, start=None, end=None):`
返回子字符串str在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间。

`rsplit(self, sep=None, maxsplit=None):`
从右到左通过指定分隔符对字符串进行切片,如果参数num有指定值，则仅分隔num个子字符串

`rstrip(self, chars=None):`
删除string字符串末尾的指定字符（默认为空格）。

`splitlines(self, keepends=False):`
按照行分隔，返回一个包含各行作为元素的列表，如果num指定则仅切片num个行。

`startswith(self, prefix, start=None, end=None):`
检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。

`strip(self, chars=None):`
移除字符串头尾指定的字符（默认为空格）。

`swapcase(self):`
用于对字符串的大小写字母进行转换，大写变小写，小写变大写。

`title(self):`
返回”标题化”的字符串,就是说所有单词都是以大写开始，其余字母均为小写。

`translate(self, table, deletechars=None):`
根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到 del 参数中。


####str类型和bytes类型转换

以UTF-8编码的时候，一个汉字是三个字节，一个字节是八位。

```
#3.5.x实例
var = "中文"
for n in var:
    print(n)
--------------
中
文
--------------

#2.7.x实例
var = "中文"
for n in var:
    print(n)
--------------
�
�
�
�
�
�
--------------
```

通过上面的实例可以知道，Python3.5.x在输出中文或者英文的时候是按照一个字符一个字符来输出的，但是在Python2.7.x就不这样了，Python2.7.x是按照字节来进行输出的，可以看到在输出中文的时候是乱码的，而且还输出了六次，因为在UTF-8编码的情况下一个汉字是等于三个字节的，所以输出了六个乱码的字符。

在Python3.5.x里面是既可以输出汉字，也可以把输出字节的，利用bytes这个方法，bytes可以将字符串转换为字节

```
var="中文"
for n in var:
    print(n)
    bytes_list = bytes(n, encoding='utf-8')
    # 十六进制输出
    print(bytes_list)
    for x in bytes_list:
        # 十进制,bin(x)二进制
        print(x,bin(x))
-------------------------
# 字符串
中
# 十六进制
b'\xe4\xb8\xad'
# 228=十进制，0b11100100=二进制
228 0b11100100
184 0b10111000
173 0b10101101
文
b'\xe6\x96\x87'
230 0b11100110
150 0b10010110
135 0b10000111
```

####索引

索引是指某个值在列表或别的数据类型中的一个位置

```
>>> list_os = ["Windows","Linux","Mac","Unix"]
>>> list_os.index("Linux")
1
>>> list_os[1]
'Linux'
```

