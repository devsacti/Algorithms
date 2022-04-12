import sys
import random

# member insert
# membership은 member의 반정규화 결과로서 member insert 시 자동 추가
def macro_member():
    print("-- member 테이블 insert" )
    for i in range(100):
        command="exec member_pack.member_insert("+  \
                "\'member"+str(i)+"\'"  + "," +  \
                "\'password!"+str(i)+"\'"  + "," + \
                "\'membername"+str(i)+"\'"  + "," + \
                "\'member"+str(i)+"@test.com\'"  + "," + \
                "\'010123400"+str(i)+"\'"  + "," + \
                "sysdate"  + "," + \
                "\'"+"남"+"\'"  + "," +  \
                ""+str(100+i)+""  + "," + \
                ""+str(i)+""  + \
                ")"
        print(command)


# board insert

def macro_board():
    print("-- board 테이블 insert" )
    for i in range(500):
        # 전체 게시물의 80프로는 20프로의 주 멤버가 작성한다.
        if(i<400):
            j=random.randrange(0,20)
        else:
            j=random.randrange(20,100)

        if(i<150):
            category="t"
        elif(i<250):
            category="b"
        elif(i<300):
            category="s"
        elif(i<350):
            category="t,b"
        elif(i<400):
            category="t,b,s"
        else:
            category="t,b,s,a"


        command="exec board_pack.board_insert("+  \
                "\'b"+str(i)+"\'"  + "," +  \
                "\'member"+str(j)+"\'"  + "," + \
                "\'title"+str(i)+"\'"  + "," + \
                "\'content"+str(i)+"\'"  + "," + \
                "\'picture"+str(i)+"\'"  + "," + \
                "sysdate"     + "," +       \
                "\'"+category+"\'" + \
                ")"
        print(command)

# reply insert

## 외래키로 구성된 기본키 특성상 입력되지 않을 경우를 염두하여 범위를 1000
def macro_reply():
    print("-- reply 테이블 insert" )

    # 총 댓글 1000개 상정
    # member0 ~ member99
    # b0 ~ b499
    for i in range(1000):

        # 전체 댓글의 80프로는 20프로의 게시물에 작성된다.
        if(i<800):
            j=random.randrange(0,100)
        else:
            j=random.randrange(100,500)


        # 전체 댓글의 80프로는 20프로의 사용자가 작성한다.
        if(i<800):
            k=random.randrange(0,20)
        else:
            k=random.randrange(20,100)


        command="exec reply_pack.reply_insert("+  \
                "\'b"+str(j)+"\'"  + "," + \
                "\'member"+str(k)+"\'"  + "," + \
                "\'content"+str(i)+"\'" + \
                ")"
        print(command)


if __name__=="__main__":
    sys.stdout = open('fashionReview_dump_insert.sql','w')
    macro_member()
    macro_board()
    macro_reply()
    sys.stdout.close()