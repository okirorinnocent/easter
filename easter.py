import streamlit as st
import streamlit.components.v1 as components

# Emoji Unicode
E_CHICK = "\U0001F423"
E_TULIP = "\U0001F337"

HTML_CODE = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://tailwindcss.com"></script>
    <link href="https://googleapis.com" rel="stylesheet">
    <style>
        body, html {{ 
            height: 100vh; margin: 0; padding: 0; overflow: hidden; 
            font-family: 'Inter', sans-serif;
        }}
        
        /* OUTSTANDING ANIMATED MESH GRADIENT */
        .animated-bg {{
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            z-index: -1;
            background: linear-gradient(135deg, #fce7f3 0%, #fef3c7 50%, #dcfce7 100%);
            background-size: 400% 400%;
            animation: gradientMove 15s ease infinite;
        }}

        @keyframes gradientMove {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        /* GLASSMORPHISM CARD */
        .card {{ 
            position: relative; 
            z-index: 20; 
            background: rgba(255, 255, 255, 0.4);
            backdrop-filter: blur(30px) saturate(150%); 
            -webkit-backdrop-filter: blur(30px) saturate(150%);
            padding: 5rem 3rem; 
            border-radius: 4rem; 
            box-shadow: 0 40px 100px -20px rgba(0,0,0,0.1), inset 0 0 0 1px rgba(255,255,255,0.6); 
            text-align: center; 
            max-width: 650px; 
            width: 90%; 
            animation: cardFadeIn 1.5s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        @keyframes cardFadeIn {{
            from {{ transform: scale(0.9); opacity: 0; }}
            to {{ transform: scale(1); opacity: 1; }}
        }}

        .main-emoji {{ 
            animation: floatEmoji 4s ease-in-out infinite; 
            font-size: 8rem; 
            display: inline-block;
            filter: drop-shadow(0 20px 20px rgba(0,0,0,0.1));
        }}

        @keyframes floatEmoji {{ 
            0%, 100% {{ transform: translateY(0); }} 
            50% {{ transform: translateY(-30px); }} 
        }}

        .title {{
            font-family: 'Playfair Display', serif;
            color: #1e293b;
            letter-spacing: -0.05em;
        }}

        .floating-bg {{ 
            position: absolute; 
            font-size: 2.5rem; 
            z-index: 5; 
            animation: rise 15s linear infinite; 
            pointer-events: none;
            opacity: 0.6;
        }}

        @keyframes rise {{ 
            from {{ transform: translateY(110vh) rotate(0deg); opacity: 0; }} 
            20% {{ opacity: 0.6; }} 
            80% {{ opacity: 0.6; }}
            to {{ transform: translateY(-20vh) rotate(360deg); opacity: 0; }} 
        }}
    </style>
</head>
<body class="flex items-center justify-center">
    <div class="animated-bg"></div>
    <div id="emoji-container"></div>

    <div class="card">
        <div class="main-emoji">{E_CHICK}</div>
        <h1 class="title text-6xl md:text-8xl font-black mb-6">
            Happy Easter!
        </h1>
        <p class="text-2xl md:text-3xl text-slate-700 font-medium leading-relaxed mb-12 italic opacity-80">
            "Wishing you a joyful and blessed Easter season filled with love, hope, and happiness!"
        </p>
        
        <div class="flex items-center justify-center gap-4 mb-10 opacity-30">
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
            el.style.animationDuration = (Math.random() * 5 + 10) + 's';
            container.appendChild(el);
            setTimeout(() => el.remove(), 16000);
        }}
        setInterval(createEmoji, 2000);
    </script>
</body>
</html>
"""

st.set_page_config(page_title="Happy Easter!", layout="wide")

# Remove Streamlit UI
st.markdown("""
    <style>
        header, footer, #MainMenu {visibility: hidden;}
        .block-container {padding: 0 !important;}
        iframe {border: none; width: 100vw; height: 100vh;}
    </style>
""", unsafe_allow_html=True)

components.html(HTML_CODE, height=1200, scrolling=False)
