一个将RPN这种计算表达式字符串还原成表达式并计算出结果的题。

我的解法：从左往右遍历，在每次遇到运算符时处理这个运算符与其前面两个数值，再不断的循环直到处理完所有的元素。这是一种从内部往外的处理方式，其实也可以从右往左来递归，从第一个运算符出发，往左扫描，每当遇到一个运算符就开始这个过程，直到遇到的是两个数值。我想我是因为没有用递归所以时间很长

注意点：因为python的int除法是向下取整，而C，java都是向零取整，而答案需要向零取整的结果，因此
```
if x*y<0 and opr == '/':
    abs(x)/abs(y)*-1
```