

try:
    i = 1
    number = int(input('Enter a number: '))
    if number > 0 :
        print('Sequence is: ', end='')
        while i <= int(number):
            if(str(i) == str(i)[::-1] and "{0:b}".format(int(i)) == "{0:b}".format(int(i))[::-1]):
                print(i, end=',')
            i+=1
    else:
        print('Oops, I can’t deal with negative numbers or zero. ')
except:
    print('Sorry, I understand only numbers.')