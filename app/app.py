
from streamlit import sidebar
from ratings import section_ratings
from cancellation import section_cancellation
from revenue import section_revenue
from vehicle_type import section_vehicle_type
from overall import section_overall
from embedded_tableau import section_embedded_tableau
from typing import Callable
import streamlit as st


class SidebarOptionData:

    def __init__(self,label: str,show_content: Callable[[],None]):
        self.label = label
        self.show_content = show_content

sidebar_options = [
    SidebarOptionData("Overall",section_overall),
    SidebarOptionData("Vehicle Type", section_vehicle_type),
    SidebarOptionData("Revenue", section_revenue),
    SidebarOptionData("Cancellation",section_cancellation),
    SidebarOptionData("Ratings",section_ratings),
    SidebarOptionData("Embedded Tableau", section_embedded_tableau)
]

def place_sidebar():
    sidebar = st.sidebar

    if "selected_option" not in st.session_state:
        st.session_state.selected_option = 0

    for index, option in enumerate(sidebar_options):
        if sidebar.button(
            label=option.label,
            width='stretch',
            use_container_width=True,
        ):
            st.session_state.selected_option = index
    
    
    sidebar_options[st.session_state.selected_option].show_content()


def main():
    st.set_page_config(layout="wide")

    place_sidebar()  


if __name__ == "__main__":
    main()