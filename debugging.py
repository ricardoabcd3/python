
def run():
    try:
        num=int(input("enter number : "))
    except ValueError:
        print("wrong value")

    hi = [a for a in range (1, num + 1) if num % a == 1]
    print(hi)
if __name__=='__main__':
    run()