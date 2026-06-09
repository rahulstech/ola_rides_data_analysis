import streamlit as st
import database as db

def content_kpis():
    total_rides_booked = db.get_total_rides_booked()
    total_rides_completed = db.get_total_rides_completed()
    total_rides_canceled = db.get_total_rides_canceled()
    total_revenue = db.get_total_revenue()
    avg_customer_rating = db.get_average_customer_ratings()
    cancel_rate = round(100.00 * total_rides_canceled / total_rides_booked, 2)

    col1, col2, col3 = st.columns(
        spec=3,
        border=True
    )

    col1.metric(
        label="Total Rides Booked",
        value=total_rides_booked
    )

    col2.metric(
        label="Total Rides Completed",
        value=total_rides_completed
    )

    col3.metric(
        label="Booking Cancellation Rate",
        value=f"{cancel_rate}%"
    )

    col4, col5 = st.columns(
        spec=2,
        border=True
    )

    col4.metric(
        label="Total Revenue",
        value=total_revenue
    )

    col5.metric(
        label="Average Customer Rating",
        value=avg_customer_rating
    )


def section_overall():

    st.title("Overall",text_alignment="center")

    content_kpis()
