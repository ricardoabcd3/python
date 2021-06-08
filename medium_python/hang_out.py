import os
import random
def hangman(one):#define hang_out's draw
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    print(HANGMANPICS[one])


def ya():
    one=6#total lives
    con=0
    ba="_"
    numbers = []#this is to read the document data2.txt and chose a ramdom word
    with open ("data2.txt", "r",encoding="utf-8") as files:
        for line in files:
            if line == "\n":
                break
            numbers.append(line)
    
        
    txt=random.choice(numbers)
    for i in txt:
        con=con+1
    print(txt)
    
    ba=ba*(con-1)#define each letter in the word chosed to space 
    t=0
    s=0
    
    abu=[]
   
    mangos=0
    time=[]
    while t == 0:

        os.system ("cls")
        hangman(one)
        print(ba)
        
        
        
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
            if one== 1:
                os.system ("cls")
                print("sorry ,end game ¡¡¡¡")
                break
            
            try:                
                
                
                a=input("!guess the word¡")
                z=abu.index(a)
                p=1
                
            except ValueError:
                os.system ("cls")
                one=one-1
                hangman(one)
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
        if one== 1:
                os.system ("cls")
                print("sorry ,end game ¡¡¡¡")
                break
               
        if ba +"\n" == txt:
            
            os.system ("cls")
            print("congratulations : the word is ",ba)
            break
    
    

def main():
    #os.system ("cls")     
    
    ya()


if __name__=='__main__':

    main()