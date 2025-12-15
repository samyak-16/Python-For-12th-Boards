import pickle
data = "My name is samyak"

# Pickling an object 
with open("students.dat","wb") as f :
    pickle.dump(data,f)

# UnPickling an object 

with open("students.dat","rb") as f :
    print(pickle.load(f))
