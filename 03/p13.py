while(True):
    n=int(input())
    if(n==-1):break
    if(n>100):print('Error')
    elif(n>=80):print('A')
    elif(n>=75):print('B+')
    elif(n>=70):print('B')
    elif(n>=65):print('C+')
    elif(n>=60):print('C')
    elif(n>=55):print('D+')
    elif(n>=50):print('D')
    else:print('F')