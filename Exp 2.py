# Activity 2.1
# Write a program to illustrate iteration over the list. 


list1=[10,10.5,'Apple',34,47]
length=len(list1)
while(1):
    print('*****List Iteration*******')
    print('1.Using For loop')
    print('2.Using for with range')
    print('3.Using while')
    print('4.Using List Comprehension')
    print('5.Using Enumeration')
    print('6.Exit')
    m=int(input('Enter your choice'))
    if(m==1):
        for i in list1:
            print(i)
    elif(m==2):
        for i in range(length):
            print(list1[i])
    elif(m==3):
        i=0
        while i < length:
            print(list1[i])
            i += 1
    elif(m==4):
        [print(i) for i in list1]
    elif(m==5):
        for i, val in enumerate(list1):
            print (i, ",",val)
    else:
        print('Exit from the program')
        break

# Activity 2.2
# Write a program to illustrate iteration over the dictionary. 



d = {'key1': 1, 'key2': 2, 'key3': 3}
for k in d:
    print(k)
print(list(d))
print(type(list(d)))
while(1):6
    print('********DICTIONARY ITERATION*********')
    print('1.Through Dictionary keys()')
    print('2.Through Dictionary values()')
    print('3.Through Dictionary items()')
    print('4.Exit')
    c=int(input('Enter Your Choice'))
    if(c==1):
        for k in d.keys():
            print(k)
        print(d.keys())
        print(type(d.keys()))
        print(list(d.keys()))
        print(type(list(d.keys())))
    elif(c==2):
        for v in d.values():
            print(v)
        print(d.values())
        print(type(d.values()))
    elif(c==3):
        for k, v in d.items():
            print('Keys=',k, 'Values=',v)
        print(d.items())
        print(type(d.items()))
    elif(c==4):
        break

        




