import csv 


# Writing to a CSV file
with open("test.csv","w",newline='') as f :
    writer = csv.writer(f)
    writer.writerow(["Name","Age","City"])
    writer.writerow(["Samyak Raj Subedi","18","Biratnagar"])


with open("test1.csv","w",newline='') as f :
    data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 22, 'Tokyo']
]
    writer = csv.writer(f)
    writer.writerows(data)


    # Reading to a CSV file


with open("test1.csv","r",newline='') as f :
    reader = csv.reader(f)
    print(reader)
    for i in reader :
        print (i)