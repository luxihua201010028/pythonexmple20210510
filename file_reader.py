file_path = 'test_file_read/pi_digits.txt'
with open(file_path) as file_object:  # open file
    contens = file_object.readlines()  # store all lines in a list
pistring = ''  # create a variable to store pi
for line1 in contens:  # loop
    pistring += line1.strip()  # delete the \n
print(pistring)  # print pi
print(len(pistring))  # print the length of pi
str_input = input("please input your word to serach")
if str_input in pistring:
    print('%s in %s' % (str_input, pistring))
else:
    print('%s not in %s' % (str_input, pistring))
