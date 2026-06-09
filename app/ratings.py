from streamlit.delta_generator import DeltaGenerator
import streamlit as st 
import database as db
import pandas as pd
import plotly.express as px


def _rating_cards(data: list, title: str, rating_index: int):
    """Reusable component that displays average ratings per vehicle type.

    Args:
        data: Rows from get_vehicle_ratings() — each row is
              (vehicle_type, vehicle_image, avg_customer_rating, avg_driver_rating).
        title: Section subheader text.
        rating_index: Column index of the rating to display (2 = customer, 3 = driver).
    """
    st.subheader(title)

    cols = st.columns(len(data), border=True, gap='xxsmall')

    for index, row in enumerate(data):
        col = cols[index]
        col.image(row[1])
        col.write(row[0])
        col.subheader(f"{row[rating_index]}")


def section_ratings():
    st.title("Ratings", text_alignment="center")

    data = db.get_vehicle_ratings()

    # customer ratings
    _rating_cards(data, "Average Customer Ratings", rating_index=2)

    # driver ratings
    _rating_cards(data, "Average Driver Ratings", rating_index=3)