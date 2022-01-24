def fib(a):
    if a==0 or a==1:
        return 1
    else:
        return fib(a-1)+fib(a-2)

if __name__=='__main__':
    print(fib(5))