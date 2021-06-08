def write():
    numbers = []
    with open ("data.txt", "r",encoding="utf-8") as files:
        for line in files:
            numbers.append(int(line))
        print(numbers)
        
    
def read():
    pass

def main():
    write()
    
    
if __name__=='__main__':
    main()
