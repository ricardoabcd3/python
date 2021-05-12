
def run():
    try:
        num=int(input("enter number : "))
        hi = [a for a in range (1, num + 1) if num % a == 1]
        print(hi)
        a=0
    except ValueError:
        print("wrong value")
        a=1
    while a == 1:
        try:
            num=int(input("enter number : "))
            hi = [a for a in range (1, num + 1) if num % a == 1]
            print(hi)
            a=0
        except ValueError:
            print("wrong value")
            a=1


    
if __name__=='__main__':
    run()