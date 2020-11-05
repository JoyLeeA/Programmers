1. 최댓값 구하기

```mysql
SELECT MAX(DATETIME) AS "시간" FROM ANIMAL_INS 
```



2. 최솟값 구하기

```mysql
SELECT MIN(DATETIME) as "시간" FROM ANIMAL_INS
```



3. 동물 수 구하기

```mysql
SELECT COUNT(*) AS "count" FROM ANIMAL_INS
```



4. 중복 제거하기

```mysql
SELECT COUNT(DISTINCT NAME) AS "count" FROM ANIMAL_INS WHERE NAME IS NOT NULL
```

