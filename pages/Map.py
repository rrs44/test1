import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import numpy as np
import random

# Page configuration
st.set_page_config(page_title="CrowdSense - Map", layout="wide")

# Custom CSS to match the dark theme
st.markdown("""
<style>
    .stApp {
        color: white;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 15px;
        background-color: #1E2130;
        border-radius: 8px;
        color: #8f9cb3;
    }
    .stTabs [data-baseweb="tab"][data-selected="true"] {
        background-color: #3b82f6;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #1E2130;
    }
    .stSelectbox, .stRadio, .stSlider {
        color: white;
    }
    .stSelectbox div, .stRadio div, .stSlider div {
        background-color: #1E2130 !important;
        color: white !important;
    }
    .stMarkdown {
        color: white;
    }
    .map-legend {
        background-color: #1E2130;
        border-radius: 8px;
        padding: 15px;
        color: white;
    }
    .stDataFrame {
        background-color: #1E2130 !important;
        color: white !important;
    }
    .stDataFrame th {
        background-color: #2D3748 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Function to generate realistic crowd data
def generate_crowd_data(crowd_type, time_range):
    # London area coordinates with some variation
    base_locations = {
        'Downtown': [51.5074, -0.1278],
        'West End': [51.5138, -0.1337],
        'East End': [51.5222, -0.0756],
        'South Bank': [51.5064, -0.1119],
        'City of London': [51.5155, -0.0922]
    }
    
    # Generate data based on crowd type and time range
    data = []
    for location, coords in base_locations.items():
        # Vary number of people based on crowd type and time range
        base_people = {
            'All Crowds': 100,
            'Commuters': 200,
            'Tourists': 150,
            'Residents': 50
        }
        
        time_multiplier = {
            'Live': 1,
            'Last Hour': 0.8,
            'Last 24 Hours': 0.5,
            'Last Week': 0.2
        }
        
        num_people = int(base_people.get(crowd_type, 100) * time_multiplier.get(time_range, 1))
        
        for _ in range(num_people):
            # Add some random variation to coordinates
            lat = coords[0] + random.uniform(-0.02, 0.02)
            lon = coords[1] + random.uniform(-0.02, 0.02)
            
            # Determine density based on location and crowd type
            if location in ['City of London', 'Downtown']:
                density = 'High'
            elif location in ['West End', 'South Bank']:
                density = 'Medium'
            else:
                density = 'Low'
            
            data.append({
                'Location': location,
                'Latitude': lat,
                'Longitude': lon,
                'Density': density,
                'Crowd Type': crowd_type
            })
    
    return pd.DataFrame(data)

# Sidebar for Map Controls
st.sidebar.title("🗺️ Map Controls")

# Crowd Type Selector
crowd_type = st.sidebar.selectbox(
    "Crowd Type",
    ["All Crowds", "Commuters", "Tourists", "Residents"]
)

# Time Range Selector
time_range = st.sidebar.selectbox(
    "Time Range",
    ["Live", "Last Hour", "Last 24 Hours", "Last Week"]
)

# Density Level Slider
density_level = st.sidebar.slider(
    "Density Level", 
    min_value=0, 
    max_value=100, 
    value=50
)

# Quick Location Buttons
st.sidebar.markdown("## Quick Location")
location_cols = st.sidebar.columns(2)
with location_cols[0]:
    downtown_btn = st.sidebar.button("🏙️ Downtown")
with location_cols[1]:
    station_btn = st.sidebar.button("🚉 Station")

# Main Page Title
st.markdown("# 🗺️ CrowdSense Map")

# Generate crowd data based on selections
crowd_data = generate_crowd_data(crowd_type, time_range)

# Create Folium Map
m = folium.Map(
    location=[51.5074, -0.1278],  # London coordinates
    zoom_start=11,
    tiles='CartoDB dark_matter'  # Dark theme map
)

# Density color mapping
density_colors = {
    'High': 'red',
    'Medium': 'yellow',
    'Low': 'green'
}

# Add density markers
for _, row in crowd_data.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        popup=f"Location: {row['Location']}<br>Density: {row['Density']}<br>Crowd Type: {row['Crowd Type']}",
        color=density_colors[row['Density']],
        fill=True,
        fill_color=density_colors[row['Density']]
    ).add_to(m)

# Display the map
folium_static(m, width=1100, height=600)

# Detailed Data Table
st.markdown("## Crowd Data Details")
st.dataframe(crowd_data)

# Summary Statistics
st.markdown("## Crowd Density Summary")
density_summary = crowd_data.groupby('Density').size().reset_index(name='Count')
density_summary['Percentage'] = (density_summary['Count'] / len(crowd_data) * 100).round(2)

st.dataframe(density_summary)

# Visualization of Density Distribution
import plotly.express as px

fig = px.pie(
    density_summary, 
    values='Count', 
    names='Density', 
    title='Crowd Density Distribution',
    color='Density',
    color_discrete_map={
        'High': '#f43f5e', 
        'Medium': '#f97316', 
        'Low': '#10b981'
    }
)
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)', 
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='white'
)
st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("""
---
<div style="text-align: center; color: #8f9cb3;">
    © 2025 CrowdSense. All rights reserved.
</div>
""", unsafe_allow_html=True)