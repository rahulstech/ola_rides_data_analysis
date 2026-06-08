import sqlite3

db_path = "../sql/ola_rides.sqlite3"

db_conn = sqlite3.connect(db_path)

cur = db_conn.cursor()


def get_top_5_vehicle_by_ride_distance():
    query = """
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