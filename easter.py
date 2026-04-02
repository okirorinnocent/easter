import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# 1. Provide the name of your image file here
# Make sure this file is in the SAME folder as your easter.py
IMAGE_FILENAME = "easter-bg.jpg"


def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return f"data:image/jpeg;base64,{base64.b64encode(img_file.read()).decode()}"
    return ""


# Convert your local image to a string
img_base64 = get_base64_image(IMAGE_FILENAME)

# Unicode Emojis
E_CHICK = "\U0001F423"
E_TULIP = "\U0001F337"

HTML_CODE = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://tailwindcss.com"></script>
    <style>
        body, html {{ height: 100vh; margin: 0; overflow: hidden; font-family: 'Georgia', serif; background-color: #f8fafc; }}
        
        .bg-img {{ 
            position: fixed; 
            top: 0; left: 0;
            width: 100vw; height: 100vh; 
            object-fit: cover; 
            opacity: 0.9; /* High visibility */
            z-index: -2;
        }}
        
        .overlay {{ 
            position: fixed; 
            inset: 0; 
            background: rgba(0, 0, 0, 0.15); 
            z-index: -1;
        }}

        .card {{ 
            position: relative; 
            z-index: 20; 
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(8px); 
            padding: 3rem 2rem; 
            border-radius: 2.5rem; 
            box-shadow: 0 20px 50px rgba(0,0,0,0.3); 
            text-align: center; 
            max-width: 500px; 
            width: 90%; 
            border: 2px solid rgba(255,255,255,0.5); 
        }}

        .main-emoji {{ animation: bounce 3s ease-in-out infinite; font-size: 5rem; display: inline-block; }}
        @keyframes bounce {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-20px); }} }}
        .floating-bg {{ position: absolute; font-size: 2rem; z-index: 10; animation: rise 8s linear infinite; }}
        @keyframes rise {{ from {{ transform: translateY(110vh) rotate(0deg); opacity: 0; }} 20% {{ opacity: 1; }} to {{ transform: translateY(-20vh) rotate(360deg); opacity: 0; }} }}
    </style>
</head>
<body class="flex items-center justify-center">
    <img src="{img_base64}" class="bg-img">
    <div class="overlay"></div>
    <div id="emoji-container"></div>

    <div class="card">
        <div class="main-emoji">{E_CHICK}</div>
        <h1 class="text-4xl md:text-5xl font-extrabold text-gray-900 mb-4">Happy Easter! {E_TULIP}</h1>
        <p class="text-lg md:text-xl text-gray-700 leading-relaxed mb-6">
            Wishing you a joyful and blessed Easter season filled with love, hope, and happiness!
        </p>
        <div class="h-px bg-gray-200 w-full mb-6"></div>
        <p class="text-gray-400 text-xs uppercase tracking-widest mb-1">Best regards</p>
        <p class="text-3xl font-bold text-blue-600">Okiror Innocent</p>
    </div>

    <script>
        const container = document.getElementById('emoji-container');
        const emojis = ['🐣', '🌷', '🥚', '🐰', '🌸', '🦋', '✨', '🌼'];
        function createEmoji() {{
            const el = document.createElement('div');
            el.className = 'floating-bg';
            el.innerHTML = emojis[Math.floor(Math.random() * emojis.length)];
            el.style.left = Math.random() * 100 + 'vw';
            el.style.animationDuration = (Math.random() * 4 + 6) + 's';
            container.appendChild(el);
            setTimeout(() => el.remove(), 9000);
        }}
        setInterval(createEmoji, 1500);
    </script>
</body>
</html>
"""

st.set_page_config(page_title="Happy Easter!", layout="wide")
st.markdown(
    "<style>header, footer, #MainMenu {visibility: hidden;} .block-container {padding:0;}</style>", unsafe_allow_html=True)

# If the image failed to load, show a warning
if not img_base64:
    st.error(f"Image file '{IMAGE_FILENAME}' not found in the directory.")

components.html(HTML_CODE, height=1000)
