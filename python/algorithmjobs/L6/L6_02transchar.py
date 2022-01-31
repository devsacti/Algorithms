if __name__=='__main__':
    text=input()

    trans_text=[]
    for char in text:
        if(ord(char)>=65+32 and ord(char)<=65+32+26):
            trans_text.append(char.upper())
        elif(ord(char)>=65 and ord(char)<=(65-1)+26):
            trans_text.append(char.lower())
        else:
            trans_text.append(char)

    for char in trans_text:
        print(char,end='')