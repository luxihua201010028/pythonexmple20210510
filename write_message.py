filename= 'test_file_read/programming.txt'
with open(filename,'w') as file_object:
    file_object.write(" i love python.\n")
    file_object.write(" i love you.\n")
with open(filename,'r+') as file_object1:
    contens=file_object1.read()
    print(contens)
