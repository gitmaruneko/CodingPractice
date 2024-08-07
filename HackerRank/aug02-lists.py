#!/bin/python3


#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#sort
#print
#pop
#reverse


# inseet/ print/ remove/ append/ sort/ pop/ reverse

if __name__ == '__main__':
    N = int(input())

#solution 1
    operations = []
    arr = []
    for _ in range(N):
        op = input().split()
        operations.append(op)
    

    for _ in operations:
        op = _[0]
            
        if op == 'insert':
            index = int(_[1])
            value = int(_[2])
            arr.insert(index, value)
        if op == 'remove':
            value = int(_[1])
            arr.remove(value)
        if op == 'append':
            value = int(_[1])
            arr.append(value)
        if op == 'sort':
            arr.sort()
        if op == 'pop':
            arr.pop()
        if op == 'reverse':
            arr.reverse()
        if op == 'print':
            print(arr)



# solution opt

    # outlist = []
    # for _ in range(N):
    #     args = input().strip().split(' ')
    #     cmd = args[0]
    #     if cmd == 'insert':
    #         outlist.insert(int(args[1]), int(args[2]))
    #     elif cmd == 'remove':
    #         outlist.remove(int(args[1]))
    #     elif cmd == 'append':
    #         outlist.append(int(args[1]))
    #     elif cmd == 'print':
    #         print(outlist)
    #     elif cmd == 'sort':
    #         outlist.sort()
    #     elif cmd == 'pop':
    #         outlist.pop()
    #     elif cmd == 'reverse':
    #         outlist.reverse()



    
