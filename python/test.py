def macro_member():
    print(" #####################################start" )
    for i in range(100):
        command="exec member_pack.member_insert("+  \
                "\'user"+str(i)+"\'"  + "," +  \
                "\'password!"+str(i)+"\'"  + "," + \
                "\'username"+str(i)+"\'"  + "," + \
                "\'user"+str(i)+"@test.com\'"  + "," + \
                "\'010123400"+str(i)+"\'"  + "," + \
                ""+str(i)+""  + "," + \
                "\'"+"남"+"\'"  + "," +  \
                ""+str(100+i)+""  + "," + \
                ""+str(i)+""  + \
                ")"
        print(command)
    print(" #####################################end" )
        

def macro_board():
    print(" #####################################start" )
    for i in range(100):
        command="exec board_pack.board_insert("+  \
                "\'b"+str(i)+"\'"  + "," +  \
                "\'user"+str(i)+"\'"  + "," + \
                "\'title"+str(i)+"\'"  + "," + \
                "\'content"+str(i)+"\'"  + "," + \
                "\'picture"+str(i)+"\'"  + "," + \
                "sysdate"             \
                + ")"
        print(command)
    print(" #####################################end" )

import random

def macro_reply():
    print(" #####################################start" )
    for _ in range(100):
        i=random.randrange(0,100)    
        command="exec reply_pack.reply_insert("+  \
                "\'r"+str(i)+"\'"  + "," +  \
                "\'b"+str(i)+"\'"  + "," + \
                "\'user"+str(i)+"\'"  + "," + \
                "\'content"+str(i)+"\'"  + "," + \
                ")"
        print(command)
    print(" #####################################end" )



if __name__=="__main__":
    macro_member()