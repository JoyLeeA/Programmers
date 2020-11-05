1. 고양이와 개는 몇 마리 있을까

```mysql
SELECT ANIMAL_TYPE, COUNT(*) AS "count" FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE ASC
```



2. 동명 동물 수 찾기

```mysql
SELECT NAME, COUNT(*) as "COUNT" FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) >= 2 ORDER BY NAME ASC
```



3. 입양 시각 구하기(1)

```mysql
SELECT HOUR(DATETIME) as 'HOUR', count(HOUR(DATETIME)) as 'COUNT' from ANIMAL_OUTS
    # where HOUR(DATETIME) >= 9 and HOUR(DATETIME) < 20
    where HOUR(DATETIME) between 9 and 20 # WHERE절에서는 as 키워드를 사용할수 없음
    group by HOUR #group by와 order by는 사용 가능
    # Having Hour between 9 and 20
    order by HOUR ASC;
```



4. 입양 시각 구하기(2)

```mysql
WITH RECURSIVE cte 
AS 
( SELECT 0 AS HOUR
 UNION ALL
 SELECT HOUR + 1
 FROM cte
 WHERE HOUR < 23 )
SELECT      cte.hour, COUNT(ani.ANIMAL_ID)
FROM        cte
LEFT JOIN   ANIMAL_OUTS AS ani
ON          cte.hour = HOUR(ani.DATETIME)
GROUP BY    cte.hour
```

