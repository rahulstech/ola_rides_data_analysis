import streamlit as st
import streamlit.components.v1 as components

TABS = {
    "Overview": "https://public.tableau.com/views/ola_rides_tableau_visualization/Overview?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link&:showVizHome=no&:embed=true",
    "Booking Demand Analysis": "https://public.tableau.com/views/ola_rides_tableau_visualization/BookingDemandAnalysis?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link&:showVizHome=no&:embed=true",
    "Cancellation Analysis": "https://public.tableau.com/views/ola_rides_tableau_visualization/CancellationAnalysis?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link&:showVizHome=no&:embed=true",
    "Rating and Revenue": "https://public.tableau.com/views/ola_rides_tableau_visualization/RatingandRevenue?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link&:showVizHome=no&:embed=true",
}


def section_embedded_tableau():
    st.header("Embedded Tableau", text_alignment="center")

    tabs = st.tabs(list(TABS.keys()))

    for tab, (name, url) in zip(tabs, TABS.items()):
        with tab:
            components.iframe(url, width=1200, height=900, scrolling=False)
