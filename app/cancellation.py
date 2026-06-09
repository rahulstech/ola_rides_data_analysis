from database import get_driver_cancellation_reasons
from database import get_customer_cancellation_reasons
from streamlit.elements.lib.mutable_tab_container import TabContainer
import streamlit as st 
import pandas as pd 
import plotly.express as px

def tab_content_canceled_by_customer(tab: TabContainer): 
    data = get_customer_cancellation_reasons()

    df = pd.DataFrame(
        data,
        columns=["Cancellation Reason", "Booking Count"]
    )

    fig = px.bar(
        df,
        x="Cancellation Reason",
        y="Booking Count",
        color="Cancellation Reason",
    )

    tab.plotly_chart(
        fig,
        width='stretch',
        height=500,
        use_container_width=True
    )


def tab_content_canceled_by_driver(tab: TabContainer): 
    data = get_driver_cancellation_reasons()

    df = pd.DataFrame(
        data,
        columns=["Cancellation Reason", "Booking Count"]
    )

    fig = px.bar(
        df,
        x="Booking Count",
        y="Cancellation Reason",
        color="Cancellation Reason",
        orientation="h",
    )

    tab.plotly_chart(
        fig,
        width='stretch',
        height=500,
        use_container_width=True
    )


def section_cancellation():
    st.title("Cancellation", text_alignment='center')

    tab1, tab2 = st.tabs(
        tabs=["Canceled by Customer", "Canceled by Driver"], 
    )

    tab_content_canceled_by_customer(tab1)

    tab_content_canceled_by_driver(tab2)

