from database import get_driver_cancellation_reasons
from database import get_customer_cancellation_reasons
from streamlit.elements.lib.mutable_tab_container import TabContainer
import streamlit as st 
import pandas as pd 

def tab_content_canceled_by_customer(tab: TabContainer): 
    data = get_customer_cancellation_reasons()

    df = pd.DataFrame(
        data,
        columns=["Cancellation Reason", "Booking Count"]
    )

    tab.bar_chart(
        data=df,
        x="Cancellation Reason",
        y="Booking Count",
        horizontal=True,
        color='Cancellation Reason',
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

    tab.bar_chart(
        data=df,
        x="Cancellation Reason",
        y="Booking Count",
        horizontal=True,
        color='Cancellation Reason',
        width='stretch',
        height=500,
        use_container_width=True
    )


def section_cancellation():
    st.title("Cancellation", text_alignment='center')

    tab_canceled_by_customer, tab_canceled_by_driver = st.tabs(
        tabs=["Canceled by Customer", "Canceled by Driver"], 
        default="Canceled by Customer",
    )

    tab_content_canceled_by_customer(tab_canceled_by_customer)

    tab_content_canceled_by_driver(tab_canceled_by_driver)

