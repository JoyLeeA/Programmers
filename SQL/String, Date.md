1. 루시와 엘라 찾기

```mysql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS WHERE NAME IN("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty") ORDER BY ANIMAL_ID ASC
```



2. 이름에 el이 들어가는 동물 찾기

```mysql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE NAME LIKE "%el%"AND ANIMAL_TYPE = "Dog" ORDER BY NAME
```



3. 중성화 여부 파악하기

```mysql
SELECT  ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE REGEXP 'Neutered|Spayed', 'O' , 'X') AS 중성화 FROM ANIMAL_INS

SELECT  ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE LIKE '%Neutered%' or SEX_UPON_INTAKE LIKE "%Spayed%", 'O' , 'X') AS 중성화 FROM ANIMAL_INS
```



4. 오랜 기간 보호한 동물(2)

```mysql
SELECT  O.ANIMAL_ID, O.NAME FROM ANIMAL_OUTS AS O INNER JOIN  ANIMAL_INS AS I ON  O.ANIMAL_ID = I.ANIMAL_ID ORDER BY DATEDIFF(O.DATETIME, I.DATETIME) DESC LIMIT 2;
```



5. DATETIME에서 DATE로 형 변환

```mysql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME,"%Y-%m-%d") FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC
```



* DATE_FORMAT() 관련

%M 

 월(Janeary, December, ...)

 %W

 요일(Sunday, Monday, ...)

 %D 

 월(1st, 2dn, 3rd, ...)

 %Y 

 연도(1987, 2000, 2013)

 %y

 연도(87, 00, 13) 

 %X 

 연도(1987, 2000) %V와 같이 쓰임.

 %x 

 연도(1987, 2000) %v와 같이 쓰임.

 %a 

 요일(Sun, Tue, ...)

 %d 

 일(00, 01, 02, ...) 

 %e

 일(0, 1, 2, ...) 

 %c 

 월(1, 2, ..., 12) 

 %b 

 월(Jan, Dec, ...) 

 %j 

 몇번째 일(120, 365) 

 %H 

 시(00, 01, 02, 13, 24) 

 %h 

 시(01, 02, 12)

 %I(대문자 아이)

 시(01, 02, 12)

 %l(소문자 엘)

 시(1, 2, 12) 

 %i 

 분(00, 01, 30) 

 %r 

 "hh:mm:ss AM|PM" 

 %T 

 "hh:mm:ss" 

 %S

 초 

 %s 

 초 

 %p

 AM, PM 

 %w 

 요일(0, 1, 2) 0:일요일 

 %U 

 주(시작:일요일) 

 %u 

 주(시작:월요일) 

 %V 

 주(시작:일요일) 

 %v

 주(시작:월요일) 



