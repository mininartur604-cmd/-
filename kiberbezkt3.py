def main():
    aaa = 1
    while aaa != '2':
        wt = input('Как что делаем 1-шифрование 2-расшифрование: ')
        if wt == '1':
            incription()
        elif wt =='2':
            decription()
        else: print('чото не то')
        aaa = input('Продолжить ? 1-да 2-нет (def 1): ')

def incription():
    a = int(input("Выберите язык: 1-русский, 2-английский: "))
    d = int(input("Выберите шаг: "))
    c = input("Введите сообщение, которое хотите зашифровать: ")
    r = ""
    b = []  
    if a == 1:
        print ("Зашифрованный текст:" , ru(c,d,b,r))
    if a == 2:    
        print ("Зашифрованный текст:" , angl(c,d,b,r))
            
def decription():
    c = input('Введите сообщение, которое хотите расшифровать: ')
    a = int(input("Выберите язык: 1-русский, 2-английский: "))
    b = []
    n=0
    answer = 1
    while answer != '2':
        n +=1
        r = ''
        if a == 1:
            print ('Итеррация', n ,"расшифрованный текст:" , ru(c,n,b,r))
        if a == 2:    
            print ('Итеррация', n ,"расшифрованный текст:" , angl(c,n,b,r))

        answer = input('Расшифровалось? 1-нет 2-да (def 1): ')

def angl(c,n,b,r):
    for i in range(len(c)):
        currentChar = ord(c[i])
        b.append(currentChar) 
                    
        if currentChar >= 65 and currentChar <= 90: 
            b[i] = currentChar + n
                    
            while b[i] > 90:
                b[i] = b[i] - 26
                    
            while b[i] < 65:
                b[i] = b[i] + 26
                    
        elif currentChar >= 97 and currentChar <= 122:
            b[i] = currentChar + n
            
            while b[i] > 122:
                b[i] = b[i] - 26
                
            while b[i] < 97:
                b[i] = b[i] + 26
                
        r += chr(b[i])
    return r

def ru(c,n,b,r):
    for i in range(len(c)):
        currentChar = ord(c[i])
        b.append(currentChar) 
        
        if currentChar >= ord('а') and currentChar <= ord('я'): 
            b[i] = currentChar + n
            
            while b[i] > ord('я'):
                b[i] = b[i] - 32
            
            while b[i] < ord('а'):
                b[i] = b[i] + 32
            
        elif currentChar >= ord('А') and currentChar <= ord('Я'):
            b[i] = currentChar + n
            
            while b[i] > ord('Я'):
                b[i] = b[i] - 32
                
            while b[i] < ord('А'):
                b[i] = b[i] + 32  
    
        r += chr(b[i])
    return r

main()
# Задание 1
# Ассиметричное шифрование
# Хеш-функция
# Хеш-функция
# Цифровая подпись
# Симметричное шифрование

# Задание 3
# Приватным
# 2 h1
# 3 PrA
# 4 PuA
# 5 PuA
# 6 равно 
