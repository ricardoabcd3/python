def main():

   '''
    dic={}
    for i in range(1,101):
        if i % 3 !=0:

            dic[i]=i**3
    '''
    dic = {i: i**3 for i in range (1,101) if i % 3 !=0}
    print(dic)
    '''for keys,values in dic.items():
        print(keys)
        print(values)
        '''


if __name__== '__main__':
     main()