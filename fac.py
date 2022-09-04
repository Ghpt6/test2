def fac(n):
    N=n
    if type(n)!=type(0):                       #判断类型
        print('请输入大于等于0的整数')
    elif n==0:
        print(0)
    elif n<0:
        print('请输入大于等于0的整数')
    else:
        while n>1:
          n-=1
          N*=n
        print(N)

