from altair.theme import names
from streamlit.delta_generator import DeltaGenerator
import streamlit as st
import database as db
import pandas as pd 
import plotly.express as ex

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


def tab_content_ride_volume(tab: DeltaGenerator):
    data = db.get_daily_ride_volume()
    df = pd.DataFrame(
        data,
        columns=["Date", "Ride Volume"]
    )

    line = ex.line(
        data_frame=df,
        x="Date",
        y="Ride Volume",
    )

    tab.plotly_chart(
        figure_or_data=line,
        height=500,
        use_container_width=True
    )

    with tab.expander(label="Show Raw Data") as exp:
        exp.dataframe(
            df,
            hide_index=True,
            width='stretch',
            use_container_width=True
        )


def tab_content_booking_status_breakdown(tab: DeltaGenerator):
    data = db.get_booking_count_by_booking_status()
    df = pd.DataFrame(
        data,
        columns=["Booking Status", "Booking Count"]
    )

    donut = ex.pie(
        data_frame=df,
        names="Booking Status",
        values="Booking Count",
        hole=0.4
    )
    donut.update_traces(textinfo="value")

    tab.plotly_chart(
        figure_or_data=donut,
        height=500,
        use_container_width=True
    )


def content_chart_tabs():
    tab1, tab2 = st.tabs(
        tabs=[
            "Daily Ride Volume",
            "Booking Status Breakdown"
        ],
        default="Daily Ride Volume"
    )

    tab_content_ride_volume(tab1)

    tab_content_booking_status_breakdown(tab2)


def section_overall():

    st.title("Overall",text_alignment="center")

    content_kpis()

    content_chart_tabs()
