import streamlit as st
import streamlit.components.v1 as components

TABLEAU_URL = "https://public.tableau.com/views/OLARideStory/OLARideStory?:embed=yes&:showVizHome=no&:display_count=no"

def section_embedded_tableau():
    st.header("Embedded Tableau",text_alignment="center")
    
    components.iframe(TABLEAU_URL, width=1200, height=900, scrolling=False)