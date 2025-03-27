import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="Heat Alert Dashboard", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .stAlert {
        background-color: #f8d7da;
        border-color: #f5c6cb;
        color: #721c24;
        padding: 1rem;
        border-radius: 0.25rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
        margin-bottom: 1rem;
        color: #000000;
    }
    .critical {
        color: #dc3545;
    }
    .warning {
        color: #ffc107;
    }
    .metric-value {
        color: #000000;
    }
    .activity-time {
        color: #666666;
    }
    .activity-event {
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

# Main layout
col1, col2 = st.columns([2, 1])

with col1:
    # Heat Alert Camera Section
    st.markdown("## 🔥 Heat Alert Camera")
    # Placeholder for camera feed
    st.image("https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&q=80&w=2070", 
             caption="Live Thermal Feed")
    
    # Heat Alert Map Section
    st.markdown("## 📍 Heat Alert Map")
    
    # Create a simple map using plotly
    fig = go.Figure(go.Scattermapbox(
        lat=[40.7128, 40.7228],
        lon=[-74.0060, -74.0160],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=14,
            color='red',
            opacity=0.7
        ),
        text=["Alert Zone B", "Alert Zone A"],
    ))

    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox=dict(
            center=dict(lat=40.7128, lon=-74.0060),
            zoom=12
        ),
        margin={"r":0,"t":0,"l":0,"b":0},
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Alert Details Section
    st.markdown("## ℹ️ Alert Details")
    
    with st.container():
        st.markdown("""
        <div class="metric-card">
            <p><strong>Status:</strong> <span class="critical">Active</span></p>
            <p><strong>Location:</strong> <span class="metric-value">Zone B, Sector 4</span></p>
            <p><strong>Detected at:</strong> <span class="metric-value">14:32:18 PM</span></p>
            <p><strong>Crowd Density:</strong> <span class="critical">High (82%)</span></p>
            <p><strong>Temperature:</strong> <span class="critical">36.8°C</span></p>
            <p><strong>Humidity:</strong> <span class="warning">76%</span></p>
            <p><strong>Severity:</strong> <span class="critical">Critical</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Recent Activity Section
    st.markdown("## 🔔 Recent Activity")
    
    activities = [
        {"time": "14:32:18", "event": "High density detected in Zone B"},
        {"time": "14:31:45", "event": "Security team dispatched"},
        {"time": "14:30:22", "event": "High density detected in Zone B"},
        {"time": "14:29:15", "event": "High density detected in Zone B"}
    ]
    
    for activity in activities:
        st.markdown(f"""
        <div class="metric-card">
            <small class="activity-time">{activity['time']}</small><br>
            <span class="activity-event">{activity['event']}</span>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
---
<div style="text-align: center; color: #666;">
    © 2025 CrowdSense. All rights reserved.
</div>
""", unsafe_allow_html=True)