import sys
import random

# board insert

def macro_article():
    print("-- article 테이블 insert" )
    for i in range(1,130):
        command="INSERT INTO edudb.article (no,board_id,subject,title,name,content,password) VALUES ("+  \
                ""+str(i)+""  + "," +  \
                ""+str(1)+""  + "," +  \
                "\'yesterday"+"\'"  + "," + \
                "\'이러지도, 저러지도"+"\'"  + "," + \
                "\'adam"+"\'"  + "," + \
                "\'나서자니, 에러와 실수를 찾아가는 것 같고, 가만히 있어도 에러와 실수는 찾아온다"+"\'"  + "," + \
                ""+str(1234)+""  + "" +  \
                ");"
        print(command)


if __name__=="__main__":
    #  sys.stdout = open('fashionReview_dump_insert.sql','w')

    macro_article()

    #  sys.stdout.close()