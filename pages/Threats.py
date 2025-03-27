import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import base64
import os

# Page configuration
st.set_page_config(page_title="CrowdSense - Threat Analysis", layout="wide")

# Custom CSS to match the dark theme
st.markdown("""
<style>
    .camera-feed {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
        margin-bottom: 1rem;
        color: #000000;
    }
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
    .metric-card {
        background-color: #1E2130;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        color: white;
    }
    .high-risk { color: #f43f5e; }
    .medium-risk { color: #f97316; }
    .low-risk { color: #10b981; }
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

# Threat Overview Data
threat_overview = {
    'high_threats': 12,
    'high_change': 5,
    'medium_threats': 37,
    'medium_change': -2,
    'resolved_threats': 85,
    'resolved_change': 3,
    'avg_response_time': 14
}

# Main layout
st.markdown("# 🛡️ Threat Analysis")
st.markdown("Monitor and analyze potential threats to public safety")

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the video file
video_path = os.path.join(current_dir, "videosense.mp4")

# Main layout
col1, col2 = st.columns([2, 1])
with open(video_path, "rb") as video_file:
    video_bytes = video_file.read()
video_encoded = base64.b64encode(video_bytes).decode('utf-8')

with col1:
    # Main Camera Section
    st.markdown("## 📹 Live Camera Monitoring")
    
    # Correctly insert the video inside the div with base64 encoding
    st.markdown(f"""
    <div class="camera-feed">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <strong>Main Entrance - Live Feed</strong>
            <span class="recording-indicator">● Recording</span>
        </div>
        <video width="100%" autoplay loop muted style="border-radius: 8px;">
            <source src="data:video/mp4;base64,{video_encoded}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    """, unsafe_allow_html=True)

# Metrics Row
cols = st.columns(4)

metrics = [
    ("High Threats", threat_overview['high_threats'], threat_overview['high_change'], "high-risk"),
    ("Medium Threats", threat_overview['medium_threats'], threat_overview['medium_change'], "medium-risk"),
    ("Resolved", threat_overview['resolved_threats'], threat_overview['resolved_change'], "low-risk"),
    ("Avg Response", threat_overview['avg_response_time'],threat_overview['resolved_change'], "low-risk")
]

for col, (label, value, change, style_class) in zip(cols, metrics):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <p style="margin: 0; color: #8f9cb3;">{label}</p>
                    <h2 class="{style_class}">{value}</h2>
                </div>
                {f'<span style="color: {"#f43f5e" if change and change > 0 else "#10b981"};">{"↑" if change and change > 0 else "↓"} {abs(change)}%</span>' if change is not None else ''}
            </div>
        </div>
        """, unsafe_allow_html=True)

# Threat Distribution and Categories
dist_cols = st.columns(2)

with dist_cols[0]:
    st.markdown("## Threat Distribution")
    # Pie chart for threat distribution
    threat_dist_data = pd.DataFrame({
        'Category': ['High Risk', 'Medium Risk', 'Low Risk'],
        'Count': [12, 37, 85]
    })
    
    fig_dist = px.pie(threat_dist_data, values='Count', names='Category', 
                      color='Category',
                      color_discrete_map={
                          'High Risk': '#f43f5e', 
                          'Medium Risk': '#f97316', 
                          'Low Risk': '#10b981'
                      })
    fig_dist.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', 
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    st.plotly_chart(fig_dist, use_container_width=True)

with dist_cols[1]:
    st.markdown("## Threat Categories")
    # Bar chart for threat categories
    threat_cat_data = pd.DataFrame({
        'Category': ['Fire Hazards', 'Flooding', 'Health Risks', 'Power Failures', 'Weather Events'],
        'Percentage': [85, 62, 45, 38, 27]
    })
    
    fig_cat = px.bar(threat_cat_data, x='Category', y='Percentage', 
                     color='Category',
                     color_discrete_map={
                         'Fire Hazards': '#f43f5e', 
                         'Flooding': '#3b82f6', 
                         'Health Risks': '#10b981',
                         'Power Failures': '#f97316',
                         'Weather Events': '#8b5cf6'
                     })
    fig_cat.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', 
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        xaxis_title='',
        yaxis_title=''
    )
    st.plotly_chart(fig_cat, use_container_width=True)

# Recent Threats Table
st.markdown("## Recent Threats")

# Create DataFrame for recent threats
recent_threats_data = pd.DataFrame([
    {
        'ID': '#TH-2542', 
        'Threat': 'Wildfire Risk', 
        'Location': 'North District', 
        'Severity': 'High', 
        'Reported': '5 hours ago', 
        'Status': 'Active'
    },
    {
        'ID': '#TH-2541', 
        'Threat': 'Flash Flood', 
        'Location': 'West District', 
        'Severity': 'Medium', 
        'Reported': '8 hours ago', 
        'Status': 'Monitoring'
    },
    {
        'ID': '#TH-2540', 
        'Threat': 'Virus Outbreak', 
        'Location': 'Central District', 
        'Severity': 'Medium', 
        'Reported': '12 hours ago', 
        'Status': 'Active'
    },
    {
        'ID': '#TH-2539', 
        'Threat': 'Power Outage', 
        'Location': 'South District', 
        'Severity': 'Low', 
        'Reported': '1 day ago', 
        'Status': 'Resolved'
    },
    {
        'ID': '#TH-2538', 
        'Threat': 'Severe Weather', 
        'Location': 'All Districts', 
        'Severity': 'Medium', 
        'Reported': '1 day ago', 
        'Status': 'Monitoring'
    }
])

# Style the DataFrame
def style_threats(df):
    # Color mapping for severity and status
    def color_severity(val):
        color_map = {
            'High': '#f43f5e',
            'Medium': '#f97316',
            'Low': '#10b981'
        }
        return f'color: {color_map.get(val, "white")}'
    
    def color_status(val):
        color_map = {
            'Active': '#f43f5e', 
            'Monitoring': '#f97316', 
            'Resolved': '#10b981'
        }
        return f'color: {color_map.get(val, "white")}'
    
    styled_df = df.style\
        .applymap(color_severity, subset=['Severity'])\
        .applymap(color_status, subset=['Status'])
    
    return styled_df

# Display the styled DataFrame
st.dataframe(style_threats(recent_threats_data), use_container_width=True)

# Sound Detection Data
sound_data = pd.DataFrame({
    'Time': pd.date_range(start='2025-03-28 10:00:00', periods=50, freq='1min'),
    'Sound Intensity': np.concatenate([
        np.random.normal(50, 10, 10),  # baseline noise
        np.random.normal(80, 15, 15),  # sudden spike
        np.random.normal(60, 12, 10),  # return to baseline
        np.random.normal(90, 20, 5),   # high intensity event
        np.random.normal(55, 8, 10)    # stabilizing
    ])
})

# Create line graph for sound detection
fig_sound = go.Figure()
fig_sound.add_trace(go.Scatter(
    x=sound_data['Time'], 
    y=sound_data['Sound Intensity'], 
    mode='lines', 
    line=dict(color='#3b82f6', width=3),
    fill='tozeroy',
    fillcolor='rgba(59, 130, 246, 0.3)'
))

fig_sound.update_layout(
    title='Sound Intensity Detection',
    xaxis_title='Time',
    yaxis_title='Sound Intensity (dB)',
    plot_bgcolor='rgba(0,0,0,0)', 
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='white',
    height=300
)

# Replace the placeholder in the original script
st.markdown("## Threat Sound Detection")
st.plotly_chart(fig_sound, use_container_width=True)

# Footer
st.markdown("""
---
<div style="text-align: center; color: #8f9cb3;">
    © 2025 CrowdSense. All rights reserved.
</div>
""", unsafe_allow_html=True)