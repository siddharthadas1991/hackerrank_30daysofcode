T = int(input())

for i in range(0,T):
    
    S = input()
    
    for j in range(0,len(S)):
        if j%2==0:
            print(S[j], end='')

    print(" ", end='')

    for j in range(0, len(S)):
        if j % 2 != 0:
            print(S[j], end='')

    print("")
            
            