stringer = input("Enter the string")

def func(stringer):
    index = 0 
    list1 =[]
    newstr = ""
    while(index < len(stringer)):
        if(stringer[index]!= ' '):
            newstr += stringer[index]
        if(stringer[index] == '"'):
            index+=1
            while(stringer[index] != '"'):
                newstr += stringer[index]
                index+=1
            newstr+='"'
            if(index == len(stringer)-1):
                list1.append(newstr)
        if (stringer[index] == ' '):
            list1.append(newstr)
            newstr = ''
        index += 1
    for i in list1:
        print(i)

func(stringer)

print(sorted(tuple("testing 1243"))) 

