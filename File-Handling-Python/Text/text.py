#  Default mode : r --> throws error if file is not present in the directory 
# file = open("sample.txt")
# print(file.read())

# file2 = open("sample.txt","w")
# #    mode : w --> doesn't throws error if file is not present in the directory and creates the file by itself
# file2.write("Original content will be over write")
# print(file.read())

# ---------------------------------------------------------------------------------------------

#  Second syntax 
# try:
#     with open("sample2.txt","w") as f :
#         print (f.write("Hello world im inside sample2.txt"))
        
# except FileExistsError:
#     print("File isn't present")


# try:
#     with open("sample2.txt") as f :
#         print (f.read())
#         f.seek(0)          # move cursor back to start
#         print (f.readline())
#         f.seek(0)          # move cursor back to start
#         print (f.readlines())
#         f.close()
        
# except FileExistsError:
#     print("File isn't present")



try:
    with open("sample2.txt","w") as f :
     
     f.writelines(["Samyak\n","Pranika\n","Prabesh\n","Sampada\n"])
        
except FileExistsError:
    print("File isn't present")



