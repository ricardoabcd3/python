def run():
    print("welcome \n this program solve your doubt of \n my word is a palimdrome,isn't it?")
    palimdrome = lambda string : string == string [::-1]
    print("enter your word ")
    ana=input("= ")
    print (palimdrome  (ana))
if __name__=='__main__':
    run()