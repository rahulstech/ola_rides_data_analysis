from streamlit.delta_generator import DeltaGenerator
import streamlit as st 
import database as db
import pandas as pd
import plotly.express as px


def content_revenue_by_payment_method(target: DeltaGenerator):
    data = db.get_revenue_by_payment_method()
    df = pd.DataFrame(
        data,
        columns=["Payment Method","Revenue"]
    )

    fig = px.bar(
        df,
        x="Payment Method",
        y="Revenue",
        color="Payment Method",
    )

    target.plotly_chart(
        fig,
        height=500,
        width='stretch',
        use_container_width=True
    )


def content_top_5_customer_by_booking_value(target: DeltaGenerator):
    data = db.get_top_5_customers_by_booking_value()
    df = pd.DataFrame(
        data,
        columns=["Customer ID","Total Booking Value"]
    )

    fig = px.bar(
        df,
        x="Customer ID",
        y="Total Booking Value",
        color="Customer ID",
    )

    target.plotly_chart(
        fig,
        height=500,
        width='stretch',
        use_container_width=True
    )


def content_daily_ride_distance_distribution(target: DeltaGenerator):
    data = db.get_daily_total_ride_distance()
    df = pd.DataFrame(
        data,
        columns=["Date","Daily Total Ride Distance"]
    )

    fig = px.scatter(
        df,
        x="Date",
        y="Daily Total Ride Distance",
        color="Date",
    )

    target.plotly_chart(
        fig,
        height=500,
        width='stretch',
        use_container_width=True
    )

    with target.expander(label="Show Raw Data") as exp:
        exp.dataframe(
            df,
            hide_index=True,
            width='stretch',
            use_container_width=True
        )


def section_revenue():
    st.title("Revenue", text_alignment="center")

    tab1, tab2, tab3 = st.tabs(
        tabs=[
            "Revenue by Payment Method", 
            "Top 5 Customers by Total Booking Value", 
            "Daily Ride Distance Distribution"
        ],
        default="Revenue by Payment Method"
    )


    # revenue by payment method
    content_revenue_by_payment_method(tab1)

    # top 5 customer by total booking value
    content_top_5_customer_by_booking_value(tab2)

    # daily ride distance distribution
    content_daily_ride_distance_distribution(tab3)



