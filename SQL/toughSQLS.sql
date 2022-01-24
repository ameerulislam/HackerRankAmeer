-- problem name: Prepare SQL Aggregation Top Earners
-- Had to use group by along with order and limit
SELECT (salary*months) as earnings, count(*) from Employee group by 1 order BY earnings DESC LIMIT 1 ;

-- problem name: Prepare SQL AggregationWeather Observation Station 15
LECT ROUND(LONG_W, 4) FROM STATION WHERE LAT_N < 137.2345 ORDER BY LAT_N DESC LIMIT 1;

-- problem name: Prepare SQL AggregationWeather Observation Station 18
SELECT ROUND(MAX(LAT_N)-MIN(LAT_N)+MAX(LONG_W)-MIN(LONG_W) ,4) FROM STATION;

-- problem name: Prepare SQL AggregationWeather Observation Station 19
SELECT 
ROUND(
    SQRT(
        POWER(MAX(LAT_N)-MIN(LAT_N), 2) +
        POWER(MAX(LONG_W)-MIN(LONG_W), 2)
    ), 
    4) FROM STATION;

-- Prepare SQL Aggregation Weather Observation Station 20 #BELOW STILL WRITE IN PROGRESS
SELECT COUNT(*) FROM STATION INTO @TOTAL;
-- SELECT @TOTAL;
-- SELECT MOD(@TOTAL,2);
SELECT FLOOR(@TOTAL/2) INTO @MYLIMIT;
-- SELECT @MYLIMIT;
PREPARE STMT FROM 'SELECT ROUND(LAT_N, 4) FROM STATION ORDER BY LAT_N ASC LIMIT ?, 1';
EXECUTE STMT USING @MYLIMIT;
-- SELECT ROUND(LAT_N, 4) FROM STATION ORDER BY LAT_N ASC LIMIT @MYLIMIT, 1
-- CASE 
    --     WHEN MOD(@TOTAL,2) = 1 
    --     THEN LIMIT CEIL(@TOTAL/2) , 1
    --     ELSE LIMIT CEIL(@TOTAL/2), 2
    -- END;