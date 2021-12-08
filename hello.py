from random import randint
while True:
    a=input('Bạn chọn:')
    b= randint(0,2)
    if b==0:
        b='kéo'    
    elif b==1:
        b='búa'   
    elif b==2:
        b='bao'
    if a==b:
        print('máy chọn: '+b)  
        print('hòa')
    elif a=='kéo' and b=='bao':
        print('máy chọn: '+b)  
        print('you win')
    elif a=='bao' and b=='kéo':
        print('máy chọn: '+b)  
        print('you lose')
    elif a=='búa' and b=='kéo':
        print('máy chọn: '+b)  
        print('you win')  
    elif a=='búa' and b=='bao':
        print('máy chọn: '+b)  
        print('you lose')            
    elif a=='kéo' and b=='búa':
        print('máy chọn: '+b)  
        print('you lose')
    elif a=='bao' and b=='búa':
        print('máy chọn: '+b)  
        print('you win')     
    else:print('chọn kéo, búa, bao')