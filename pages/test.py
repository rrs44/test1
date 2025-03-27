import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Live Camera Monitoring",
    page_icon="🎥",
    layout="wide",
)

# --- CSS Styling ---
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6; /* Light gray background */
        color: #333; /* Dark text */
        font-family: sans-serif;
    }
    .st-bb {
        background-color: #e8e8e8; /* Light gray for cards */
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
    }
    .st-bb h3 {
        color: #007bff; /* Blue for titles */
    }
    .density-high {
        background-color: #f8d7da; /* Light red */
        color: #721c24; /* Dark red */
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    .density-medium {
        background-color: #fff3cd; /* Light yellow */
        color: #856404; /* Dark yellow */
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    .density-normal {
        background-color: #d4edda; /* Light green */
        color: #155724; /* Dark green */
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    .density-text {
        font-size: 1.2em;
        font-weight: bold;
    }
    .change-positive {
        color: green;
        font-weight: bold;
    }
    .change-negative {
        color: red;
        font-weight: bold;
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        color: #777;
        font-size: 0.8em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header ---
st.title("Live Camera Monitoring")

# --- Main Content Layout ---
col1, col2, col3 = st.columns(3)

# --- Left Column (Main Entrance - Live Feed) ---
with col1:
    st.markdown('<div class="st-bb">', unsafe_allow_html=True)
    st.subheader("Main Entrance - Live Feed")
    st.markdown("🔴 Recording")
    st.image("placeholder_image.png", use_column_width=True, caption="Camera Feed Placeholder") # Replace "placeholder_image.png" with your image URL
    st.markdown('</div>', unsafe_allow_html=True)

# --- Middle Column (Main Entrance - Live Feed x3) ---
with col2:
    for _ in range(3):
        st.markdown('<div class="st-bb">', unsafe_allow_html=True)
        st.subheader("Main Entrance - Live Feed")
        st.image("placeholder_image.png", use_column_width=True, caption="Camera Feed Placeholder") # Replace "placeholder_image.png" with your image URL
        st.markdown('</div>', unsafe_allow_html=True)

# --- Right Column (Zone Details) ---
with col3:
    st.markdown('<div class="st-bb">', unsafe_allow_html=True)
    st.subheader("Zone Details")
    
    # Zone 1
    st.markdown("<h4>Zone 1 - Entrance Lobby</h4>", unsafe_allow_html=True)
    st.markdown('<span class="density-high">High Density</span>', unsafe_allow_html=True)
    st.markdown("People Count: 78")
    st.markdown('<span class="density-text">Density: 85%</span>', unsafe_allow_html=True)
    
    # Zone 2
    st.markdown("<h4>Zone 2 - Waiting Area</h4>", unsafe_allow_html=True)
    st.markdown('<span class="density-medium">Medium Density</span>', unsafe_allow_html=True)
    st.markdown("People Count: 42")
    st.markdown('<span class="density-text">Density: 57%</span>', unsafe_allow_html=True)
    
    # Zone 3
    st.markdown("<h4>Zone 3 - Information Desk</h4>", unsafe_allow_html=True)
    st.markdown('<span class="density-normal">Normal</span>', unsafe_allow_html=True)
    st.markdown("People Count: 15")
    st.markdown('<span class="density-text">Density: 28%</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Crowd Density Summary ---
st.subheader("Crowd Density Summary")
col4, col5, col6, col7 = st.columns(4)

with col4:
    st.markdown('<div class="st-bb">', unsafe_allow_html=True)
    st.markdown('<span class="density-text">85%</span>', unsafe_allow_html=True)
    st.markdown('<span class="change-positive">↑ 12% from yesterday</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col5:
    st.markdown('<div class="st-bb">', unsafe_allow_html=True)
    st.markdown('<span class="density-text">57%</span>', unsafe_allow_html=True)
    st.markdown('<span class="change-positive">↑ 5% from yesterday</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="st-bb">', unsafe_allow_html=True)
    st.markdown('<span class="density-text">28%</span>', unsafe_allow_html=True)
    st.markdown('<span class="change-negative">↓ 3% from yesterday</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col7:
    st.markdown('<div class="st-bb">', unsafe_allow_html=True)
    st.markdown('<span class="density-text">42%</span>', unsafe_allow_html=True)
    st.markdown('<span class="change-positive">↑ 7% from yesterday</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    <p>© 2025 CrowdSense. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)