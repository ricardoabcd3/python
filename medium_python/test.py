import os

def run():
    t=0
    s=0
    
    abu=[]
    ba="_______"
    mangos=0
    time=[]
    while t == 0:
        os.system ("cls")
        print(ba)
        txt = "bananas"
        cont=0
        cont2=0
        p=0
       
        
        
        
        #if s == 0:
         #   ba=ba*7
          #  s=1
        
        if mangos==0:

            for i in txt:
                cont=cont + 1 
                
                abu.append(i)
            mangos=1
        while p == 0:
            try:
                
                a=input("!guess the word¡")
                z=abu.index(a)
                p=1
            except ValueError:
                os.system ("cls")
                print(ba)
                p=0
        for i in abu:
            cont2=cont2+1
            if i == a:
                
                string_list = list(ba)
                cont2=cont2-1
                string_list[cont2] = a
                ba = "".join(string_list)
                cont2=cont2+1
                
        if ba== txt:
            os.system ("cls")
            print("congratulations : the word is ",ba)
            break
    
  
        
        
        
run()

