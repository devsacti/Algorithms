# SQL
 '관계형 데이터베이스(RDB)'를 전제로 데이터를 관리하기 위한 프로그래밍 언어
 반대로, noSQL이 존재
 *MySQL 기준

# kinds of SQL
 Data Definition Language ; DDL
 Data Manipulation Language ; DML
 Data Control Language ; DCL

 * 아래 명령문 예시에서 테이블 혹은 뷰 이름은 myexampletable로 통일, 추가 시 myexampletable2

## DDL
CREATE TABLE myexampletable(
 my_field1 INT,
 my_field2 VARCHAR(50),
 my_field3 DATE NOT NULL,
 PRIMARY KEY (my_field1, my_field2)
);

ALTER TABLE myexampletable ADD my_field4 NUMBER(3) NOT NULL;

TRUNCATE TABLE myexampletable;

DROP TABLE myexampletable;

## DML
SELECT myexampletable.공통컬럼 FROM myexampletable [INNER] JOIN myexampletable2 ON myexampletable.공통컬럼 = myexampletable2.공통컬럼;

INSERT INTO myexampletable (컬럼1, [컬럼2, ...]) values (값1, [값2, ...])
INSERT INTO myexampletable values (값1, [값2, ...])

UPDATE myexampletable SET column_name = value [, column_name = value ...] [WHERE condition]

DELETE FROM myexampletable [WHERE 조건]

출처:https://ko.wikipedia.org/wiki/SQL

## DCL
-- 사용자 권한 부여 명령어
GRANT ALL PRIVILEGES ON [dbname.myexampletable] TO [user@host] IDENTIFIEDBY 'my_password';
 
-- 예제 (호스트 : 로컬호스트)
GRANT ALL PRIVILEGES ON testDB.myexampletable TO myuser@localhost IDENTIFIEDBY 'testPassword';
 
-- 예제 (호스트 : 원격 접속)
GRANT ALL PRIVILEGES ON testDB.myexampletable TO myuser@'%' IDENTIFIEDBY 'testPassword';
 
-- 예제 (호스트 : 아이피)
GRANT ALL PRIVILEGES ON testDB.myexampletable TO myuse@192.168.0.100 IDENTIFIEDBY 'testPassword';

출처: https://kkamikoon.tistory.com/171 [컴퓨터를 다루다]