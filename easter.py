import streamlit as st
import streamlit.components.v1 as components

# 1. PASTE YOUR IMAGE URL HERE
MY_IMAGE_URL = "https://unsplash.com"

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
        body, html { height: 100vh; margin: 0; overflow: hidden; font-family: 'Georgia', serif; background-color: #000; }
        
        /* Background Image - High Visibility */
        .bg-img { 
            position: fixed; 
            top: 0;
            left: 0;
            width: 100vw; 
            height: 100vh; 
            object-fit: cover; 
            opacity: 0.85; /* Increased visibility */
            z-index: -2;
        }
        
        /* Darker overlay to make the white card pop against the bright image */
        .overlay { 
            position: fixed; 
            inset: 0; 
            background: rgba(0, 0, 0, 0.2); 
            z-index: -1;
        }

        .card { 
            position: relative; 
            z-index: 20; 
            background: rgba(255, 255, 255, 0.9); /* Solid enough to read text */
            backdrop-filter: blur(8px); 
            padding: 3rem 2rem; 
            border-radius: 2.5rem; 
            box-shadow: 0 20px 50px rgba(0,0,0,0.3); 
            text-align: center; 
            max-width: 500px; 
            width: 90%; 
            border: 2px solid rgba(255,255,255,0.5); 
        }

        .main-emoji { 
            animation: bounce 3s ease-in-out infinite; 
            font-size: 5rem; 
            display: inline-block;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }

        .floating-bg {
            position: absolute;
            font-size: 2rem;
            z-index: 10;
            animation: rise 8s linear infinite;
        }

        @keyframes rise {
            from { transform: translateY(110vh) rotate(0deg); opacity: 0; }
            20% { opacity: 1; }
            80% { opacity: 1; }
            to { transform: translateY(-20vh) rotate(360deg); opacity: 0; }
        }
    </style>
</head>
<body class="flex items-center justify-center">
    <img src="IMAGE_PLACEHOLDER" class="bg-img">
    <div class="overlay"></div>
    <div id="emoji-container"></div>

    <div class="card">
        <div class="main-emoji">CHICK</div>
        <h1 class="text-4xl md:text-5xl font-extrabold text-gray-900 mb-4">
            Happy Easter! TULIP
        </h1>
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
        function createEmoji() {
            const el = document.createElement('div');
            el.className = 'floating-bg';
            el.innerHTML = emojis[Math.floor(Math.random() * emojis.length)];
            el.style.left = Math.random() * 100 + 'vw';
            el.style.animationDuration = (Math.random() * 4 + 6) + 's';
            container.appendChild(el);
            setTimeout(() => el.remove(), 9000);
        }
        setInterval(createEmoji, 1000);
    </script>
</body>
</html>
"""

final_html = HTML_CODE.replace("IMAGE_PLACEHOLDER", MY_IMAGE_URL).replace(
    "CHICK", E_CHICK).replace("TULIP", E_TULIP)

st.set_page_config(page_title="Happy Easter!", layout="wide")
st.markdown(
    "<style>header, footer, #MainMenu {visibility: hidden;} .block-container {padding:0;}</style>", unsafe_allow_html=True)
components.html(final_html, height=1000)
