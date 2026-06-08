
from ratings import section_ratings
from cancellation import section_cancellation
from revenue import section_revenue
from vehicle_type import section_vehicle_type
from overall import section_overall
from streamlit.delta_generator import DeltaGenerator
from typing import Callable
import streamlit as st


class SidebarOptionData:

    def __init__(self,label: str,on_click: Callable[[],None]):
        self.label = label
        self.on_click = on_click



def place_sidebar(sidebar: DeltaGenerator):
    sidebar_options = [
        SidebarOptionData("Overall",section_overall),
        SidebarOptionData("Vehicle Type", section_vehicle_type),
        SidebarOptionData("Revenue", section_revenue),
        SidebarOptionData("Cancellation",section_cancellation),
        SidebarOptionData("Ratings",section_ratings)
    ]

    for option in sidebar_options:
        if sidebar.button(label=option.label,use_container_width=True):
            option.on_click()


def main():
    sidebar = st.sidebar

    place_sidebar(sidebar)  

if __name__ == "__main__":
    main()