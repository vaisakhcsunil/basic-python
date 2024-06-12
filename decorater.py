# def make_pretty(func):
    # def inner():
        # print("i got decorater")
        # func()
    # return inner
# @make_pretty
# def ordinary():
    # print("i am ordinary")
# ordinary()



# def smart_divide(func):
    # def inner(a,b):
        # print("i am going to divide",a,"and",b)
        # if b==0:
            # print("whoops i cant divide")
            # return
        # return func(a,b)
    # return inner
# @smart_divide
# def divide(a,b):
    # print(a/b)
    # 
# divide(2,5)
# 
# divide(2,0)




def outer_div (func):
    def inner(x,y):
        if(x<y):
            x,y=y,x
        return func(x,y)
    return inner
def divide(x,y):
    print(x/y)
divide(10,2)

    

