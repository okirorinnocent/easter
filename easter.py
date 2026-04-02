import streamlit as st
import streamlit.components.v1 as components
import requests
import base64

# 1. RAW IMAGE URL (Fixed to point directly to the file data)
RAW_IMAGE_URL = "https://githubusercontent.com"

def get_base64_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode()
    except Exception as e:
        return None
    return None

# Convert the image to a string for guaranteed display
img_b64 = get_base64_from_url(RAW_IMAGE_URL)

# Emoji Unicode
E_CHICK = "\U0001F423"
E_TULIP = "\U0001F337"

HTML_CODE = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://tailwindcss.com"></script>
    <style>
        body, html {{ height: 100vh; margin: 0; padding: 0; overflow: hidden; font-family: 'Georgia', serif; }}
        
        /* Background Image - Outstanding Clarity */
        .bg-container {{
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background-image: url('data:image/jpeg;base64,{img_b64}');
            background-size: cover;
            background-position: center;
            z-index: -1;
        }}
        
        /* Subtle card for readability */
        .card {{ 
            position: relative; 
            z-index: 20; 
            background: rgba(255, 255, 255, 0.88);
            backdrop-filter: blur(10px); 
            padding: 3.5rem 2rem; 
            border-radius: 2.5rem; 
            box-shadow: 0 30px 60px rgba(0,0,0,0.4); 
            text-align: center; 
            max-width: 550px; 
            width: 90%; 
            border: 1px solid rgba(255,255,255,0.4); 
        }}

        .main-emoji {{ 
            animation: bounce 3s ease-in-out infinite; 
            font-size: 6rem; 
            display: inline-block;
            margin-bottom: 1rem;
        }}

        @keyframes bounce {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-30px); }} }}

        .floating-bg {{ 
            position: absolute; 
            font-size: 2rem; 
            z-index: 5; 
            animation: rise 10s linear infinite; 
            pointer-events: none;
        }}

        @keyframes rise {{ 
            from {{ transform: translateY(110vh) rotate(0deg); opacity: 0; }} 
            20% {{ opacity: 0.8; }} 
            80% {{ opacity: 0.8; }}
            to {{ transform: translateY(-20vh) rotate(360deg); opacity: 0; }} 
        }
    </style>
</head>
<body class="flex items-center justify-center">
    <div class="bg-container"></div>
    <div id="emoji-container"></div>

    <div class="card">
        <div class="main-emoji">{E_CHICK}</div>
        <h1 class="text-4xl md:text-6xl font-extrabold text-gray-900 mb-6">
            Happy Easter! {E_TULIP}
        </h1>
        <p class="text-xl md:text-2xl text-gray-800 leading-relaxed mb-8">
            Wishing you a joyful and blessed Easter season filled with love, hope, and happiness!
        </p>
        
        <div class="h-px bg-gray-300 w-full mb-8"></div>
        
        <p class="text-gray-500 text-sm italic mb-1">Best regards,</p>
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
            el.style.animationDuration = (Math.random() * 5 + 7) + 's';
            container.appendChild(el);
            setTimeout(() => el.remove(), 12000);
        }}
        setInterval(createEmoji, 1500);
    </script>
</body>
</html>
"""

st.set_page_config(page_title="Happy Easter!", layout="wide")

# Hide Streamlit elements
st.markdown("""
    <style>
        header, footer, #MainMenu {visibility: hidden;}
        .block-container {padding: 0 !important;}
        iframe {border: none; width: 100vw; height: 100vh;}
    </style>
""", unsafe_allow_html=True)

if img_b64:
    components.html(HTML_CODE, height=1000, scrolling=False)
else:
    st.error("Could not load the image from GitHub. Check the URL!")
