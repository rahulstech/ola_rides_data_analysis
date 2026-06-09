import sqlite3
import atexit

db_path = "../sql/ola_rides.sqlite3"

db_conn = sqlite3.connect(db_path, check_same_thread=False)

cur = db_conn.cursor()


def close_db():
    cur.close()
    db_conn.close()


atexit.register(close_db)



def get_total_rides_booked():
    query = """
        SELECT 
            COUNT(`booking_id`) AS `total_rides_booked` 
        FROM
            `rides`
        ;
    """
    
    cur.execute(query)
    return cur.fetchone()[0]


def get_total_rides_completed():
    query = """
        SELECT 
            COUNT(`booking_id`) AS `total_successful_rides` 
        FROM
            `rides`
        WHERE
            `incomplete_rides` = ?
        ;
    """
    
    cur.execute(query, ("No",))
    return cur.fetchone()[0]


def get_total_rides_canceled():
    query = """
        SELECT 
            COUNT(`booking_id`) AS `total_rides_canceled` 
        FROM
            `rides`
        WHERE
            `booking_status` != ?
        ;
    """
    
    cur.execute(query, ("Success",))
    return cur.fetchone()[0]


def get_total_revenue():
    query = """
        SELECT 
            SUM(`booking_value`) AS `total_revenue`
        FROM 
            `rides`
        WHERE
            `booking_status` = ?
        ;
    """

    cur.execute(query, ("Success",))
    return cur.fetchone()[0]


def get_average_customer_ratings():
    query = """
        SELECT 
             ROUND(AVG(`customer_rating`), 1) AS `avg_customer_rating`
        FROM
            `rides`
        WHERE 
            `booking_status` = ?
        ;
    """

    cur.execute(query, ("Success",))
    return cur.fetchone()[0]


def get_daily_ride_volume():
    query = """
        SELECT 
            DATE(`date`) AS `date`,
            COUNT(`booking_id`) AS `daily_ride_volume` 
        FROM 
            `rides`
        GROUP BY 
            DATE(`date`) 
        ORDER BY 
            `date`
        ;
    """

    cur.execute(query)
    return cur.fetchall()


def get_booking_count_by_booking_status():
    query = """
        SELECT
            `booking_status`,
            COUNT(`booking_id`) AS `booking_count`
        FROM
            `rides`
        GROUP BY
            `booking_status`
        ;
    """

    cur.execute(query)
    return cur.fetchall()


def get_vehicle_ride_data():
    query = """
        SELECT
            `vehicle_type`,
            `vehicle_images`,
            SUM(`booking_value`) AS `total_booking_value`,
            SUM(CASE `booking_status` WHEN 'Success' THEN `booking_value` ELSE 0 END) AS `total_success_booking_value`,
            SUM(CASE `incomplete_rides` WHEN 'No' THEN 1 else 0 end) AS `total_complete_ride_count`,
            SUM(CASE `incomplete_rides` WHEN 'No' THEN `ride_distance` ELSE 0 END) AS `total_complete_ride_distance`
        FROM
            `rides`
        GROUP BY
            `vehicle_type`, `vehicle_images`
        ;
    """

    cur.execute(query)
    return cur.fetchall()


def get_revenue_by_payment_method():
    query = """
        SELECT 
            `payment_method`,
            SUM(`booking_value`) AS `revenue_by_payment_method`
        FROM
            `rides`
        WHERE
            `incomplete_rides` = ?
        GROUP BY
            `payment_method`
        ORDER BY 
            `revenue_by_payment_method`
        ;
    """

    cur.execute(query, ("No",))
    return cur.fetchall()


def get_top_5_customers_by_booking_value():
    query = """
        SELECT
            `customer_id`,
            sum(`booking_value`) AS `customer_total_booking_value`
        FROM 
            `rides`
        WHERE 
            `booking_status` = ?
        GROUP BY
            `customer_id`
        ORDER BY 
            `customer_total_booking_value` DESC
        LIMIT
            5
        ;
    """

    cur.execute(query, ("Success",))
    return cur.fetchall()


def get_daily_total_ride_distance():
    query = """
        SELECT
            DATE(`date`) AS `date`,
            SUM(`ride_distance`) AS `daily_total_ride_distance`
        FROM
            `rides`
        WHERE
            `incomplete_rides` = ?
        GROUP BY
            DATE(`date`)
        ORDER BY
            `date`
        ;
    """

    cur.execute(query, ("No",))
    return cur.fetchall()


def get_customer_cancellation_reasons():
    query = """
        SELECT
            `canceled_rides_by_customer`,
            COUNT(`booking_id`) AS `count`
        FROM
            `rides`
        WHERE 
            `booking_status` = ?
        GROUP BY 
            `canceled_rides_by_customer`
        ORDER BY
            `count`
        ;
    """
    
    cur.execute(query, ("Canceled by Customer",))
    return cur.fetchall()


def get_driver_cancellation_reasons():
    query = """
        SELECT
            `canceled_rides_by_driver`,
            COUNT(`booking_id`) AS `count`
        FROM
            `rides`
        WHERE 
            `booking_status` = ?
        GROUP BY 
            `canceled_rides_by_driver`
        ORDER BY
            `count`
        ;
    """
    
    cur.execute(query, ("Canceled by Driver",))
    return cur.fetchall()


def get_vehicle_ratings():
    query = """
        SELECT
            `vehicle_type`,
            `vehicle_images`,
            ROUND(AVG(`customer_rating`), 1) AS `avg_customer_rating`,
            ROUND(AVG(`driver_ratings`), 1) AS `avg_driver_rating`
        FROM
            `rides`
        WHERE
            `incomplete_rides` = 'No' AND `customer_rating` IS NOT NULL
        GROUP BY
            `vehicle_type`, `vehicle_images`
        ;
    """

    cur.execute(query)
    return cur.fetchall()
