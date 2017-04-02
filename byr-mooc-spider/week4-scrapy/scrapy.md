###Framework

[Lecture notes](https://drive.google.com/open?id=0Bxvv1hqGj91VeVoxRGdQc05pS0E)


###Practice

[Lecture notes](https://drive.google.com/open?id=0Bxvv1hqGj91VXzdBa1lYWWxnZnM)


Understand `yield`:

<http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python>


```
#产生所有小于 n 的平方值

def gen(n):
    for i in range(n):
    yield i**2

for i in gen(5):
    print (i, " ", end="")

To master yield, you must understand that when you call the function, the code you have written in the function body does not run. The function only returns the generator object, this is a bit tricky :-)
```



