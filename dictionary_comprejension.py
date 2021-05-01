import math
import time
def main():
    dic={i: math.sqrt(i) for i in range(1,1001)}
    
    print("welcome to a my code..")
    time.sleep(1)
    print("it's come a list of square roots from 1 to 1000\n in ")
    time.sleep(2)
    print("three")
    time.sleep(2)
    print("two")
    time.sleep(2)
    print("one")
    time.sleep(2)
    print("here we go....")
    time.sleep(2)
    for e,h in dic.items():

        print(e,h)



if __name__=='__main__':
    main()