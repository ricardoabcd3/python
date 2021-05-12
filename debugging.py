'''
this is program to get a value and return their divisible numbers 
'''
def run():
    try:
        num=int(input("enter number : "))
        a=1
        if num >= 0:

            hi = [a for a in range (1, num + 1) if num % a == 0]
            print(hi)
            a=0
    except ValueError:
        print("wrong value")
        a=1
    if num <=0:
        print("enter a value grater than 0")
    while a == 1:
        try:
            num=int(input("enter number : "))
            if num >=0:
                hi = [a for a in range (1, num + 1) if num % a == 0]
                print(hi)
                a=0
        except ValueError:
            print("wrong value")
            a=1
        if num <=0:
            print("enter a value grater than 0")    
if __name__=='__main__':
    run()