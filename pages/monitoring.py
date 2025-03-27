import streamlit as st
import random

# Page configuration
st.set_page_config(page_title="Crowd Monitoring Dashboard", layout="wide")

# Initialize demo data in session state if not exists
if 'zone_data' not in st.session_state:
    st.session_state.zone_data = {
        'zone1': {'count': 78, 'density': 85, 'change': 12},
        'zone2': {'count': 42, 'density': 57, 'change': 5},
        'zone3': {'count': 15, 'density': 28, 'change': -3},
        'zone4': {'count': 35, 'density': 42, 'change': 7}
    }

def update_demo_data():
    for zone in st.session_state.zone_data:
        st.session_state.zone_data[zone]['count'] += random.randint(-5, 5)
        st.session_state.zone_data[zone]['density'] += random.randint(-3, 3)
        st.session_state.zone_data[zone]['density'] = max(0, min(100, st.session_state.zone_data[zone]['density']))

# Custom CSS
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
    .density-badge {
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 14px;
        font-weight: 500;
    }
    .density-high {
        background-color: #f8d7da;
        color: #dc3545;
    }
    .density-medium {
        background-color: #fff3e0;
        color: #ffc107;
    }
    .density-normal {
        background-color: #e8f5e9;
        color: #28a745;
    }
    .metric-card {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
        margin-bottom: 1rem;
        color: #000000;
    }
    .recording-indicator {
        color: #dc3545;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Main layout
col1, col2 = st.columns([2, 1])

with col1:
    # Main Camera Section
    st.markdown("## 📹 Live Camera Monitoring")
    
    # Camera Feed
    st.markdown("""
    <div class="camera-feed">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <strong>Main Entrance - Live Feed</strong>
            <span class="recording-indicator">● Recording</span>
        </div>
        <img src='https://via.placeholder.com/800x400' style='width: 100%; height: auto; border-radius: 0.5rem;'>
    </div>
    """, unsafe_allow_html=True)
    
    # Density Metrics
    st.markdown("## 📊 Crowd Density")
    metrics_cols = st.columns(4)
    for i, (zone, data) in enumerate(st.session_state.zone_data.items()):
        with metrics_cols[i]:
            st.markdown(f"""
            <div class="metric-card" style="text-align: center;">
                <h4 style="margin-bottom: 10px;">Zone {i+1}</h4>
                <h2 style="margin: 5px 0;">{data['density']}%</h2>
                <p style="color: {'#dc3545' if data['change'] > 0 else '#28a745'}; margin: 5px 0;">
                    {"↑" if data["change"] > 0 else "↓"} {abs(data["change"])}% from yesterday
                </p>
            </div>
            """, unsafe_allow_html=True)

with col2:
    # Zone Details Section
    st.markdown("## 🏢 Zone Details")
    
    zones = [
        ("Zone 1 - Entrance Lobby", "high"),
        ("Zone 2 - Waiting Area", "medium"),
        ("Zone 3 - Information Desk", "normal")
    ]
    
    for i, (zone_name, density_level) in enumerate(zones):
        zone_data = st.session_state.zone_data[f'zone{i+1}']
        density_class = {
            "high": "density-high",
            "medium": "density-medium",
            "normal": "density-normal"
        }[density_level]
        
        st.markdown(f"""
        <div class="metric-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <strong>{zone_name}</strong>
                <span class="density-badge {density_class}">{density_level.title()}</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <div>
                    <p style="margin: 0; color: #666;">People Count</p>
                    <h3 style="margin: 5px 0;">{zone_data['count']}</h3>
                </div>
                <div>
                    <p style="margin: 0; color: #666;">Density</p>
                    <h3 style="margin: 5px 0;">{zone_data['density']}%</h3>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Update button for demo
    if st.button("Update Data (Demo)"):
        update_demo_data()
        st.experimental_rerun()

# Footer
st.markdown("""
---
<div style="text-align: center; color: #666;">
    © 2025 CrowdSense. All rights reserved.
</div>
""", unsafe_allow_html=True)
