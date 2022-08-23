# from plistlib import FMT_XML


# fm = input().rstrip().split()
# m = int(fm[0])
# n = int(fm[1])
# q = int(fm[2])
# t = map(int,input().rstrip().split())
# print(fm,m,m,q,t)

# num  = [1,2,3,4]
# result = map(lambda a: a*a ,num)
# print(tuple(result))

# num1 = [2,4,6,8]
# num2 = [1,3,5,7]

# result = map(lambda a,b : a+b ,num1,num2)
# print(list(result))

# num = [0,2,4,5,7,8]

# rslt = filter(lambda x :x%2!=0,num)
# print(list(rslt))
# rslt = filter(lambda a:a%2==0,num)
# print(list(rslt))

# def myf(arg1,*argv):
#     print("First argument is:",arg1)
#     for i in argv:
#         print("Next arguments are:",i)
# myf('Kathmandu','is','located','in','heaven')


# def  arguments(*argv):
#     for i in argv:
#         print("Arguments are :",i)

# hi = ['Sunday','Monday']
# arguments(*hi)


def keyword_arguments(*args,**kwargs):
    
    for i in args:
        print("Other arguments are:",i)
    

    for key , value in kwargs.items():
        print(f"{key} is a {value}")


hr  =["Hari","Ram","Sita"]
kw = {
    "Sunday":"fun day",
    "Monday": "work day",
    "Tuesday": "boring day"
}
keyword_arguments(*hr,**kw)








