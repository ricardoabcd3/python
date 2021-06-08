def run():
    num=input("enter number : ")
    assert num.isnumeric(),"wrong value"
    if int(num) <=0:
        "wrong value ,it is least than 1"
    if int(num) >= 0:
        num=int(num)
        hi = [a for a in range (1, num + 1) if num % a == 0]
        print(hi)
        a=0
    
if __name__=='__main__':
    run()