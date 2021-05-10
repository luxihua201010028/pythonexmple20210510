filename = 'test_file_read/programming.txt'


def countwords(filename):
    with open(filename, 'r') as file_object:
        words = file_object.read().split()
        print(words)
        print(len(words))


countwords(filename)
