import database as db
import streamlit as st 


def section_vehicle_type():

    # section title
    st.title("Vehicle Type", text_alignment='center')

    # get data
    data = db.get_vehicle_ride_data()

    # column headers
    headers = ["Vehicle Type", "Total Booking Value", "Success Booking Value",
               "Avg. Distance Travelled", "Total Distance Travelled"]

    # header row
    header_cols = st.columns([2, 2, 2, 2, 2])
    for col, header in zip(header_cols, headers):
        col.markdown(f"**{header}**")

    # data rows
    for row in data:
        vehicle_type = row[0]
        vehicle_image = row[1]
        total_booking_count = row[2]
        total_success_booking_count = row[3]
        total_complete_ride_count = row[4]
        total_complete_ride_distance = row[5]

        avg_distance = round(total_complete_ride_distance / total_complete_ride_count, 2) if total_complete_ride_count else 0

        cols = st.columns([2, 2, 2, 2, 2], border=True, gap=None, )

        # vehicle type column with image
        cols[0].image(vehicle_image, width=50)
        cols[0].write(vehicle_type)

        # data columns
        cols[1].write(f"{total_booking_count:,}")
        cols[2].write(f"{total_success_booking_count:,}")
        cols[3].write(f"{avg_distance:,}")
        cols[4].write(f"{total_complete_ride_distance:,}")