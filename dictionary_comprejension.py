import math
import time
def delay(k,c):
    print(k)
    time.sleep(c)


def main():
    dic={i: math.sqrt(i) for i in range(1,1001)}
    delay("welcome to a my code..",1)
    delay("it's come a list of square roots from 1 to 1000\n in ",1)
    delay("three",2)
    delay("two",2)
    delay("here we go....",2)
    
    for e,h in dic.items():

        print(e,h)



if __name__=='__main__':
    main()