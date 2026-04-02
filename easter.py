import streamlit as st
import streamlit.components.v1 as components
import requests
import base64

# 1. FIXED RAW URL: Points to the actual data, not the GitHub page
RAW_IMAGE_URL = "https://github.com/okirorinnocent/easter/blob/main/easter-bg.jpg"


def get_base64_from_url(url):
    try:
        # Adding a timeout and headers to ensure the request goes through
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode()
    except:
        return None
    return None


img_b64 = get_base64_from_url(RAW_IMAGE_URL)

# Emoji Unicode
E_CHICK = "\U0001F423"
E_TULIP = "\U0001F337"

# HTML Template with "Outstanding" Professional Styling
HTML_CODE = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body, html {{ 
            height: 100vh; margin: 0; padding: 0; overflow: hidden; 
            background-color: #1a1a1a; 
        }}
        
        .bg-container {{
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background-image: url('data:image/jpeg;base64,{img_b64}');
            background-size: cover;
            background-position: center;
            z-index: -1;
            filter: brightness(0.9) contrast(1.1); /* Professional color pop */
        }}
        
        /* Glassmorphism Card Effect */
        .card {{ 
            position: relative; 
            z-index: 20; 
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(20px); 
            -webkit-backdrop-filter: blur(20px);
            padding: 4rem 2.5rem; 
            border-radius: 3rem; 
            box-shadow: 0 40px 100px rgba(0,0,0,0.5); 
            text-align: center; 
            max-width: 600px; 
            width: 90%; 
            border: 1px solid rgba(255,255,255,0.3); 
        }}

        .main-emoji {{ 
            animation: bounce 4s ease-in-out infinite; 
            font-size: 7rem; 
            display: inline-block;
            filter: drop-shadow(0 10px 10px rgba(0,0,0,0.2));
        }}

        @keyframes bounce {{ 0%, 100% {{ transform: translateY(0) scale(1); }} 50% {{ transform: translateY(-30px) scale(1.05); }} }}

        .floating-bg {{ 
            position: absolute; 
            font-size: 2.5rem; 
            z-index: 5; 
            animation: rise 12s linear infinite; 
            pointer-events: none;
            filter: drop-shadow(0 5px 5px rgba(0,0,0,0.1));
        }}

        @keyframes rise {{ 
            from {{ transform: translateY(110vh) rotate(0deg); opacity: 0; }} 
            10% {{ opacity: 0.8; }} 
            90% {{ opacity: 0.8; }}
            to {{ transform: translateY(-20vh) rotate(360deg); opacity: 0; }} 
        }}
    </style>
</head>
<body class="flex items-center justify-center">
    <div class="bg-container"></div>
    <div id="emoji-container"></div>

    <div class="card">
        <div class="main-emoji">{E_CHICK}</div>
        <h1 class="text-5xl md:text-7xl font-black text-gray-900 mb-6 tracking-tight" style="font-family: 'Georgia', serif;">
            Happy Easter!
        </h1>
        <p class="text-xl md:text-2xl text-gray-800 font-medium leading-relaxed mb-10">
            Wishing you a joyful and blessed Easter season filled with love, hope, and happiness!
        </p>
        
        <div class="h-1 bg-gradient-to-r from-transparent via-gray-400 to-transparent w-full mb-10 opacity-30"></div>
        
        <p class="text-gray-600 text-sm uppercase tracking-[0.3em] font-bold mb-2">Best regards</p>
        <p class="text-4xl font-extrabold text-blue-700 drop-shadow-sm">Okiror Innocent</p>
    </div>

    <script>
        const container = document.getElementById('emoji-container');
        const emojis = ['🐣', '🌷', '🥚', '🐰', '🌸', '🦋', '✨', '🌼'];
        function createEmoji() {{
            const el = document.createElement('div');
            el.className = 'floating-bg';
            el.innerHTML = emojis[Math.floor(Math.random() * emojis.length)];
            el.style.left = Math.random() * 100 + 'vw';
            el.style.animationDuration = (Math.random() * 6 + 8) + 's';
            container.appendChild(el);
            setTimeout(() => el.remove(), 14000);
        }}
        // Adjust spawn rate for elegance
        setInterval(createEmoji, 2000);
    </script>
</body>
</html>
"""

st.set_page_config(page_title="Happy Easter!", layout="wide")

# Hide Streamlit UI completely
st.markdown("""
    <style>
        header, footer, #MainMenu {visibility: hidden;}
        .block-container {padding: 0 !important;}
        iframe {border: none; width: 100vw; height: 100vh;}
    </style>
""", unsafe_allow_html=True)

if img_b64:
    components.html(HTML_CODE, height=1200, scrolling=False)
else:
    # Error message if the URL failed
    st.error("Error: Background image failed to load. Please check your internet connection or the GitHub Raw URL.")
