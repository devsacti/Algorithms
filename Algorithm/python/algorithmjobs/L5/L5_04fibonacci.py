if __name__=='__main__':
    n=int(input())

    fibo_sequences=[0,1]
    
    if(n<2):
        print(fibo_sequences[n])
    else:
        for i in range(n-1):
            fibo_sequences.append(fibo_sequences[-1]+fibo_sequences[-2])
        
        print(fibo_sequences[-1])


