import streamlit as st
import streamlit.components.v1 as components

# 1. Image URL (Ensure it starts with https://)
BG_URL = "https://unsplash.com"

# Emoji Unicode
E_CHICK = "\U0001F423"
E_TULIP = "\U0001F337"

HTML_CODE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://tailwindcss.com"></script>
    <style>
        body, html { height: 100vh; margin: 0; overflow: hidden; font-family: 'Georgia', serif; }
        .bg-img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.4; }
        .gradient-overlay { position: absolute; inset: 0; background: linear-gradient(to bottom, rgba(255,255,255,0.6), transparent, rgba(255,255,255,0.8)); }
        .card { position: relative; z-index: 10; background: rgba(255,255,255,0.85); backdrop-filter: blur(10px); padding: 3rem; border-radius: 2rem; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25); text-align: center; max-width: 500px; width: 90%; border: 1px solid rgba(255,255,255,0.3); }
        .floating { animation: float 3s ease-in-out infinite; font-size: 5rem; margin-bottom: 1rem; }
        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }
    </style>
</head>
<body class="flex items-center justify-center bg-gray-100">
    <img src="BG_LINK" class="bg-img">
    <div class="gradient-overlay"></div>

    <div class="card">
        <div class="floating">CHICK</div>
        <h1 class="text-4xl md:text-5xl font-extrabold text-gray-900 mb-4">Happy Easter! TULIP</h1>
        <p class="text-lg text-gray-800 leading-relaxed mb-6">
            Wishing you a joyful and blessed Easter season filled with love, hope, and happiness!
        </p>
        <div class="h-px bg-gray-300 w-full mb-6"></div>
        <p class="text-gray-500 text-sm italic">Best regards,</p>
        <p class="text-2xl font-bold text-blue-600">Okiror Innocent</p>
        
        <div class="mt-8 py-3 px-5 rounded-xl bg-blue-50 inline-block">
            <p class="text-xs text-blue-400 uppercase tracking-wider mb-1">Greeting active until</p>
            <p class="text-lg font-mono font-bold text-blue-600">April 6, 2026</p>
        </div>
    </div>

    <!-- If this script runs, the "Blank" issue is fixed -->
    <script>
        console.log("Easter Greeting Script Loaded Successfully");
    </script>
</body>
</html>
"""

# Replace placeholders
final_html = HTML_CODE.replace("BG_LINK", BG_URL).replace(
    "CHICK", E_CHICK).replace("TULIP", E_TULIP)

st.set_page_config(page_title="Easter Greeting", layout="wide")

# Hide Streamlit elements
st.markdown(
    "<style>header, footer, #MainMenu {visibility: hidden;} .block-container {padding:0;}</style>", unsafe_allow_html=True)

# Render
components.html(final_html, height=800)
