



def hold_client(name):
    yield 'Hello, %s! You will be connected soon' % name
    yield 'Dear %s, could you please wait a bit.' % name
    yield 'Sorry %s, we will play a nice music for you!' % name
    yield '%s, your call is extremely important to us!' % name

def search(keyword, filename):
    print('generator started')
    f = open(filename, 'r')
    # Looping through the file line by line
    for line in f:
        if keyword in line:
            # If keyword found, return it
            yield line
    f.close()


if __name__ == '__main__':
    #the_generator = search('python', 'directory.txt')
    the_generator = hold_client('Sachin')
    print(next(the_generator))
    print(next(the_generator))
    print(next(the_generator))
    print(next(the_generator))

    