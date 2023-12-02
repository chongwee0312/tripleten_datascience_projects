/*
Find the number of taxi rides for each taxi company 
for November 15-16, 2017
*/
CREATE TABLE company_avg_trips AS
SELECT
    cabs.company_name AS company_name,
    COUNT(trips.trip_id) AS trips_amount
FROM
    cabs
RIGHT JOIN
	trips
ON
	cabs.cab_id = trips.cab_id 
WHERE
    CAST(trips.start_ts AS date) BETWEEN '2017-11-15' AND '2017-11-16'
GROUP BY
    company_name
ORDER BY
    trips_amount DESC;

/*
Find the number of rides for every taxi company whose name 
contains the words "Yellow" or "Blue" for November 1-7, 2017
*/
SELECT
    cabs.company_name AS company_name,
    COUNT(trips.trip_id) AS trips_amount
FROM
    cabs
RIGHT JOIN
	trips
ON
	cabs.cab_id = trips.cab_id
WHERE
    CAST(trips.start_ts AS date) BETWEEN '2017-11-01' AND '2017-11-07'
    AND cabs.company_name ~ '(Yellow|Blue)'
GROUP BY
    company_name;
	
/*
Find the number of rides for Flash Cab and Taxi Affiliation Services
for November 1-7
*/
SELECT
    CASE WHEN company_name IN ('Flash Cab', 'Taxi Affiliation Services') THEN
        company_name
    ELSE 
        'Other' 
    END AS company,    
    COUNT(trips.trip_id) AS trips_amount
FROM
    cabs
RIGHT JOIN
    trips
ON
    cabs.cab_id = trips.cab_id 
WHERE
    CAST(trips.start_ts AS date) BETWEEN '2017-11-01' AND '2017-11-07'
GROUP BY
    company
ORDER BY
    trips_amount DESC;
	
/*
Calculate the average number of trips in November 2017
for each dropoff location
*/
CREATE TABLE dropoff_loc_avg_trips AS
WITH month_day_counts AS (
    SELECT
        neighborhoods.name AS drop_off_location,
        COUNT(DISTINCT DATE_TRUNC('day', CAST(trips.end_ts AS date))) AS days_in_month
    FROM
        trips
    LEFT JOIN
        neighborhoods
    ON
        trips.dropoff_location_id = neighborhoods.neighborhood_id
    WHERE
        EXTRACT(MONTH FROM CAST(trips.end_ts AS date)) = 11
    GROUP BY
        neighborhoods.name
)

SELECT
    neighborhoods.name AS drop_off_location,
    COUNT(trips.trip_id) / month_day_counts.days_in_month AS average_trips
FROM
    trips
LEFT JOIN
    neighborhoods
ON
    trips.dropoff_location_id = neighborhoods.neighborhood_id
LEFT JOIN
    month_day_counts
ON
    neighborhoods.name = month_day_counts.drop_off_location
GROUP BY
    neighborhoods.name, month_day_counts.days_in_month
ORDER BY
    average_trips DESC;
	
/*
Retrieve the identifiers of the O'Hare and Loop neighborhoods
*/
SELECT
    name,
    neighborhood_id
FROM
    neighborhoods
WHERE
    name in ('O''Hare', 'Loop');
	
/*
For each hour, retrieve the weather condition records
*/
SELECT
    ts,
    CASE WHEN description LIKE '%rain%' OR description LIKE '%storm%' THEN
        'Bad'
    ELSE 
        'Good' 
    END AS weather_conditions
FROM
    weather_records;
	
/*
Retrieve all the rides that started in the Loop (pickup_location_id: 50) 
on a Saturday and ended at O'Hare (dropoff_location_id: 63)
Get the weather conditions for each ride
*/
CREATE TABLE loop_ohare_trips AS
SELECT
    trips.start_ts,
    weather_temp.weather_conditions,
    trips.duration_seconds
FROM
    trips
LEFT JOIN (
    SELECT
        ts,
        CASE
            WHEN description LIKE '%rain%' OR description LIKE '%storm%' THEN 'Bad'
            ELSE 'Good'
        END AS weather_conditions
    FROM
        weather_records
) AS weather_temp
on 
	trips.start_ts = weather_temp.ts
WHERE
    trips.pickup_location_id = 50
    AND trips.dropoff_location_id = 63
    AND EXTRACT(DOW FROM trips.start_ts) = 6
ORDER BY
    trips.trip_id;