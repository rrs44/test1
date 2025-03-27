# import streamlit as st

# # Page config
# st.set_page_config(page_title="CrowdSense", layout="wide")

# # Custom CSS for layout
# st.markdown("""
#     <style>
#         .header {
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             background-color: #f1f3f6;
#             padding: 10px 30px;
#             border-bottom: 1px solid #ddd;
#         }
#         .logo {
#             height: 40px;
#         }
#         .nav-buttons {
#             display: flex;
#             gap: 15px;
#         }
#         .nav-buttons a {
#             text-decoration: none;
#             font-weight: 500;
#             color: #333;
#             background-color: #e6e6e6;
#             padding: 8px 16px;
#             border-radius: 8px;
#             transition: background-color 0.3s ease;
#         }
#         .nav-buttons a:hover {
#             background-color: #d0d0d0;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Header layout with logo and nav buttons
# st.markdown(f"""
#     <div class="header">
#         <div>
#             <img class="logo" src="https://via.placeholder.com/150x40.png?text=CrowdSense" alt="Logo">
#         </div>
#         <div class="nav-buttons">
#             <a href="#home">Home</a>
#             <a href="#dashboard">Dashboard</a>
#             <a href="#about-us">About Us</a>
#         </div>
#     </div>
# """, unsafe_allow_html=True)

# # Content placeholders
# st.header("Welcome to CrowdSense")
# st.write("Use the navigation buttons to explore the platform.")


# import streamlit as st

# # Set page config
# st.set_page_config(page_title="CrowdSense", layout="wide")

# # Custom CSS
# st.markdown("""
#     <style>
#         /* Reset default margins */
#         body {
#             margin: 0;
#             font-family: 'Segoe UI', sans-serif;
#         }

#         /* Header styles */
#         .header {
#             background-color: #ffffff;
#             padding: 20px 80px;
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             box-shadow: 0 2px 8px rgba(0,0,0,0.05);
#             position: sticky;
#             top: 0;
#             z-index: 1000;
#         }

#         .logo {
#             font-size: 1.5rem;
#             font-weight: 700;
#             color: #1a2b50;
#         }

#         .nav-links a {
#             margin-left: 24px;
#             text-decoration: none;
#             color: #1a2b50;
#             font-weight: 500;
#             font-size: 1rem;
#             transition: color 0.2s ease;
#         }

#         .nav-links a:hover {
#             color: #ff7a00;
#         }

#         /* Hero section */
#         .hero {
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             padding: 80px;
#             background-color: #f5f7fa;
#         }

#         .hero-text {
#             max-width: 50%;
#         }

#         .hero-title {
#             font-size: 3.5rem;
#             font-weight: 800;
#             color: #1a2b50;
#             margin-bottom: 20px;
#             line-height: 1.2;
#         }

#         .hero-subtext {
#             font-size: 1.3rem;
#             color: #6c757d;
#             margin-bottom: 30px;
#         }

#         .button-group button {
#             font-weight: 600;
#             padding: 12px 24px;
#             font-size: 1rem;
#             margin-right: 16px;
#             border-radius: 8px;
#             border: none;
#             cursor: pointer;
#         }

#         .btn-orange {
#             background-color: #ff7a00;
#             color: white;
#         }

#         .btn-outline {
#             background-color: transparent;
#             border: 2px solid #1a2b50;
#             color: #1a2b50;
#         }

#         .hero-image {
#             max-width: 40%;
#             text-align: center;
#         }

#         .hero-image img {
#             max-width: 100%;
#             height: auto;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Header section
# st.markdown("""
# <div class="header">
#     <div class="logo">CrowdSense</div>
#     <div class="nav-links">
#         <a href="#">Home</a>
#         <a href="#">About</a>
#         <a href="#">Features</a>
#         <a href="#">Contact</a>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # Hero section
# st.markdown("""
# <div class="hero">
#     <div class="hero-text">
#         <div class="hero-title">
#             AI-Powered Smart<br>Crowd Management
#         </div>
#         <div class="hero-subtext">
#             Real-time monitoring, chaos prediction, and enhanced security
#         </div>
#         <div class="button-group">
#             <button class="btn-orange">Request Demo</button>
#             <button class="btn-outline">Learn More</button>
#         </div>
#     </div>
#     <div class="hero-image">
#         <img src="https://cdn.jsdelivr.net/gh/rajatdiptabiswas/particles-bg/circle-particle-bg.png" alt="Particles Background">
#     </div>
# </div>
# """, unsafe_allow_html=True)




# import streamlit as st
# from streamlit.components.v1 import html

# # Set page configuration
# st.set_page_config(page_title="CrowdSense", layout="wide")

# # Custom CSS for layout and styling
# st.markdown("""
#     <style>
#         .main {
#             background-color: #ffffff;
#         }
#         .header {
#             font-size: 42px;
#             font-weight: 700;
#             color: #1f2b4d;
#             text-align: center;
#             margin-bottom: 20px;
#         }
#         .subheader {
#             font-size: 20px;
#             text-align: center;
#             color: #555;
#             margin-bottom: 50px;
#         }
#         .button-card {
#             background-color: #f5f8fc;
#             padding: 30px 20px;
#             border-radius: 15px;
#             box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
#             text-align: left;
#             transition: all 0.2s ease-in-out;
#             height: 180px;
#         }
#         .button-card:hover {
#             transform: scale(1.03);
#             cursor: pointer;
#             box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
#         }
#         .card-icon {
#             font-size: 28px;
#             color: orange;
#             margin-bottom: 10px;
#         }
#         .card-title {
#             font-weight: 700;
#             font-size: 20px;
#             color: #1f2b4d;
#         }
#         .card-desc {
#             color: #333;
#             font-size: 15px;
#             margin-top: 5px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown("<h1 class='header'>CrowdSense</h1>", unsafe_allow_html=True)
# st.markdown("<p class='subheader'>AI-powered Smart Crowd Management System</p>", unsafe_allow_html=True)

# # Hero image placeholder (if needed)
# # st.image("hero.png", use_column_width=True)

# # Features Section
# st.markdown("<h2 class='header'>Key Features</h2>", unsafe_allow_html=True)

# # Layout for features
# features = [
#     {
#         "title": "Real-time Monitoring",
#         "desc": "AI-powered crowd density analysis via CCTV and image processing",
#         "icon": "📹"
#     },
#     {
#         "title": "Chaos Prediction",
#         "desc": "Prevent stampedes and congestion with AI predictive analytics",
#         "icon": "⚠️"
#     },
#     {
#         "title": "Threat Detection",
#         "desc": "Identify weapons, gunshots, and distress signals with AI models",
#         "icon": "🛡️"
#     },
#     {
#         "title": "Route Optimization",
#         "desc": "Dynamic pathfinding for smooth crowd movement",
#         "icon": "🧭"
#     },
#     {
#         "title": "Missing Persons",
#         "desc": "AI-based identification system using facial recognition",
#         "icon": "🔍"
#     },
#     {
#         "title": "Mobile & Web Dashboard",
#         "desc": "Real-time insights for event managers and law enforcement",
#         "icon": "📱"
#     }
# ]

# # Display feature buttons in 3 columns per row
# cols = st.columns(3)
# for i, feature in enumerate(features):
#     with cols[i % 3]:
#         clicked = st.button(
#             label=f"{feature['icon']}  {feature['title']}",
#             key=feature['title'],
#             help=feature['desc']
#         )
#         if clicked:
#             st.success(f"You clicked on **{feature['title']}**")
#         # Add HTML styled description
#         st.markdown(f"""
#             <div class='button-card'>
#                 <div class='card-icon'>{feature['icon']}</div>
#                 <div class='card-title'>{feature['title']}</div>
#                 <div class='card-desc'>{feature['desc']}</div>
#             </div>
#         """, unsafe_allow_html=True)



#approved section 1



# import streamlit as st
# from streamlit.components.v1 import html

# # Set page configuration
# st.set_page_config(page_title="CrowdSense", layout="wide")

# # Custom CSS for layout and styling
# st.markdown("""
#     <style>
#         .main {
#             background-color: #ffffff;
#         }
#         .header {
#             font-size: 42px;
#             font-weight: 700;
#             color: #1f2b4d;
#             text-align: center;
#             margin-bottom: 20px;
#         }
#         .subheader {
#             font-size: 20px;
#             text-align: center;
#             color: #555;
#             margin-bottom: 50px;
#         }
#         .button-card {
#             background-color: #f5f8fc;
#             padding: 30px 20px;
#             border-radius: 15px;
#             box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
#             text-align: left;
#             transition: all 0.2s ease-in-out;
#             height: 180px;
#         }
#         .button-card:hover {
#             transform: scale(1.03);
#             cursor: pointer;
#             box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
#         }
#         .card-icon {
#             font-size: 28px;
#             color: orange;
#             margin-bottom: 10px;
#         }
#         .card-title {
#             font-weight: 700;
#             font-size: 20px;
#             color: #1f2b4d;
#         }
#         .card-desc {
#             color: #333;
#             font-size: 15px;
#             margin-top: 5px;
#         }
#         .tech-stack-section {
#             background-color: #1f2b4d;
#             padding: 50px 0;
#             margin-top: 50px;
#             color: white;
#         }
#         .tech-stack-header {
#             color: white;
#             font-size: 36px;
#             text-align: center;
#             margin-bottom: 40px;
#         }
#         .tech-category {
#             color: #ff6b00;
#             font-size: 24px;
#             font-weight: 600;
#             margin-bottom: 20px;
#         }
#         .tech-item {
#             color: white;
#             font-size: 18px;
#             margin-bottom: 15px;
#             padding: 10px;
#             background-color: rgba(255, 255, 255, 0.1);
#             border-radius: 8px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown("<h1 class='header'>CrowdSense</h1>", unsafe_allow_html=True)
# st.markdown("<p class='subheader'>AI-powered Smart Crowd Management System</p>", unsafe_allow_html=True)

# # Features Section
# st.markdown("<h2 class='header'>Key Features</h2>", unsafe_allow_html=True)

# # Layout for features
# features = [
#     {
#         "title": "Real-time Monitoring",
#         "desc": "AI-powered crowd density analysis via CCTV and image processing",
#         "icon": "📹"
#     },
#     {
#         "title": "Chaos Prediction",
#         "desc": "Prevent stampedes and congestion with AI predictive analytics",
#         "icon": "⚠️"
#     },
#     {
#         "title": "Threat Detection",
#         "desc": "Identify weapons, gunshots, and distress signals with AI models",
#         "icon": "🛡️"
#     },
#     {
#         "title": "Route Optimization",
#         "desc": "Dynamic pathfinding for smooth crowd movement",
#         "icon": "🧭"
#     },
#     {
#         "title": "Missing Persons",
#         "desc": "AI-based identification system using facial recognition",
#         "icon": "🔍"
#     },
#     {
#         "title": "Mobile & Web Dashboard",
#         "desc": "Real-time insights for event managers and law enforcement",
#         "icon": "📱"
#     }
# ]

# # Display feature buttons in 3 columns per row
# cols = st.columns(3)
# for i, feature in enumerate(features):
#     with cols[i % 3]:
#         clicked = st.button(
#             label=f"{feature['icon']}  {feature['title']}",
#             key=feature['title'],
#             help=feature['desc']
#         )
#         if clicked:
#             st.success(f"You clicked on **{feature['title']}**")
#         # Add HTML styled description
#         st.markdown(f"""
#             <div class='button-card'>
#                 <div class='card-icon'>{feature['icon']}</div>
#                 <div class='card-title'>{feature['title']}</div>
#                 <div class='card-desc'>{feature['desc']}</div>
#             </div>
#         """, unsafe_allow_html=True)

# # Technology Stack Section
# st.markdown("""
#     <div class='tech-stack-section'>
#         <h2 class='tech-stack-header'>Our Technology Stack</h2>
#     </div>
# """, unsafe_allow_html=True)

# # Create three columns for the tech stack
# col1, col2, col3 = st.columns(3)

# # AI & Machine Learning Stack
# with col1:
#     st.markdown("<h3 class='tech-category'>AI & Machine Learning</h3>", unsafe_allow_html=True)
#     ai_stack = ["YOLOv8", "Faster R-CNN", "DeepSORT", "YAMNet", "FaceNet"]
#     for tech in ai_stack:
#         st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

# # Backend & Data Stack
# with col2:
#     st.markdown("<h3 class='tech-category'>Backend & Data</h3>", unsafe_allow_html=True)
#     backend_stack = ["FastAPI/Flask", "PostgreSQL/MongoDB", "Cloud Deployment (AWS/GCP)"]
#     for tech in backend_stack:
#         st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

# # Frontend & Mobile Stack
# with col3:
#     st.markdown("<h3 class='tech-category'>Frontend & Mobile</h3>", unsafe_allow_html=True)
#     frontend_stack = ["React.js/Next.js", "Node.js", "Kotlin", "Firebase"]
#     for tech in frontend_stack:
#         st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)



# import streamlit as st
# from streamlit.components.v1 import html

# # Set page configuration
# st.set_page_config(page_title="CrowdSense", layout="wide")

# # Custom CSS for layout and styling
# st.markdown("""
#     <style>
#         .main {
#             background-color: #ffffff;
#         }
#         .header {
#             font-size: 42px;
#             font-weight: 700;
#             color: #1f2b4d;
#             text-align: center;
#             margin-bottom: 20px;
#         }
#         .subheader {
#             font-size: 20px;
#             text-align: center;
#             color: #555;
#             margin-bottom: 50px;
#         }
#         .button-card {
#             background-color: #f5f8fc;
#             padding: 30px 20px;
#             border-radius: 15px;
#             box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
#             text-align: left;
#             transition: all 0.2s ease-in-out;
#             height: 180px;
#         }
#         .button-card:hover {
#             transform: scale(1.03);
#             cursor: pointer;
#             box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
#         }
#         .card-icon {
#             font-size: 28px;
#             color: orange;
#             margin-bottom: 10px;
#         }
#         .card-title {
#             font-weight: 700;
#             font-size: 20px;
#             color: #1f2b4d;
#         }
#         .card-desc {
#             color: #333;
#             font-size: 15px;
#             margin-top: 5px;
#         }
#         .tech-stack-section {
#             background-color: #1f2b4d;
#             padding: 50px 0;
#             margin-top: 50px;
#             color: white;
#         }
#         .tech-stack-header {
#             color: white;
#             font-size: 36px;
#             text-align: center;
#             margin-bottom: 40px;
#         }
#         .tech-category {
#             color: #ff6b00;
#             font-size: 24px;
#             font-weight: 600;
#             margin-bottom: 20px;
#         }
#         .tech-item {
#             color: white;
#             font-size: 18px;
#             margin-bottom: 15px;
#             padding: 10px;
#             background-color: rgba(255, 255, 255, 0.1);
#             border-radius: 8px;
#         }
#         .impact-section {
#             padding: 50px 0;
#             background-color: #ffffff;
#         }
#         .impact-card {
#             background-color: #ffffff;
#             padding: 30px;
#             border-radius: 15px;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#             height: 100%;
#         }
#         .impact-number {
#             font-size: 72px;
#             color: #e0e0e0;
#             position: absolute;
#             right: 20px;
#             top: 10px;
#         }
#         .impact-title {
#             font-size: 24px;
#             color: #1f2b4d;
#             font-weight: 600;
#             margin-bottom: 15px;
#         }
#         .impact-desc {
#             color: #666;
#             font-size: 16px;
#         }
#         .demo-section {
#             background-color: #1f2b4d;
#             padding: 50px 0;
#             color: white;
#         }
#         .demo-form {
#             max-width: 500px;
#             margin: 0 auto;
#         }
#         .footer {
#             background-color: #0a192f;
#             padding: 50px 0 20px;
#             color: #ffffff;
#         }
#         .footer-title {
#             font-size: 20px;
#             font-weight: 600;
#             margin-bottom: 20px;
#             color: white;
#         }
#         .footer-link {
#             color: #a0aec0;
#             text-decoration: none;
#             display: block;
#             margin-bottom: 10px;
#             transition: color 0.2s;
#         }
#         .footer-link:hover {
#             color: #ffffff;
#         }
#         .social-icons {
#             display: flex;
#             gap: 20px;
#             justify-content: flex-end;
#         }
#         .social-icon {
#             color: #a0aec0;
#             font-size: 24px;
#             transition: color 0.2s;
#         }
#         .social-icon:hover {
#             color: #ffffff;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown("<h1 class='header'>CrowdSense</h1>", unsafe_allow_html=True)
# st.markdown("<p class='subheader'>AI-powered Smart Crowd Management System</p>", unsafe_allow_html=True)

# # Features Section
# st.markdown("<h2 class='header'>Key Features</h2>", unsafe_allow_html=True)

# # Layout for features
# features = [
#     {
#         "title": "Real-time Monitoring",
#         "desc": "AI-powered crowd density analysis via CCTV and image processing",
#         "icon": "📹"
#     },
#     {
#         "title": "Chaos Prediction",
#         "desc": "Prevent stampedes and congestion with AI predictive analytics",
#         "icon": "⚠️"
#     },
#     {
#         "title": "Threat Detection",
#         "desc": "Identify weapons, gunshots, and distress signals with AI models",
#         "icon": "🛡️"
#     },
#     {
#         "title": "Route Optimization",
#         "desc": "Dynamic pathfinding for smooth crowd movement",
#         "icon": "🧭"
#     },
#     {
#         "title": "Missing Persons",
#         "desc": "AI-based identification system using facial recognition",
#         "icon": "🔍"
#     },
#     {
#         "title": "Mobile & Web Dashboard",
#         "desc": "Real-time insights for event managers and law enforcement",
#         "icon": "📱"
#     }
# ]

# # Display feature buttons in 3 columns per row
# cols = st.columns(3)
# for i, feature in enumerate(features):
#     with cols[i % 3]:
#         clicked = st.button(
#             label=f"{feature['icon']}  {feature['title']}",
#             key=feature['title'],
#             help=feature['desc']
#         )
#         if clicked:
#             st.success(f"You clicked on **{feature['title']}**")
#         # Add HTML styled description
#         st.markdown(f"""
#             <div class='button-card'>
#                 <div class='card-icon'>{feature['icon']}</div>
#                 <div class='card-title'>{feature['title']}</div>
#                 <div class='card-desc'>{feature['desc']}</div>
#             </div>
#         """, unsafe_allow_html=True)

# # Technology Stack Section
# st.markdown("""
#     <div class='tech-stack-section'>
#         <h2 class='tech-stack-header'>Our Technology Stack</h2>
#     </div>
# """, unsafe_allow_html=True)

# # Create three columns for the tech stack
# col1, col2, col3 = st.columns(3)

# # AI & Machine Learning Stack
# with col1:
#     st.markdown("<h3 class='tech-category'>AI & Machine Learning</h3>", unsafe_allow_html=True)
#     ai_stack = ["YOLOv8", "Faster R-CNN", "DeepSORT", "YAMNet", "FaceNet"]
#     for tech in ai_stack:
#         st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

# # Backend & Data Stack
# with col2:
#     st.markdown("<h3 class='tech-category'>Backend & Data</h3>", unsafe_allow_html=True)
#     backend_stack = ["FastAPI/Flask", "PostgreSQL/MongoDB", "Cloud Deployment (AWS/GCP)"]
#     for tech in backend_stack:
#         st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

# # Frontend & Mobile Stack
# with col3:
#     st.markdown("<h3 class='tech-category'>Frontend & Mobile</h3>", unsafe_allow_html=True)
#     frontend_stack = ["React.js/Next.js", "Node.js", "Kotlin", "Firebase"]
#     for tech in frontend_stack:
#         st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

# # Real-World Impact Section
# st.markdown("<h2 class='header'>Real-World Impact</h2>", unsafe_allow_html=True)

# impact_cols = st.columns(4)
# impacts = [
#     {
#         "number": "01",
#         "title": "Innovation",
#         "desc": "First-of-its-kind multi-modal AI integrating vision, NLP, and predictive analytics"
#     },
#     {
#         "number": "02",
#         "title": "Business Viability",
#         "desc": "Targeting event organizers, law enforcement, and smart city planners"
#     },
#     {
#         "number": "03",
#         "title": "Public Safety",
#         "desc": "Prevents stampedes and enhances emergency response with real-time alerts"
#     },
#     {
#         "number": "04",
#         "title": "Scalability",
#         "desc": "Deployable across various event sizes and smart cities worldwide"
#     }
# ]

# for i, impact in enumerate(impacts):
#     with impact_cols[i]:
#         st.markdown(f"""
#             <div class='impact-card'>
#                 <div class='impact-number'>{impact['number']}</div>
#                 <h3 class='impact-title'>{impact['title']}</h3>
#                 <p class='impact-desc'>{impact['desc']}</p>
#             </div>
#         """, unsafe_allow_html=True)

# # Demo Request Section
# st.markdown("""
#     <div class='demo-section'>
#         <h2 style='text-align: center; font-size: 36px; margin-bottom: 10px;'>Transform Your Crowd Management with AI</h2>
#         <p style='text-align: center; margin-bottom: 30px;'>Schedule a demo to see CrowdSense in action</p>
#     </div>
# """, unsafe_allow_html=True)

# # Create the demo form
# col1, col2, col3 = st.columns([1,2,1])
# with col2:
#     with st.form("demo_form"):
#         st.text_input("Name", key="name")
#         st.text_input("Email", key="email")
#         st.text_input("Organization", key="organization")
#         submitted = st.form_submit_button("Request Demo")
#         if submitted:
#             st.success("Thanks for your interest! We'll contact you soon.")

# # Footer Section
# st.markdown("""
#     <div class='footer'>
#         <div style='display: flex; justify-content: space-between; margin-bottom: 40px;'>
#             <div>
#                 <img src="https://placeholder.com/150x50" alt="CrowdSense Logo" style="margin-bottom: 20px;">
#                 <p>CrowdSense</p>
#             </div>
#             <div>
#                 <h3 class='footer-title'>Company</h3>
#                 <a href="#" class='footer-link'>About Us</a>
#                 <a href="#" class='footer-link'>Our Team</a>
#                 <a href="#" class='footer-link'>Careers</a>
#                 <a href="#" class='footer-link'>Contact</a>
#             </div>
#             <div>
#                 <h3 class='footer-title'>Resources</h3>
#                 <a href="#" class='footer-link'>Blog</a>
#                 <a href="#" class='footer-link'>Documentation</a>
#                 <a href="#" class='footer-link'>API</a>
#                 <a href="#" class='footer-link'>Support</a>
#             </div>
#             <div>
#                 <h3 class='footer-title'>Legal</h3>
#                 <a href="#" class='footer-link'>Privacy Policy</a>
#                 <a href="#" class='footer-link'>Terms of Service</a>
#                 <a href="#" class='footer-link'>Security</a>
#             </div>
#             <div class='social-icons'>
#                 <a href="#" class='social-icon'>🐦</a>
#                 <a href="#" class='social-icon'>💼</a>
#                 <a href="#" class='social-icon'>🎵</a>
#                 <a href="#" class='social-icon'>📸</a>
#             </div>
#         </div>
#         <div style='text-align: center; color: #a0aec0; padding-top: 20px; border-top: 1px solid #2d3748;'>
#             © 2025 CrowdSense. All rights reserved.
#         </div>
#     </div>
# """, unsafe_allow_html=True)




# import streamlit as st
# from streamlit.components.v1 import html
# import random  # For demo data, will be replaced with AI model data later

# # Initialize session state for page management
# if 'current_page' not in st.session_state:
#     st.session_state.current_page = 'home'

# # Initialize demo data in session state (will be replaced with real data later)
# if 'zone_data' not in st.session_state:
#     st.session_state.zone_data = {
#         'zone1': {'count': 78, 'density': 85, 'change': 12},
#         'zone2': {'count': 42, 'density': 57, 'change': 5},
#         'zone3': {'count': 15, 'density': 28, 'change': -3},
#         'zone4': {'count': 35, 'density': 42, 'change': 7}
#     }

# # Function to update demo data (will be replaced with AI model integration)
# def update_demo_data():
#     for zone in st.session_state.zone_data:
#         st.session_state.zone_data[zone]['count'] += random.randint(-5, 5)
#         st.session_state.zone_data[zone]['density'] += random.randint(-3, 3)
#         st.session_state.zone_data[zone]['density'] = max(0, min(100, st.session_state.zone_data[zone]['density']))

# # Set page configuration
# st.set_page_config(page_title="CrowdSense", layout="wide")

# # Custom CSS (previous CSS remains the same, adding new styles for monitoring page)
# st.markdown("""
#     <style>
#         .main {
#             background-color: #ffffff;
#         }
#         .header {
#             font-size: 42px;
#             font-weight: 700;
#             color: #1f2b4d;
#             text-align: center;
#             margin-bottom: 20px;
#         }
#         .subheader {
#             font-size: 20px;
#             text-align: center;
#             color: #555;
#             margin-bottom: 50px;
#         }
#         .button-card {
#             background-color: #f5f8fc;
#             padding: 30px 20px;
#             border-radius: 15px;
#             box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
#             text-align: left;
#             transition: all 0.2s ease-in-out;
#             height: 180px;
#         }
#         .button-card:hover {
#             transform: scale(1.03);
#             cursor: pointer;
#             box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
#         }
#         .card-icon {
#             font-size: 28px;
#             color: orange;
#             margin-bottom: 10px;
#         }
#         .card-title {
#             font-weight: 700;
#             font-size: 20px;
#             color: #1f2b4d;
#         }
#         .card-desc {
#             color: #333;
#             font-size: 15px;
#             margin-top: 5px;
#         }
#         .tech-stack-section {
#             background-color: #1f2b4d;
#             padding: 50px 0;
#             margin-top: 50px;
#             color: white;
#         }
#         .tech-stack-header {
#             color: white;
#             font-size: 36px;
#             text-align: center;
#             margin-bottom: 40px;
#         }
#         .tech-category {
#             color: #ff6b00;
#             font-size: 24px;
#             font-weight: 600;
#             margin-bottom: 20px;
#         }
#         .tech-item {
#             color: white;
#             font-size: 18px;
#             margin-bottom: 15px;
#             padding: 10px;
#             background-color: rgba(255, 255, 255, 0.1);
#             border-radius: 8px;
#         }
#         .impact-section {
#             padding: 50px 0;
#             background-color: #ffffff;
#         }
#         .impact-card {
#             background-color: #ffffff;
#             padding: 30px;
#             border-radius: 15px;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#             height: 100%;
#         }
#         .impact-number {
#             font-size: 72px;
#             color: #e0e0e0;
#             position: absolute;
#             right: 20px;
#             top: 10px;
#         }
#         .impact-title {
#             font-size: 24px;
#             color: #1f2b4d;
#             font-weight: 600;
#             margin-bottom: 15px;
#         }
#         .impact-desc {
#             color: #666;
#             font-size: 16px;
#         }
#         .demo-section {
#             background-color: #1f2b4d;
#             padding: 50px 0;
#             color: white;
#         }
#         .demo-form {
#             max-width: 500px;
#             margin: 0 auto;
#         }
#         .footer {
#             background-color: #0a192f;
#             padding: 50px 0 20px;
#             color: #ffffff;
#         }
#         .footer-title {
#             font-size: 20px;
#             font-weight: 600;
#             margin-bottom: 20px;
#             color: white;
#         }
#         .footer-link {
#             color: #a0aec0;
#             text-decoration: none;
#             display: block;
#             margin-bottom: 10px;
#             transition: color 0.2s;
#         }
#         .footer-link:hover {
#             color: #ffffff;
#         }
#         .social-icons {
#             display: flex;
#             gap: 20px;
#             justify-content: flex-end;
#         }
#         .social-icon {
#             color: #a0aec0;
#             font-size: 24px;
#             transition: color 0.2s;
#         }
#         .social-icon:hover {
#             color: #ffffff;
#         }
        
#         /* New styles for monitoring page */
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
#         @keyframes blink {
#             50% { opacity: 0; }
#         }
#     </style>
# """, unsafe_allow_html=True)

# def show_monitoring_page():
#     st.markdown("<h1 class='header'>Live Camera Monitoring</h1>", unsafe_allow_html=True)
    
#     # Main layout
#     col1, col2 = st.columns([2, 1])
    
#     with col1:
#         # Main camera feed
#         st.markdown("""
#             <div class='camera-feed'>
#                 <div class='camera-title'>
#                     <span>Main Entrance - Live Feed</span>
#                     <span class='recording-dot'>● Recording</span>
#                 </div>
#                 <div style='height: 400px; display: flex; align-items: center; justify-content: center;'>
#                     <img src='https://via.placeholder.com/800x400' style='max-width: 100%; height: auto;'>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)
        
#         # Density metrics
#         metrics_cols = st.columns(4)
#         for i, (zone, data) in enumerate(st.session_state.zone_data.items()):
#             with metrics_cols[i]:
#                 st.markdown(f"""
#                     <div style='text-align: center; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
#                         <h3>Crowd Density</h3>
#                         <h2 style='color: #1f2b4d; font-size: 36px;'>{data['density']}%</h2>
#                         <p style='color: {"#ff4444" if data["change"] > 0 else "#4caf50"}'>
#                             {"↑" if data["change"] > 0 else "↓"} {abs(data["change"])}% from yesterday
#                         </p>
#                     </div>
#                 """, unsafe_allow_html=True)
    
#     with col2:
#         st.markdown("<h3>Zone Details</h3>", unsafe_allow_html=True)
        
#         # Zone cards
#         zones = [
#             ("Zone 1 - Entrance Lobby", "high"),
#             ("Zone 2 - Waiting Area", "medium"),
#             ("Zone 3 - Information Desk", "normal")
#         ]
        
#         for i, (zone_name, density_level) in enumerate(zones):
#             zone_data = st.session_state.zone_data[f'zone{i+1}']
#             density_class = {
#                 "high": "density-high",
#                 "medium": "density-medium",
#                 "normal": "density-normal"
#             }[density_level]
            
#             st.markdown(f"""
#                 <div class='zone-card'>
#                     <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 15px;'>
#                         <h4 style='margin: 0;'>{zone_name}</h4>
#                         <span class='density-badge {density_class}'>{density_level.title()}</span>
#                     </div>
#                     <div style='display: flex; justify-content: space-between;'>
#                         <div>
#                             <p style='color: #666; margin: 0;'>People Count</p>
#                             <h3 style='margin: 5px 0;'>{zone_data['count']}</h3>
#                         </div>
#                         <div>
#                             <p style='color: #666; margin: 0;'>Density</p>
#                             <h3 style='margin: 5px 0;'>{zone_data['density']}%</h3>
#                         </div>
#                     </div>
#                 </div>
#             """, unsafe_allow_html=True)
        
#         # Update button for demo
#         if st.button("Update Data (Demo)"):
#             update_demo_data()
#             st.experimental_rerun()

# def show_home_page():
#     st.markdown("<h1 class='header'>CrowdSense</h1>", unsafe_allow_html=True)
#     st.markdown("<p class='subheader'>AI-powered Smart Crowd Management System</p>", unsafe_allow_html=True)

#     # Features Section
#     st.markdown("<h2 class='header'>Key Features</h2>", unsafe_allow_html=True)

#     # Layout for features
#     features = [
#         {
#             "title": "Real-time Monitoring",
#             "desc": "AI-powered crowd density analysis via CCTV and image processing",
#             "icon": "📹"
#         },
#         {
#             "title": "Chaos Prediction",
#             "desc": "Prevent stampedes and congestion with AI predictive analytics",
#             "icon": "⚠️"
#         },
#         {
#             "title": "Threat Detection",
#             "desc": "Identify weapons, gunshots, and distress signals with AI models",
#             "icon": "🛡️"
#         },
#         {
#             "title": "Route Optimization",
#             "desc": "Dynamic pathfinding for smooth crowd movement",
#             "icon": "🧭"
#         },
#         {
#             "title": "Missing Persons",
#             "desc": "AI-based identification system using facial recognition",
#             "icon": "🔍"
#         },
#         {
#             "title": "Mobile & Web Dashboard",
#             "desc": "Real-time insights for event managers and law enforcement",
#             "icon": "📱"
#         }
#     ]

#     # Display feature buttons in 3 columns per row
#     cols = st.columns(3)
#     for i, feature in enumerate(features):
#         with cols[i % 3]:
#             clicked = st.button(
#                 label=f"{feature['icon']}  {feature['title']}",
#                 key=feature['title'],
#                 help=feature['desc']
#             )
#             if clicked and feature['title'] == "Real-time Monitoring":
#                 st.session_state.current_page = 'monitoring'
#                 st.experimental_rerun()
                
#             st.markdown(f"""
#                 <div class='button-card'>
#                     <div class='card-icon'>{feature['icon']}</div>
#                     <div class='card-title'>{feature['title']}</div>
#                     <div class='card-desc'>{feature['desc']}</div>
#                 </div>
#             """, unsafe_allow_html=True)

#     # Technology Stack Section
#     st.markdown("""
#         <div class='tech-stack-section'>
#             <h2 class='tech-stack-header'>Our Technology Stack</h2>
#         </div>
#     """, unsafe_allow_html=True)

#     # Create three columns for the tech stack
#     col1, col2, col3 = st.columns(3)

#     # AI & Machine Learning Stack
#     with col1:
#         st.markdown("<h3 class='tech-category'>AI & Machine Learning</h3>", unsafe_allow_html=True)
#         ai_stack = ["YOLOv8", "Faster R-CNN", "DeepSORT", "YAMNet", "FaceNet"]
#         for tech in ai_stack:
#             st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

#     # Backend & Data Stack
#     with col2:
#         st.markdown("<h3 class='tech-category'>Backend & Data</h3>", unsafe_allow_html=True)
#         backend_stack = ["FastAPI/Flask", "PostgreSQL/MongoDB", "Cloud Deployment (AWS/GCP)"]
#         for tech in backend_stack:
#             st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

#     # Frontend & Mobile Stack
#     with col3:
#         st.markdown("<h3 class='tech-category'>Frontend & Mobile</h3>", unsafe_allow_html=True)
#         frontend_stack = ["React.js/Next.js", "Node.js", "Kotlin", "Firebase"]
#         for tech in frontend_stack:
#             st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

#     # Real-World Impact Section
#     st.markdown("<h2 class='header'>Real-World Impact</h2>", unsafe_allow_html=True)

#     impact_cols = st.columns(4)
#     impacts = [
#         {
#             "number": "01",
#             "title": "Innovation",
#             "desc": "First-of-its-kind multi-modal AI integrating vision, NLP, and predictive analytics"
#         },
#         {
#             "number": "02",
#             "title": "Business Viability",
#             "desc": "Targeting event organizers, law enforcement, and smart city planners"
#         },
#         {
#             "number": "03",
#             "title": "Public Safety",
#             "desc": "Prevents stampedes and enhances emergency response with real-time alerts"
#         },
#         {
#             "number": "04",
#             "title": "Scalability",
#             "desc": "Deployable across various event sizes and smart cities worldwide"
#         }
#     ]

#     for i, impact in enumerate(impacts):
#         with impact_cols[i]:
#             st.markdown(f"""
#                 <div class='impact-card'>
#                     <div class='impact-number'>{impact['number']}</div>
#                     <h3 class='impact-title'>{impact['title']}</h3>
#                     <p class='impact-desc'>{impact['desc']}</p>
#                 </div>
#             """, unsafe_allow_html=True)

#     # Demo Request Section
#     st.markdown("""
#         <div class='demo-section'>
#             <h2 style='text-align: center; font-size: 36px; margin-bottom: 10px;'>Transform Your Crowd Management with AI</h2>
#             <p style='text-align: center; margin-bottom: 30px;'>Schedule a demo to see CrowdSense in action</p>
#         </div>
#     """, unsafe_allow_html=True)

#     # Create the demo form
#     col1, col2, col3 = st.columns([1,2,1])
#     with col2:
#         with st.form("demo_form"):
#             st.text_input("Name", key="name")
#             st.text_input("Email", key="email")
#             st.text_input("Organization", key="organization")
#             submitted = st.form_submit_button("Request Demo")
#             if submitted:
#                 st.success("Thanks for your interest! We'll contact you soon.")

#     # Footer Section
#     st.markdown("""
#         <div class='footer'>
#             <div style='display: flex; justify-content: space-between; margin-bottom: 40px;'>
#                 <div>
#                     <img src="https://placeholder.com/150x50" alt="CrowdSense Logo" style="margin-bottom: 20px;">
#                     <p>CrowdSense</p>
#                 </div>
#                 <div>
#                     <h3 class='footer-title'>Company</h3>
#                     <a href="#" class='footer-link'>About Us</a>
#                     <a href="#" class='footer-link'>Our Team</a>
#                     <a href="#" class='footer-link'>Careers</a>
#                     <a href="#" class='footer-link'>Contact</a>
#                 </div>
#                 <div>
#                     <h3 class='footer-title'>Resources</h3>
#                     <a href="#" class='footer-link'>Blog</a>
#                     <a href="#" class='footer-link'>Documentation</a>
#                     <a href="#" class='footer-link'>API</a>
#                     <a href="#" class='footer-link'>Support</a>
#                 </div>
#                 <div>
#                     <h3 class='footer-title'>Legal</h3>
#                     <a href="#" class='footer-link'>Privacy Policy</a>
#                     <a href="#" class='footer-link'>Terms of Service</a>
#                     <a href="#" class='footer-link'>Security</a>
#                 </div>
#                 <div class='social-icons'>
#                     <a href="#" class='social-icon'>🐦</a>
#                     <a href="#" class='social-icon'>💼</a>
#                     <a href="#" class='social-icon'>🎵</a>
#                     <a href="#" class='social-icon'>📸</a>
#                 </div>
#             </div>
#             <div style='text-align: center; color: #a0aec0; padding-top: 20px; border-top: 1px solid #2d3748;'>
#                 © 2025 CrowdSense. All rights reserved.
#             </div>
#         </div>
#     """, unsafe_allow_html=True)

# # Main app logic
# if st.session_state.current_page == 'monitoring':
#     show_monitoring_page()
# else:
#     show_home_page()



# import streamlit as st
# from streamlit.components.v1 import html

# # Set page configuration
# st.set_page_config(page_title="CrowdSense", layout="wide")

# # Custom CSS for layout and styling
# st.markdown("""
#     <style>
#         .main { background-color: #ffffff; }
#         .header {
#             font-size: 42px;
#             font-weight: 700;
#             color: #1f2b4d;
#             text-align: center;
#             margin-bottom: 20px;
#         }
#         .subheader {
#             font-size: 20px;
#             text-align: center;
#             color: #555;
#             margin-bottom: 50px;
#         }
#         .button-card {
#             background-color: #f5f8fc;
#             padding: 30px 20px;
#             border-radius: 15px;
#             box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
#             text-align: left;
#             transition: all 0.2s ease-in-out;
#             height: 180px;
#         }
#         .button-card:hover {
#             transform: scale(1.03);
#             cursor: pointer;
#             box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
#         }
#         .card-icon {
#             font-size: 28px;
#             color: orange;
#             margin-bottom: 10px;
#         }
#         .card-title {
#             font-weight: 700;
#             font-size: 20px;
#             color: #1f2b4d;
#         }
#         .card-desc {
#             color: #333;
#             font-size: 15px;
#             margin-top: 5px;
#         }
#         .tech-stack-section {
#             background-color: #1f2b4d;
#             padding: 50px 0;
#             margin-top: 50px;
#             color: white;
#         }
#         .tech-stack-header {
#             color: white;
#             font-size: 36px;
#             text-align: center;
#             margin-bottom: 40px;
#         }
#         .tech-category {
#             color: #ff6b00;
#             font-size: 24px;
#             font-weight: 600;
#             margin-bottom: 20px;
#         }
#         .tech-item {
#             color: white;
#             font-size: 18px;
#             margin-bottom: 15px;
#             padding: 10px;
#             background-color: rgba(255, 255, 255, 0.1);
#             border-radius: 8px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown("<h1 class='header'>CrowdSense</h1>", unsafe_allow_html=True)
# st.markdown("<p class='subheader'>AI-powered Smart Crowd Management System</p>", unsafe_allow_html=True)

# # Features Section
# st.markdown("<h2 class='header'>Key Features</h2>", unsafe_allow_html=True)

# # Layout for features
# features = [
#     { "title": "Real-time Monitoring", "desc": "AI-powered crowd density analysis via CCTV and image processing", "icon": "📹" },
#     { "title": "Chaos Prediction", "desc": "Prevent stampedes and congestion with AI predictive analytics", "icon": "⚠️" },
#     { "title": "Threat Detection", "desc": "Identify weapons, gunshots, and distress signals with AI models", "icon": "🛡️" },
#     { "title": "Route Optimization", "desc": "Dynamic pathfinding for smooth crowd movement", "icon": "🧭" },
#     { "title": "Missing Persons", "desc": "AI-based identification system using facial recognition", "icon": "🔍" },
#     { "title": "Mobile & Web Dashboard", "desc": "Real-time insights for event managers and law enforcement", "icon": "📱" }
# ]

# # Display feature buttons in 3 columns per row
# cols = st.columns(3)
# for i, feature in enumerate(features):
#     with cols[i % 3]:
#         st.markdown(f"""
#             <div class='button-card'>
#                 <div class='card-icon'>{feature['icon']}</div>
#                 <div class='card-title'>{feature['title']}</div>
#                 <div class='card-desc'>{feature['desc']}</div>
#             </div>
#         """, unsafe_allow_html=True)

# # Technology Stack Section
# st.markdown("<div class='tech-stack-section'><h2 class='tech-stack-header'>Our Technology Stack</h2></div>", unsafe_allow_html=True)

# # Create three columns for the tech stack
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown("<h3 class='tech-category'>AI & Machine Learning</h3>", unsafe_allow_html=True)
#     for tech in ["YOLOv8", "Faster R-CNN", "DeepSORT", "YAMNet", "FaceNet"]:
#         st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

# with col2:
#     st.markdown("<h3 class='tech-category'>Backend & Data</h3>", unsafe_allow_html=True)
#     for tech in ["FastAPI/Flask", "PostgreSQL/MongoDB", "Cloud Deployment (AWS/GCP)"]:
#         st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

# with col3:
#     st.markdown("<h3 class='tech-category'>Frontend & Mobile</h3>", unsafe_allow_html=True)
#     for tech in ["React.js/Next.js", "Node.js", "Kotlin", "Firebase"]:
#         st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

# # Footer Section
# st.markdown("""
#     <div class='footer'>
#         <p style='text-align: center; color: white;'>© 2025 CrowdSense. All rights reserved.</p>
#     </div>
# """, unsafe_allow_html=True)



import streamlit as st
from streamlit.components.v1 import html
import random  # For demo data, will be replaced with AI model data later

# Initialize session state for page management
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# Initialize demo data in session state (will be replaced with real data later)
if 'zone_data' not in st.session_state:
    st.session_state.zone_data = {
        'zone1': {'count': 78, 'density': 85, 'change': 12},
        'zone2': {'count': 42, 'density': 57, 'change': 5},
        'zone3': {'count': 15, 'density': 28, 'change': -3},
        'zone4': {'count': 35, 'density': 42, 'change': 7}
    }

# Function to update demo data (will be replaced with AI model integration)
def update_demo_data():
    for zone in st.session_state.zone_data:
        st.session_state.zone_data[zone]['count'] += random.randint(-5, 5)
        st.session_state.zone_data[zone]['density'] += random.randint(-3, 3)
        st.session_state.zone_data[zone]['density'] = max(0, min(100, st.session_state.zone_data[zone]['density']))

# Set page configuration
st.set_page_config(page_title="CrowdSense", layout="wide")

# Custom CSS (previous CSS remains the same, adding new styles for monitoring page)
st.markdown("""
    <style>
        .main {
            background-color: #ffffff;
        }
        .header {
            font-size: 42px;
            font-weight: 700;
            color: #1f2b4d;
            text-align: center;
            margin-bottom: 20px;
        }
        .subheader {
            font-size: 20px;
            text-align: center;
            color: #555;
            margin-bottom: 50px;
        }
        .button-card {
            background-color: #f5f8fc;
            padding: 30px 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
            text-align: left;
            transition: all 0.2s ease-in-out;
            height: 180px;
        }
        .button-card:hover {
            transform: scale(1.03);
            cursor: pointer;
            box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
        }
        .card-icon {
            font-size: 28px;
            color: orange;
            margin-bottom: 10px;
        }
        .card-title {
            font-weight: 700;
            font-size: 20px;
            color: #1f2b4d;
        }
        .card-desc {
            color: #333;
            font-size: 15px;
            margin-top: 5px;
        }
        .tech-stack-section {
            background-color: #1f2b4d;
            padding: 50px 0;
            margin-top: 50px;
            color: white;
        }
        .tech-stack-header {
            color: white;
            font-size: 36px;
            text-align: center;
            margin-bottom: 40px;
        }
        .tech-category {
            color: #ff6b00;
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 20px;
        }
        .tech-item {
            color: white;
            font-size: 18px;
            margin-bottom: 15px;
            padding: 10px;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
        }
        .impact-section {
            padding: 50px 0;
            background-color: #ffffff;
        }
        .impact-card {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            height: 100%;
        }
        .impact-number {
            font-size: 72px;
            color: #e0e0e0;
            position: absolute;
            right: 20px;
            top: 10px;
        }
        .impact-title {
            font-size: 24px;
            color: #1f2b4d;
            font-weight: 600;
            margin-bottom: 15px;
        }
        .impact-desc {
            color: #666;
            font-size: 16px;
        }
        .demo-section {
            background-color: #1f2b4d;
            padding: 50px 0;
            color: white;
        }
        .demo-form {
            max-width: 500px;
            margin: 0 auto;
        }
        .footer {
            background-color: #0a192f;
            padding: 50px 0 20px;
            color: #ffffff;
        }
        .footer-title {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 20px;
            color: white;
        }
        .footer-link {
            color: #a0aec0;
            text-decoration: none;
            display: block;
            margin-bottom: 10px;
            transition: color 0.2s;
        }
        .footer-link:hover {
            color: #ffffff;
        }
        .social-icons {
            display: flex;
            gap: 20px;
            justify-content: flex-end;
        }
        .social-icon {
            color: #a0aec0;
            font-size: 24px;
            transition: color 0.2s;
        }
        .social-icon:hover {
            color: #ffffff;
        }
        
        /* New styles for monitoring page */
        .camera-feed {
            background-color: #f5f5f5;
            border-radius: 10px;
            padding: 20px;
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
        @keyframes blink {
            50% { opacity: 0; }
        }
    </style>
""", unsafe_allow_html=True)

def show_monitoring_page():
    st.markdown("<h1 class='header'>Live Camera Monitoring</h1>", unsafe_allow_html=True)
    
    # Main layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Main camera feed
        st.markdown("""
            <div class='camera-feed'>
                <div class='camera-title'>
                    <span>Main Entrance - Live Feed</span>
                    <span class='recording-dot'>● Recording</span>
                </div>
                <div style='height: 400px; display: flex; align-items: center; justify-content: center;'>
                    <img src='https://via.placeholder.com/800x400' style='max-width: 100%; height: auto;'>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Density metrics
        metrics_cols = st.columns(4)
        for i, (zone, data) in enumerate(st.session_state.zone_data.items()):
            with metrics_cols[i]:
                st.markdown(f"""
                    <div style='text-align: center; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                        <h3>Crowd Density</h3>
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
                        <h4 style='margin: 0;'>{zone_name}</h4>
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

def show_home_page():
    st.markdown("<h1 class='header'>CrowdSense</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subheader'>AI-powered Smart Crowd Management System</p>", unsafe_allow_html=True)

    # Features Section
    st.markdown("<h2 class='header'>Key Features</h2>", unsafe_allow_html=True)

    # Layout for features
    features = [
        {
            "title": "Real-time Monitoring",
            "desc": "AI-powered crowd density analysis via CCTV and image processing",
            "icon": "📹"
        },
        {
            "title": "Chaos Prediction",
            "desc": "Prevent stampedes and congestion with AI predictive analytics",
            "icon": "⚠️"
        },
        {
            "title": "Threat Detection",
            "desc": "Identify weapons, gunshots, and distress signals with AI models",
            "icon": "🛡️"
        },
        {
            "title": "Route Optimization",
            "desc": "Dynamic pathfinding for smooth crowd movement",
            "icon": "🧭"
        },
        {
            "title": "Missing Persons",
            "desc": "AI-based identification system using facial recognition",
            "icon": "🔍"
        },
        {
            "title": "Mobile & Web Dashboard",
            "desc": "Real-time insights for event managers and law enforcement",
            "icon": "📱"
        }
    ]

    # Display feature buttons in 3 columns per row
    cols = st.columns(3)
    for i, feature in enumerate(features):
        with cols[i % 3]:
            clicked = st.button(
                label=f"{feature['icon']}  {feature['title']}",
                key=feature['title'],
                help=feature['desc']
            )
            if clicked and feature['title'] == "Real-time Monitoring":
                st.session_state.current_page = 'monitoring'
                st.experimental_rerun()
                
            st.markdown(f"""
                <div class='button-card'>
                    <div class='card-icon'>{feature['icon']}</div>
                    <div class='card-title'>{feature['title']}</div>
                    <div class='card-desc'>{feature['desc']}</div>
                </div>
            """, unsafe_allow_html=True)

    # Technology Stack Section
    st.markdown("""
        <div class='tech-stack-section'>
            <h2 class='tech-stack-header'>Our Technology Stack</h2>
        </div>
    """, unsafe_allow_html=True)

    # Create three columns for the tech stack
    col1, col2, col3 = st.columns(3)

    # AI & Machine Learning Stack
    with col1:
        st.markdown("<h3 class='tech-category'>AI & Machine Learning</h3>", unsafe_allow_html=True)
        ai_stack = ["YOLOv8", "Faster R-CNN", "DeepSORT", "YAMNet", "FaceNet"]
        for tech in ai_stack:
            st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

    # Backend & Data Stack
    with col2:
        st.markdown("<h3 class='tech-category'>Backend & Data</h3>", unsafe_allow_html=True)
        backend_stack = ["FastAPI/Flask", "PostgreSQL/MongoDB", "Cloud Deployment (AWS/GCP)"]
        for tech in backend_stack:
            st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

    # Frontend & Mobile Stack
    with col3:
        st.markdown("<h3 class='tech-category'>Frontend & Mobile</h3>", unsafe_allow_html=True)
        frontend_stack = ["React.js/Next.js", "Node.js", "Kotlin", "Firebase"]
        for tech in frontend_stack:
            st.markdown(f"<div class='tech-item'>{tech}</div>", unsafe_allow_html=True)

    # Real-World Impact Section
    st.markdown("<h2 class='header'>Real-World Impact</h2>", unsafe_allow_html=True)

    impact_cols = st.columns(4)
    impacts = [
        {
            "number": "01",
            "title": "Innovation",
            "desc": "First-of-its-kind multi-modal AI integrating vision, NLP, and predictive analytics"
        },
        {
            "number": "02",
            "title": "Business Viability",
            "desc": "Targeting event organizers, law enforcement, and smart city planners"
        },
        {
            "number": "03",
            "title": "Public Safety",
            "desc": "Prevents stampedes and enhances emergency response with real-time alerts"
        },
        {
            "number": "04",
            "title": "Scalability",
            "desc": "Deployable across various event sizes and smart cities worldwide"
        }
    ]

    for i, impact in enumerate(impacts):
        with impact_cols[i]:
            st.markdown(f"""
                <div class='impact-card'>
                    <div class='impact-number'>{impact['number']}</div>
                    <h3 class='impact-title'>{impact['title']}</h3>
                    <p class='impact-desc'>{impact['desc']}</p>
                </div>
            """, unsafe_allow_html=True)

    # Demo Request Section
    st.markdown("""
        <div class='demo-section'>
            <h2 style='text-align: center; font-size: 36px; margin-bottom: 10px;'>Transform Your Crowd Management with AI</h2>
            <p style='text-align: center; margin-bottom: 30px;'>Schedule a demo to see CrowdSense in action</p>
        </div>
    """, unsafe_allow_html=True)

    # Create the demo form
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        with st.form("demo_form"):
            st.text_input("Name", key="name")
            st.text_input("Email", key="email")
            st.text_input("Organization", key="organization")
            submitted = st.form_submit_button("Request Demo")
            if submitted:
                st.success("Thanks for your interest! We'll contact you soon.")

    # Footer Section
    st.markdown("""
        <div class='footer'>
            <div style='display: flex; justify-content: space-between; margin-bottom: 40px;'>
                <div>
                    <img src="https://placeholder.com/150x50" alt="CrowdSense Logo" style="margin-bottom: 20px;">
                    <p>CrowdSense</p>
                </div>
                <div>
                    <h3 class='footer-title'>Company</h3>
                    <a href="#" class='footer-link'>About Us</a>
                    <a href="#" class='footer-link'>Our Team</a>
                    <a href="#" class='footer-link'>Careers</a>
                    <a href="#" class='footer-link'>Contact</a>
                </div>
                <div>
                    <h3 class='footer-title'>Resources</h3>
                    <a href="#" class='footer-link'>Blog</a>
                    <a href="#" class='footer-link'>Documentation</a>
                    <a href="#" class='footer-link'>API</a>
                    <a href="#" class='footer-link'>Support</a>
                </div>
                <div>
                    <h3 class='footer-title'>Legal</h3>
                    <a href="#" class='footer-link'>Privacy Policy</a>
                    <a href="#" class='footer-link'>Terms of Service</a>
                    <a href="#" class='footer-link'>Security</a>
                </div>
                <div class='social-icons'>
                    <a href="#" class='social-icon'>🐦</a>
                    <a href="#" class='social-icon'>💼</a>
                    <a href="#" class='social-icon'>🎵</a>
                    <a href="#" class='social-icon'>📸</a>
                </div>
            </div>
            <div style='text-align: center; color: #a0aec0; padding-top: 20px; border-top: 1px solid #2d3748;'>
                © 2025 CrowdSense. All rights reserved.
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main app logic
if st.session_state.current_page == 'monitoring':
    show_monitoring_page()
else:
    show_home_page()