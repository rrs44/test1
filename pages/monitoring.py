# import streamlit as st
# import random

# # Initialize demo data in session state if not exists
# if 'zone_data' not in st.session_state:
#     st.session_state.zone_data = {
#         'zone1': {'count': 78, 'density': 85, 'change': 12},
#         'zone2': {'count': 42, 'density': 57, 'change': 5},
#         'zone3': {'count': 15, 'density': 28, 'change': -3},
#         'zone4': {'count': 35, 'density': 42, 'change': 7}
#     }

# def update_demo_data():
#     for zone in st.session_state.zone_data:
#         st.session_state.zone_data[zone]['count'] += random.randint(-5, 5)
#         st.session_state.zone_data[zone]['density'] += random.randint(-3, 3)
#         st.session_state.zone_data[zone]['density'] = max(0, min(100, st.session_state.zone_data[zone]['density']))

# # Custom CSS for monitoring page
# st.markdown("""
#     <style>
#         .camera-feed {
#             background-color: #f5f5f5;
#             border-radius: 10px;
#             padding: 20px;
#             margin-bottom: 20px;
#         }
#         .camera-title {
#             background-color: #1f2b4d;
#             color: white;
#             padding: 10px 20px;
#             border-radius: 10px 10px 0 0;
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#         }
#         .recording-dot {
#             color: #ff4444;
#             animation: blink 1s infinite;
#         }
#         .zone-card {
#             background-color: white;
#             border-radius: 10px;
#             padding: 20px;
#             margin-bottom: 15px;
#             box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#         }
#         .density-badge {
#             padding: 5px 10px;
#             border-radius: 15px;
#             font-size: 14px;
#             font-weight: 500;
#         }
#         .density-high {
#             background-color: #ffe5e5;
#             color: #ff4444;
#         }
#         .density-medium {
#             background-color: #fff3e0;
#             color: #ff9800;
#         }
#         .density-normal {
#             background-color: #e8f5e9;
#             color: #4caf50;
#         }
#         .zone-card{
#             color: black;
#             box-shadow: 0px 0px;
#         }
#         @keyframes blink {
#             50% { opacity: 0; }
#         }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("<h1 class='header'>Live Camera Monitoring</h1>", unsafe_allow_html=True)

# # Main layout
# col1, col2 = st.columns([2, 1])

# with col1:
#     # Main camera feed
#     st.markdown("""
#         <div class='camera-feed'>
#             <div class='camera-title'>
#                 <span>Main Entrance - Live Feed</span>
#                 <span class='recording-dot'>● Recording</span>
#             </div>
#             <div style='height: 400px; display: flex; align-items: center; justify-content: center;'>
#                 <img src='https://via.placeholder.com/800x400' style='max-width: 100%; height: auto;'>
#             </div>
#         </div>
#     """, unsafe_allow_html=True)
    
#     # Density metrics
#     metrics_cols = st.columns(4)
#     for i, (zone, data) in enumerate(st.session_state.zone_data.items()):
#         with metrics_cols[i]:
#             st.markdown(f"""
#                 <div style='text-align: center; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
#                     <h3 style='color:black;'>Crowd Density</h3>
#                     <h2 style='color: #1f2b4d; font-size: 36px;'>{data['density']}%</h2>
#                     <p style='color: {"#ff4444" if data["change"] > 0 else "#4caf50"}'>
#                         {"↑" if data["change"] > 0 else "↓"} {abs(data["change"])}% from yesterday
#                     </p>
#                 </div>
#             """, unsafe_allow_html=True)

# with col2:
#     st.markdown("<h3>Zone Details</h3>", unsafe_allow_html=True)
    
#     # Zone cards
#     zones = [
#         ("Zone 1 - Entrance Lobby", "high"),
#         ("Zone 2 - Waiting Area", "medium"),
#         ("Zone 3 - Information Desk", "normal")
#     ]
    
#     for i, (zone_name, density_level) in enumerate(zones):
#         zone_data = st.session_state.zone_data[f'zone{i+1}']
#         density_class = {
#             "high": "density-high",
#             "medium": "density-medium",
#             "normal": "density-normal"
#         }[density_level]
        
#         st.markdown(f"""
#             <div class='zone-card'>
#                 <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 15px;'>
#                     <h4 style='margin: 0;' class='zone-card'>{zone_name}</h4>
#                     <span class='density-badge {density_class}'>{density_level.title()}</span>
#                 </div>
#                 <div style='display: flex; justify-content: space-between;'>
#                     <div>
#                         <p style='color: #666; margin: 0;'>People Count</p>
#                         <h3 style='margin: 5px 0;'>{zone_data['count']}</h3>
#                     </div>
#                     <div>
#                         <p style='color: #666; margin: 0;'>Density</p>
#                         <h3 style='margin: 5px 0;'>{zone_data['density']}%</h3>
#                     </div>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)
    
#     # Update button for demo
#     if st.button("Update Data (Demo)"):
#         update_demo_data()
#         st.experimental_rerun()





# import streamlit as st
# import random

# # Initialize demo data in session state if not exists
# if 'zone_data' not in st.session_state:
#     st.session_state.zone_data = {
#         'zone1': {'count': 78, 'density': 85, 'change': 12},
#         'zone2': {'count': 42, 'density': 57, 'change': 5},
#         'zone3': {'count': 15, 'density': 28, 'change': -3},
#         'zone4': {'count': 35, 'density': 42, 'change': 7}
#     }

# def update_demo_data():
#     for zone in st.session_state.zone_data:
#         st.session_state.zone_data[zone]['count'] += random.randint(-5, 5)
#         st.session_state.zone_data[zone]['density'] += random.randint(-3, 3)
#         st.session_state.zone_data[zone]['density'] = max(0, min(100, st.session_state.zone_data[zone]['density']))

# # Custom CSS for monitoring page
# st.markdown("""
#     <style>
#         .camera-feed {
#             background-color: #f5f5f5;
#             border-radius: 10px;
#             padding: 20px;
#             margin-bottom: 20px;
#         }
#         .camera-title {
#             background-color: #1f2b4d;
#             color: white;
#             padding: 10px 20px;
#             border-radius: 10px 10px 0 0;
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#         }
#         .recording-dot {
#             color: #ff4444;
#             animation: blink 1s infinite;
#         }
#         .zone-card {
#             background-color: white;
#             border-radius: 10px;
#             padding: 20px;
#             margin-bottom: 15px;
#             box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#         }
#         .density-badge {
#             padding: 5px 10px;
#             border-radius: 15px;
#             font-size: 14px;
#             font-weight: 500;
#         }
#         .density-high {
#             background-color: #ffe5e5;
#             color: #ff4444;
#         }
#         .density-medium {
#             background-color: #fff3e0;
#             color: #ff9800;
#         }
#         .density-normal {
#             background-color: #e8f5e9;
#             color: #4caf50;
#         }
#         .zone-card{
#             color: black;
#             box-shadow: 0px 0px;
#         }
#         @keyframes blink {
#             50% { opacity: 0; }
#         }
#         .stVideo {
#             width: 100%;
#             border-radius: 0 0 10px 10px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("<h1 class='header'>Live Camera Monitoring</h1>", unsafe_allow_html=True)

# # Main layout
# col1, col2 = st.columns([2, 1])

# with col1:
#     # Main camera feed with video
#     st.markdown("""
#         <div class='camera-feed'>
#             <div class='camera-title'>
#                 <span>Main Entrance - Live Feed</span>
#                 <span class='recording-dot'>● Recording</span>
#             </div>
#         </div>
#     """, unsafe_allow_html=True)
    
#     # Video player
#     # try:
#     #     st.video("videosense.mp4")
#     # except Exception as e:
#     #     st.error(f"Error loading video: {str(e)}")
#     #     st.markdown("""
#     #         <div style='height: 400px; display: flex; align-items: center; justify-content: center;'>
#     #             <img src='https://via.placeholder.com/800x400' style='max-width: 100%; height: auto;'>
#     #         </div>
#     #     """, unsafe_allow_html=True)
    

#     # Read the video file in binary mode
# with open("videosense.mp4", "rb") as video_file:
#     video_bytes = video_file.read()

# # Display the video in Streamlit
# if video_bytes:
#     st.video(video_bytes)
# else:
#     st.error("Error: Unable to load the video file.")
#     # Density metrics
#     metrics_cols = st.columns(4)
#     for i, (zone, data) in enumerate(st.session_state.zone_data.items()):
#         with metrics_cols[i]:
#             st.markdown(f"""
#                 <div style='text-align: center; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
#                     <h3 style='color:black;'>Crowd Density</h3>
#                     <h2 style='color: #1f2b4d; font-size: 36px;'>{data['density']}%</h2>
#                     <p style='color: {"#ff4444" if data["change"] > 0 else "#4caf50"}'>
#                         {"↑" if data["change"] > 0 else "↓"} {abs(data["change"])}% from yesterday
#                     </p>
#                 </div>
#             """, unsafe_allow_html=True)

# with col2:
#     st.markdown("<h3>Zone Details</h3>", unsafe_allow_html=True)
    
#     # Zone cards
#     zones = [
#         ("Zone 1 - Entrance Lobby", "high"),
#         ("Zone 2 - Waiting Area", "medium"),
#         ("Zone 3 - Information Desk", "normal")
#     ]
    
#     for i, (zone_name, density_level) in enumerate(zones):
#         zone_data = st.session_state.zone_data[f'zone{i+1}']
#         density_class = {
#             "high": "density-high",
#             "medium": "density-medium",
#             "normal": "density-normal"
#         }[density_level]
        
#         st.markdown(f"""
#             <div class='zone-card'>
#                 <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 15px;'>
#                     <h4 style='margin: 0;' class='zone-card'>{zone_name}</h4>
#                     <span class='density-badge {density_class}'>{density_level.title()}</span>
#                 </div>
#                 <div style='display: flex; justify-content: space-between;'>
#                     <div>
#                         <p style='color: #666; margin: 0;'>People Count</p>
#                         <h3 style='margin: 5px 0;'>{zone_data['count']}</h3>
#                     </div>
#                     <div>
#                         <p style='color: #666; margin: 0;'>Density</p>
#                         <h3 style='margin: 5px 0;'>{zone_data['density']}%</h3>
#                     </div>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)
    
#     # Update button for demo
#     if st.button("Update Data (Demo)"):
#         update_demo_data()
#         st.experimental_rerun()



# import streamlit as st
# import random

# # Initialize demo data in session state if not exists
# if 'zone_data' not in st.session_state:
#     st.session_state.zone_data = {
#         'zone1': {'count': 78, 'density': 85, 'change': 12},
#         'zone2': {'count': 42, 'density': 57, 'change': 5},
#         'zone3': {'count': 15, 'density': 28, 'change': -3},
#         'zone4': {'count': 35, 'density': 42, 'change': 7}
#     }

# def update_demo_data():
#     for zone in st.session_state.zone_data:
#         st.session_state.zone_data[zone]['count'] += random.randint(-5, 5)
#         st.session_state.zone_data[zone]['density'] += random.randint(-3, 3)
#         st.session_state.zone_data[zone]['density'] = max(0, min(100, st.session_state.zone_data[zone]['density']))

# # Custom CSS for monitoring page
# st.markdown("""
#     <style>
#         .camera-feed {
#             background-color: #f5f5f5;
#             border-radius: 10px;
#             margin-bottom: 20px;
#         }
#         .camera-title {
#             background-color: #1f2b4d;
#             color: white;
#             padding: 10px 20px;
#             border-radius: 10px 10px 0 0;
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#         }
#         .recording-dot {
#             color: #ff4444;
#             animation: blink 1s infinite;
#         }
#         .zone-card {
#             background-color: white;
#             border-radius: 10px;
#             padding: 20px;
#             margin-bottom: 15px;
#             box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#         }
#         .density-badge {
#             padding: 5px 10px;
#             border-radius: 15px;
#             font-size: 14px;
#             font-weight: 500;
#         }
#         .density-high {
#             background-color: #ffe5e5;
#             color: #ff4444;
#         }
#         .density-medium {
#             background-color: #fff3e0;
#             color: #ff9800;
#         }
#         .density-normal {
#             background-color: #e8f5e9;
#             color: #4caf50;
#         }
#         .zone-card{
#             color: black;
#             box-shadow: 0px 0px;
#         }
#         .video-container {
#             padding: 0 20px 20px 20px;
#             background-color: #f5f5f5;
#             border-radius: 0 0 10px 10px;
#         }
#         @keyframes blink {
#             50% { opacity: 0; }
#         }
#         .stVideo {
#             width: 100%;
#             border-radius: 0 0 10px 10px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("<h1 class='header'>Live Camera Monitoring</h1>", unsafe_allow_html=True)

# # Main layout
# col1, col2 = st.columns([2, 1])

# with col1:
#     # Main camera feed container
#     st.markdown("""
#         <div class='camera-feed'>
#             <div class='camera-title'>
#                 <span>Main Entrance - Live Feed</span>
#                 <span class='recording-dot'>● Recording</span>
#             </div>
#         </div>
#     """, unsafe_allow_html=True)
    
#     # Video container
#     with st.container():
#         st.markdown("<div class='video-container'>", unsafe_allow_html=True)
#         try:
#             # Read and display video
#             with open("videosense.mp4", "rb") as video_file:
#                 video_bytes = video_file.read()
#                 st.video(video_bytes)
#         except Exception as e:
#             st.error(f"Error loading video: {str(e)}")
#             st.markdown("""
#                 <div style='height: 400px; display: flex; align-items: center; justify-content: center;'>
#                     <img src='https://via.placeholder.com/800x400' style='max-width: 100%; height: auto;'>
#                 </div>
#             """, unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)
    
#     # Density metrics
#     metrics_cols = st.columns(4)
#     for i, (zone, data) in enumerate(st.session_state.zone_data.items()):
#         with metrics_cols[i]:
#             st.markdown(f"""
#                 <div style='text-align: center; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
#                     <h3 style='color:black;'>Crowd Density</h3>
#                     <h2 style='color: #1f2b4d; font-size: 36px;'>{data['density']}%</h2>
#                     <p style='color: {"#ff4444" if data["change"] > 0 else "#4caf50"}'>
#                         {"↑" if data["change"] > 0 else "↓"} {abs(data["change"])}% from yesterday
#                     </p>
#                 </div>
#             """, unsafe_allow_html=True)

# with col2:
#     st.markdown("<h3>Zone Details</h3>", unsafe_allow_html=True)
    
#     # Zone cards
#     zones = [
#         ("Zone 1 - Entrance Lobby", "high"),
#         ("Zone 2 - Waiting Area", "medium"),
#         ("Zone 3 - Information Desk", "normal")
#     ]
    
#     for i, (zone_name, density_level) in enumerate(zones):
#         zone_data = st.session_state.zone_data[f'zone{i+1}']
#         density_class = {
#             "high": "density-high",
#             "medium": "density-medium",
#             "normal": "density-normal"
#         }[density_level]
        
#         st.markdown(f"""
#             <div class='zone-card'>
#                 <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 15px;'>
#                     <h4 style='margin: 0;' class='zone-card'>{zone_name}</h4>
#                     <span class='density-badge {density_class}'>{density_level.title()}</span>
#                 </div>
#                 <div style='display: flex; justify-content: space-between;'>
#                     <div>
#                         <p style='color: #666; margin: 0;'>People Count</p>
#                         <h3 style='margin: 5px 0;'>{zone_data['count']}</h3>
#                     </div>
#                     <div>
#                         <p style='color: #666; margin: 0;'>Density</p>
#                         <h3 style='margin: 5px 0;'>{zone_data['density']}%</h3>
#                     </div>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)
    
#     # Update button for demo
#     if st.button("Update Data (Demo)"):
#         update_demo_data()
#         st.experimental_rerun()


import streamlit as st
import random
import base64

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

# Custom CSS for monitoring page
st.markdown("""
    <style>
        .camera-feed {
            background-color: #f5f5f5;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .camera-title {
            background-color: #1f2b4d;
            color: white;
            padding: 10px 20px;
            border-radius: 10px 10px 0 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .recording-dot {
            color: #ff4444;
            animation: blink 1s infinite;
        }
        .zone-card {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .density-badge {
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 14px;
            font-weight: 500;
        }
        .density-high {
            background-color: #ffe5e5;
            color: #ff4444;
        }
        .density-medium {
            background-color: #fff3e0;
            color: #ff9800;
        }
        .density-normal {
            background-color: #e8f5e9;
            color: #4caf50;
        }
        .zone-card{
            color: black;
            box-shadow: 0px 0px;
        }
        .video-container {
            padding: 0 20px 20px 20px;
            background-color: #f5f5f5;
            border-radius: 0 0 10px 10px;
        }
        @keyframes blink {
            50% { opacity: 0; }
        }
        .stVideo {
            width: 100%;
            border-radius: 0 0 10px 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='header'>Live Camera Monitoring</h1>", unsafe_allow_html=True)

# Main layout
col1, col2 = st.columns([2, 1])

with col1:
    # Main camera feed container
    st.markdown("""
        <div class='camera-feed'>
            <div class='camera-title'>
                <span>Main Entrance - Live Feed</span>
                <span class='recording-dot'>● Recording</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Video container with autoplay
    with st.container():
        st.markdown("<div class='video-container'>", unsafe_allow_html=True)
        try:
            # Read video file and encode it to base64 for embedding in HTML
            with open("videosense.mp4", "rb") as video_file:
                video_bytes = video_file.read()
                video_base64 = base64.b64encode(video_bytes).decode("utf-8")
            
            # HTML video tag with autoplay enabled
            video_html = f"""
                <video autoplay loop muted playsinline style="width:100%; border-radius: 10px;">
                    <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            """
            
            st.markdown(video_html, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error loading video: {str(e)}")
            st.markdown("""
                <div style='height: 400px; display: flex; align-items: center; justify-content: center;'>
                    <img src='https://via.placeholder.com/800x400' style='max-width: 100%; height: auto;'>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
    
    # Density metrics
    metrics_cols = st.columns(4)
    for i, (zone, data) in enumerate(st.session_state.zone_data.items()):
        with metrics_cols[i]:
            st.markdown(f"""
                <div style='text-align: center; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                    <h3 style='color:black;'>Crowd Density</h3>
                    <h2 style='color: #1f2b4d; font-size: 36px;'>{data['density']}%</h2>
                    <p style='color: {"#ff4444" if data["change"] > 0 else "#4caf50"}'>
                        {"↑" if data["change"] > 0 else "↓"} {abs(data["change"])}% from yesterday
                    </p>
                </div>
            """, unsafe_allow_html=True)

with col2:
    st.markdown("<h3>Zone Details</h3>", unsafe_allow_html=True)
    
    # Zone cards
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
            <div class='zone-card'>
                <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 15px;'>
                    <h4 style='margin: 0;' class='zone-card'>{zone_name}</h4>
                    <span class='density-badge {density_class}'>{density_level.title()}</span>
                </div>
                <div style='display: flex; justify-content: space-between;'>
                    <div>
                        <p style='color: #666; margin: 0;'>People Count</p>
                        <h3 style='margin: 5px 0;'>{zone_data['count']}</h3>
                    </div>
                    <div>
                        <p style='color: #666; margin: 0;'>Density</p>
                        <h3 style='margin: 5px 0;'>{zone_data['density']}%</h3>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Update button for demo
    if st.button("Update Data (Demo)"):
        update_demo_data()
        st.experimental_rerun()
