import streamlit as st
import streamlit.components.v1 as components
import requests
import base64

# 1. FIXED RAW URL: GitHub "blob" links do not work for images.
# "://githubusercontent.com" is the only way to get the actual image data.
RAW_IMAGE_URL = "https://://githubusercontent.com/okirorinnocent/easter/main/easter-bg.jpg"


def get_base64_from_url(url):
    try:
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

HTML_CODE = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://googleapis.com" rel="stylesheet">
    <style>
        body, html {{ 
            height: 100vh; margin: 0; padding: 0; overflow: hidden; 
            background-color: #0f172a; 
        }}
        
        /* High-Definition Background */
        .bg-container {{
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background-image: url('data:image/jpeg;base64,{img_b64}');
            background-size: cover;
            background-position: center;
            z-index: -1;
            filter: brightness(0.85) contrast(1.1) saturate(1.2);
            transition: all 0.5s ease;
        }}

        /* Subtle Animated Gradient Overlay */
        .overlay {{
            position: fixed;
            inset: 0;
            background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(0,0,0,0.3) 100%);
            z-index: 0;
        }}
        
        /* Competition-Level Glassmorphism Card */
        .card {{ 
            position: relative; 
            z-index: 20; 
            background: rgba(255, 255, 255, 0.4);
            backdrop-filter: blur(25px) saturate(180%); 
            -webkit-backdrop-filter: blur(25px) saturate(180%);
            padding: 5rem 3rem; 
            border-radius: 4rem; 
            box-shadow: 0 50px 100px -20px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.5); 
            text-align: center; 
            max-width: 650px; 
            width: 90%; 
            animation: cardAppear 1.2s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        @keyframes cardAppear {{
            from {{ transform: translateY(50px); opacity: 0; }}
            to {{ transform: translateY(0); opacity: 1; }}
        }}

        .main-emoji {{ 
            animation: floatEmoji 4s ease-in-out infinite; 
            font-size: 8rem; 
            display: inline-block;
            filter: drop-shadow(0 20px 20px rgba(0,0,0,0.3));
        }}

        @keyframes floatEmoji {{ 0%, 100% {{ transform: translateY(0) rotate(-5deg); }} 50% {{ transform: translateY(-40px) rotate(5deg); }} }}

        .title {{
            font-family: 'Playfair Display', serif;
            background: linear-gradient(to bottom, #1e293b, #475569);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        /* Elegant Floating background emojis */
        .floating-bg {{ 
            position: absolute; 
            font-size: 2.5rem; 
            z-index: 5; 
            animation: rise 15s linear infinite; 
            pointer-events: none;
            filter: drop-shadow(0 10px 10px rgba(0,0,0,0.15));
        }}

        @keyframes rise {{ 
            from {{ transform: translateY(110vh) rotate(0deg) scale(0.5); opacity: 0; }} 
            10% {{ opacity: 0.7; }} 
            90% {{ opacity: 0.7; }}
            to {{ transform: translateY(-20vh) rotate(720deg) scale(1.2); opacity: 0; }} 
        }}
    </style>
</head>
<body class="flex items-center justify-center">
    <div class="bg-container"></div>
    <div class="overlay"></div>
    <div id="emoji-container"></div>

    <div class="card">
        <div class="main-emoji">{E_CHICK}</div>
        <h1 class="title text-6xl md:text-8xl font-black mb-6 tracking-tighter">
            Happy Easter!
        </h1>
        <p class="text-2xl md:text-3xl text-slate-800 font-medium leading-relaxed mb-12 italic opacity-90" style="font-family: 'Inter', sans-serif;">
            "Wishing you a joyful and blessed Easter season filled with love, hope, and happiness!"
        </p>
        
        <div class="flex items-center justify-center gap-4 mb-10 opacity-40">
            <div class="h-[2px] bg-slate-800 w-16"></div>
            <div class="text-slate-800 text-lg">{E_TULIP}</div>
            <div class="h-[2px] bg-slate-800 w-16"></div>
        </div>
        
        <p class="text-slate-500 text-sm uppercase tracking-[0.5em] font-bold mb-3">Best regards</p>
        <p class="text-5xl font-black text-blue-900 tracking-tight" style="font-family: 'Playfair Display', serif;">
            Okiror Innocent
        </p>
    </div>

    <script>
        const container = document.getElementById('emoji-container');
        const emojis = ['🐣', '🌷', '🥚', '🐰', '🌸', '🦋', '✨', '🌼'];
        function createEmoji() {{
            const el = document.createElement('div');
            el.className = 'floating-bg';
            el.innerHTML = emojis[Math.floor(Math.random() * emojis.length)];
            el.style.left = (Math.random() * 100) + 'vw';
            el.style.animationDuration = (Math.random() * 8 + 10) + 's';
            container.appendChild(el);
            setTimeout(() => el.remove(), 18000);
        }}
        setInterval(createEmoji, 2500);
    </script>
</body>
</html>
"""

st.set_page_config(page_title="Happy Easter!", layout="wide")

# Total Removal of Streamlit UI
st.markdown("""
    <style>
        header, footer, #MainMenu {visibility: hidden;}
        .block-container {padding: 0 !important;}
        iframe {border: none; width: 100vw; height: 100vh;}
        body {background-color: #0f172a;}
    </style>
""", unsafe_allow_html=True)

if img_b64:
    components.html(HTML_CODE, height=1200, scrolling=False)
else:
    st.error(
        "Competition Error: Background image could not be fetched. Check the GitHub URL.")
