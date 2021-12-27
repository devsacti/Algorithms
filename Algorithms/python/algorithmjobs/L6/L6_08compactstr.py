if __name__=='__main__':
    character_dict=dict()

    text=input()

    '''입력값의 순서 가치가 있나 없나'''
    # for char in text:
    #     if(char not in character_dict.keys()):
    #         character_dict[char]=1
    #     else:
    #         character_dict[char]+=1

    cnt_char=1
    source_compacted_text=list()
    '''언제나 파이썬 형식이 편한건 아니야'''
    # for idx,char in enumerate(text):
    #     if(ex_char!=char):

    #         cnt_char=1
    #         ex_char=char
    #     else:
    #         cnt_+=1

    for idx in range(len(text)):
        cur_char=text[idx]
        
        if(idx==0):
            ex_char='*'
        else:
            ex_char=text[idx-1]
        
        if(ex_char==cur_char):
            cnt_char+=1
        else:
            source_compacted_text.append((cnt_char,ex_char))
            cnt_char=1

        if(idx==len(text)-1):
            source_compacted_text.append((cnt_char,cur_char))
            
    # print(source_compacted_text)
    source_compacted_text=source_compacted_text[1:]
    # print(source_compacted_text)

    compacted_text=[]

    for element in source_compacted_text:
        k, v = element

        if(k!=1):
            compacted_text.append(str(k))

        compacted_text.append(v)

    print(''.join(compacted_text))