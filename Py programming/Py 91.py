numlist=list()
while (True):
    inp=input('Enter a number: ')
    if inp=='done':
        break
    value=float(inp)
    average=sum(numlist)/len(numlist)
    print('Average: ',average)
