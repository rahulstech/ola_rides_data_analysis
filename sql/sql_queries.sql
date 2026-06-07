-- 1. Retrieve all successful bookings

SELECT 
    * 
FROM 
    `rides` 
WHERE 
    `booking_status` = 'Success' 
;



-- 2. Find the average ride distance for each vehicle type
SELECT
    `vehicle_type`,
    ROUND(AVG(`ride_distance`), 2) AS `vehicle_avg_ride_distance`
FROM
    `rides`
WHERE 
    `incomplete_rides` = ?
GROUP BY 
    `vehicle_type`
ORDER BY
    `vehicle_avg_ride_distance` DESC
LIMIT
    5
;



-- 3. Get the total number of cancelled rides by customers:

SELECT 
    count(`booking_id`) AS `canceled_by_customer_count`
FROM
    `rides`
WHERE
    `booking_status` = 'Canceled by Customer'
;



-- 4. List the top 5 customers who booked the highest number of rides

SELECT 
    `customer_id`, 
    COUNT(`booking_id`) AS `total_booking_by_customer`  
FROM 
    `rides` 
GROUP BY 
    `customer_id` 
ORDER BY 
    `total_booking_by_customer` DESC 
LIMIT 
    5
;



-- 5. Get the number of rides cancelled by drivers due to personal and car-related issues

SELECT
    COUNT(`booking_id`) AS `count`
FROM
    `rides`
WHERE
    `booking_status` = 'Canceled by Driver'
    AND `canceled_rides_by_driver` = 'Personal & Car related issue'
;


-- 6. Find the maximum and minimum driver ratings for Prime Sedan bookings

SELECT 
    MAX(`driver_ratings`) AS `max_driver_rating`,
    MIN(`driver_ratings`) AS `min_driver_rating`
FROM 
    `rides` 
WHERE 
    `vehicle_type` = 'Prime Sedan'
;



-- 7. Retrieve all rides where payment was made using UPI

SELECT 
    *
FROM
    `rides`
WHERE
    `payment_method` = 'UPI'
;


-- 8. Find the average customer rating per vehicle type

SELECT
    `vehicle_type`,
    ROUND(AVG(`customer_rating`), 1) AS `avg_customer_rating`
FROM 
    `rides`
GROUP BY
    `vehicle_type`
;



-- 9. Calculate the total booking value of rides completed successfully

SELECT 
    SUM(`booking_value`) AS `total_booking_value`
FROM
    `rides` 
WHERE
    `incomplete_rides` = 'No'
;



-- 10. List all incomplete rides along with the reason

SELECT 
    `booking_id`,
    `incomplete_rides`,
    `incomplete_rides_reason`
FROM
    `rides` 
WHERE 
    `incomplete_rides` = 'Yes'
;
