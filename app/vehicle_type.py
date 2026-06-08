from database import get_top_5_vehicle_by_ride_distance
import streamlit as st 
import pandas as pd




def section_vehicle_type():

    # section title
    st.title("Vehicle Type", text_alignment='center')

    # get data
    data = get_top_5_vehicle_by_ride_distance()
    
    df = pd.DataFrame(
        data,
        columns=["Vehicle Type", "Avg Ride Distance"]
    )
    

    # show bar chart
    st.write("Following bar chart displays the top 5 vehicle types by average ride distance")
    
    st.bar_chart(
        data=df,
        x = "Vehicle Type",
        y = "Avg Ride Distance",
        width='stretch',
        color="Vehicle Type",
        use_container_width=True
    )


