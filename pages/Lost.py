import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="CrowdSense - Lost Persons", layout="wide")

# Custom CSS for dark theme
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
        background-color: white;
        border-radius: 8px;
        color: #8f9cb3;
    }
    .stTabs [data-baseweb="tab"][data-selected="true"] {
        background-color: #3b82f6;
        color: black;
    }
    .sidebar .sidebar-content {
        background-color: white;
    }
    .stMarkdown {
        color: white;
    }
    .case-details{
        color: black
    }
    .case-card {
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        color: black;
    }
    .status-tag {
        border-radius: 4px;
        padding: 2px 8px;
        font-size: 0.8em;
    }
    .active { background-color: #10b981; color: white; }
    .urgent { background-color: #f43f5e; color: white; }
    .resolved { background-color: #8f9cb3; color: white; }
</style>
""", unsafe_allow_html=True)

# Sample Lost Persons Data
def get_lost_persons_data():
    return [
        {
            "name": "Sarah Johnson",
            "age": 27,
            "location": "Central Park, NYC",
            "last_seen": datetime(2025, 3, 20),
            "case_id": "LP-2025-1034",
            "status": "Urgent",
            "description": "Last seen wearing a red jacket, blue jeans, and white sneakers. Has a small butterfly tattoo on right wrist and carrying a black backpack."
        },
        {
            "name": "Michael Chen",
            "age": 32,
            "location": "Downtown Seattle",
            "last_seen": datetime(2025, 3, 15),
            "case_id": "LP-2025-1028",
            "status": "Active",
            "description": "Marketing professional, last seen near TechCorp offices."
        },
        {
            "name": "Emma Rodriguez",
            "age": 19,
            "location": "Miami Beach",
            "last_seen": datetime(2025, 3, 10),
            "case_id": "LP-2025-1023",
            "status": "Resolved",
            "description": "College student, was reported missing during spring break."
        },
        {
            "name": "David Wilson",
            "age": 41,
            "location": "Lincoln Park, Chicago",
            "last_seen": datetime(2025, 3, 5),
            "case_id": "LP-2025-1020",
            "status": "Active",
            "description": "Business consultant, last seen near local coffee shop."
        }
    ]

# Main Page
st.markdown("# 🔍 Lost Persons")
st.markdown("Track and manage missing person reports and investigations")

# Search and Filter Row
col1, col2, col3, col4, col5 = st.columns([4, 1, 1, 1, 1])

with col1:
    search_term = st.text_input("🔍 Search by name, location, or case ID")

with col2:
    st.write("Filter:")

with col3:
    all_btn = st.button("All")

with col4:
    urgent_btn = st.button("Urgent")

with col5:
    new_case_btn = st.button("+ New Case")

# Fetch and filter data
lost_persons = get_lost_persons_data()

# Display Lost Persons
st.markdown("## Current Cases")

# Selected case details
selected_case = None

# Case List and Details
cols = st.columns([1, 2])

with cols[0]:
    # Case List
    for person in lost_persons:
        status_class = person['status'].lower()
        st.markdown(f"""
        <div class="case-card" onclick="window.location.href='#case-{person['case_id']}'">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h3 style="margin: 0;">{person['name']}</h3>
                    <p style="margin: 0; color: #8f9cb3;">{person['location']}</p>
                </div>
                <span class="status-tag {status_class}">{person['status']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Replace the current detailed case view section with:
with cols[1]:
    # Detailed Case View (defaulting to first case)
    case = lost_persons[0]
    st.markdown(f"""
    <div class="case-details" style="background-color: white; border-radius: 8px; padding: 20px;">
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <img src="/api/placeholder/100/100" alt="{case['name']}" style="border-radius: 50%; margin-right: 20px; width: 100px; height: 100px;"/>
            <div>
                <h2 style="margin: 0;">{case['name']}</h2>
                <p style="margin: 0; color: #8f9cb3;">Female, {case['age']} years old</p>
                <p style="margin: 0; color: #8f9cb3;">Last seen: {case['last_seen'].strftime('%B %d, %Y')}</p>
            </div>
        </div>
        <div style="margin-bottom: 20px;">
            <h3>Case Details</h3>
            <p><strong>Case ID:</strong> {case['case_id']}</p>
            <p><strong>Description:</strong> {case['description']}</p>
        </div>
        <div style="display: flex; gap: 10px;">
            <button style="background-color: #3b82f6; color: white; border: none; padding: 10px 20px; border-radius: 5px;">Send Alert</button>
            <button style="background-color: #10b981; color: white; border: none; padding: 10px 20px; border-radius: 5px;">Update Case</button>
        </div>
        <div style="margin-top: 20px;">
            <h3>Case Timeline</h3>
            <ul style="list-style-type: none; padding: 0;">
                <li>• Case Opened: March 21, 2025 - 10:30 AM</li>
                <li>• Last Phone Activity: March 23, 2025 - 4:17 PM</li>
                <li>• Possible Sighting: March 20, 2025 - 5:30 PM</li>
                <li>• Alert Distributed: March 21, 2025 - 12:45 PM</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
# Footer
st.markdown("""
---
<div style="text-align: center; color: #8f9cb3;">
    © 2025 CrowdSense. All rights reserved.
</div>
""", unsafe_allow_html=True)