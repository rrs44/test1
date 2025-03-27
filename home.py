import streamlit as st
import base64

# Page configuration
st.set_page_config(page_title="CrowdSense - AI-Powered Crowd Management", layout="wide", page_icon="🌐")

# Advanced Custom CSS
st.markdown("""
<style>
    /* Base Styling */
    .stApp {
        background-color: #0F172A;
        font-family: 'Inter', 'Segoe UI', Roboto, sans-serif;
        color: white;
    }

    /* Gradient Background Effects */
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 30% 80%, rgba(59,130,246,0.2), transparent 50%),
                    radial-gradient(circle at 70% 20%, rgba(255,107,0,0.2), transparent 50%);
        z-index: -1;
    }

    /* Glowing Button Effect */
    .cta-button {
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(255,107,0,0.3);
    }

    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(255,107,0,0.4);
    }

    /* Feature Card Hover Effect */
    .feature-card {
        transition: all 0.4s ease;
        background: linear-gradient(145deg, #2D3748, #1E2130);
        border: 1px solid rgba(59,130,246,0.1);
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }

    .feature-card:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 35px rgba(59,130,246,0.2);
    }

    /* Glassmorphism Contact Form */
    .contact-section {
        background: rgba(30, 33, 48, 0.6);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.1);
    }

    /* Typography */
    h1, h2, h3 {
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .feature-grid, .tech-stack-grid {
            flex-direction: column;
        }
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Navigation
    st.markdown("""
<div style="display: flex; justify-content: center; align-items: center; padding: 20px; background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(10px);">
    <div style="display: flex; align-items: center; text-align: center;">
        <h1 style="color: white; margin: 0; display: flex; align-items: center; font-size: 5rem;">
            <svg width="60" height="60" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" style="margin-right: 10px;">
                <circle cx="50" cy="50" r="45" fill="#FF6B00"/>
                <path d="M25 50 Q50 25, 75 50 T125 50" stroke="white" stroke-width="5" fill="transparent"/>
            </svg>
            CrowdSense
        </h1>
    </div>
</div>
""", unsafe_allow_html=True)


    # Hero Section
    st.markdown("""
    <div style="position: relative; text-align: center; padding: 0px 20px 100px 20px; color: white;">
        <h1 style="font-size: 3.5rem; margin-bottom: 20px; background: linear-gradient(90deg, white, rgba(255,255,255,0.7)); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            AI-Powered Smart Crowd Management
        </h1>
        <p style="font-size: 1.3rem; color: rgba(255,255,255,0.7); max-width: 800px; margin: 0 auto 30px;">
            Revolutionizing crowd dynamics with advanced AI technologies. Real-time monitoring, predictive analysis, and intelligent risk mitigation.
        </p>
        <div style="display: flex; justify-content: center; gap: 20px; margin-top: 30px;">
            <button style="background-color: #FF6B00; color: white; border: none; padding: 12px 25px; border-radius: 8px; font-weight: bold; transition: all 0.3s;">
                Request Demo
            </button>
            <button style="background-color: transparent; color: white; border: 2px solid white; padding: 10px 25px; border-radius: 8px; font-weight: bold; transition: all 0.3s;">
                Learn More
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Key Features
    st.markdown("""
    <div style="display: flex; justify-content: space-around; padding: 50px 20px; background: linear-gradient(to right, #1E2130, #0F172A);">
        <div style="text-align: center; max-width: 250px; padding: 20px; background: linear-gradient(145deg, #2D3748, #1E2130); border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); transition: all 0.4s;">
            <svg width="60" height="60" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-bottom: 15px;">
                <circle cx="50" cy="50" r="45" fill="#FF6B00" fill-opacity="0.2"/>
                <path d="M50 25L60 45H40L50 25Z" fill="#FF6B00"/>
                <path d="M50 75L40 55H60L50 75Z" fill="#FF6B00"/>
            </svg>
            <h3 style="color: white;">Real-time Monitoring</h3>
            <p style="color: rgba(255,255,255,0.7);">Advanced tracking of crowd dynamics and movement patterns</p>
        </div>
        <div style="text-align: center; max-width: 250px; padding: 20px; background: linear-gradient(145deg, #2D3748, #1E2130); border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); transition: all 0.4s;">
            <svg width="60" height="60" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-bottom: 15px;">
                <circle cx="50" cy="50" r="45" fill="#3B82F6" fill-opacity="0.2"/>
                <path d="M25 75C25 75 35 50 50 50C65 50 75 75 75 75" stroke="#3B82F6" stroke-width="5" fill="transparent"/>
                <circle cx="50" cy="40" r="10" fill="#3B82F6"/>
            </svg>
            <h3 style="color: white;">Chaos Prediction</h3>
            <p style="color: rgba(255,255,255,0.7);">Proactive prediction of potential crowd-related challenges</p>
        </div>
        <div style="text-align: center; max-width: 250px; padding: 20px; background: linear-gradient(145deg, #2D3748, #1E2130); border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); transition: all 0.4s;">
            <svg width="60" height="60" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-bottom: 15px;">
                <circle cx="50" cy="50" r="45" fill="#10B981" fill-opacity="0.2"/>
                <path d="M50 25L70 50L50 75L30 50L50 25Z" stroke="#10B981" stroke-width="5" fill="transparent"/>
            </svg>
            <h3 style="color: white;">Threat Detection</h3>
            <p style="color: rgba(255,255,255,0.7);">Intelligent risk identification and mitigation strategies</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Technology Stack
    st.markdown("""
    <div style="background: linear-gradient(to bottom, #0F172A, #1E2130); padding: 50px 20px; text-align: center;">
        <h2 style="color: white; margin-bottom: 30px;">Our Advanced Technology Stack</h2>
        <div style="display: flex; justify-content: center; gap: 50px;">
            <div>
                <h3 style="color: #FF6B00;">AI & Machine Learning</h3>
                <p style="color: white;">Python, Deep Learning, GNN</p>
            </div>
            <div>
                <h3 style="color: #3B82F6;">Backend & Data</h3>
                <p style="color: white;">Rust, PostgreSQL, Spring</p>
            </div>
            <div>
                <h3 style="color: #10B981;">Frontend & Mobile</h3>
                <p style="color: white;">React, Next.js, Native</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Contact Section
    st.markdown("""
    <div style="background: rgba(30, 33, 48, 0.6); backdrop-filter: blur(10px); padding: 50px 20px; text-align: center; border-radius: 15px; max-width: 600px; margin: 30px auto;">
        <h2 style="color: white; margin-bottom: 20px;">Transform Your Crowd Management</h2>
        <div style="max-width: 400px; margin: 0 auto;">
            <input type="text" placeholder="Name" style="width: 100%; margin-bottom: 15px; padding: 12px; background: rgba(45, 55, 72, 0.5); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; color: white;"/>
            <input type="email" placeholder="Email" style="width: 100%; margin-bottom: 15px; padding: 12px; background: rgba(45, 55, 72, 0.5); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; color: white;"/>
            <textarea placeholder="Organization" style="width: 100%; margin-bottom: 15px; padding: 12px; background: rgba(45, 55, 72, 0.5); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; color: white; min-height: 100px;"></textarea>
            <button style="width: 100%; background-color: #FF6B00; color: white; border: none; padding: 12px; border-radius: 8px; font-weight: bold; transition: all 0.3s;">
                Request Demo
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div style="background-color: #0F172A; color: rgba(255,255,255,0.6); padding: 20px; text-align: center;">
        © 2025 CrowdSense. All Rights Reserved.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()