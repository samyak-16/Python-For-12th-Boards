oldArray = [1,22,123,25,91]

def sumArray(a):
    newArr=[]
    for i in a :
        strNum=str(i)
        sum=0
        for j in strNum :
            sum+=int(j)
        newArr.append(sum)
    return newArr

print(sumArray(oldArray)) #[1,4,6,7,10]