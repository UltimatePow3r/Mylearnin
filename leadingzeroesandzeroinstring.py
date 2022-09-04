String1=input("Enter a string\n")

def func1(test):
    beginvar=0
    for ele in test:
        if ele == '0':
            beginvar+=1
        else:
            break
    for i in range(beginvar,len(test)):
        if(test[i] == '0'):
            return True
    return False

print(func1(String1))

