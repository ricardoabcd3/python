def main():
    #squares = []
    #for i in range (1,101):
        
    #    if i % 3 != 0:

     #       squares.append(i**2)
    squares = [a for a in range (1, 10000) if a % 4 ==0 and  a % 6 == 0 and  a % 9 ==0]
    print (squares)
    


if __name__== '__main__':
    main()
