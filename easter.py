import streamlit as st
import streamlit.components.v1 as components

# 1. PASTE YOUR IMAGE URL HERE
# Make sure it starts with https://
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
        body, html { height: 100vh; margin: 0; overflow: hidden; font-family: 'Georgia', serif; background-color: #f8fafc; }
        
        /* Background Image Styling */
        .bg-img { 
            position: absolute; 
            inset: 0; 
            width: 100%; 
            height: 100%; 
            object-fit: cover; 
            opacity: 0.5; 
            z-index: 0;
        }
        
        .gradient-overlay { 
            position: absolute; 
            inset: 0; 
            background: linear-gradient(to bottom, rgba(255,255,255,0.7), transparent, rgba(255,255,255,0.9)); 
            z-index: 1;
        }

        /* Card Styling */
        .card { 
            position: relative; 
            z-index: 20; 
            background: rgba(255,255,255,0.8); 
            backdrop-filter: blur(12px); 
            padding: 3.5rem 2rem; 
            border-radius: 2.5rem; 
            box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15); 
            text-align: center; 
            max-width: 550px; 
            width: 90%; 
            border: 1px solid rgba(255,255,255,0.4); 
        }

        /* Floating Animation for the Main Emoji */
        .main-emoji { 
            animation: bounce 3s ease-in-out infinite; 
            font-size: 6rem; 
            margin-bottom: 1.5rem; 
            display: inline-block;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-25px); }
        }

        /* Floating Background Emojis */
        .floating-bg {
            position: absolute;
            font-size: 2rem;
            opacity: 0.6;
            z-index: 10;
            animation: rise 10s linear infinite;
        }

        @keyframes rise {
            from { transform: translateY(110vh) rotate(0deg); opacity: 0; }
            50% { opacity: 1; }
            to { transform: translateY(-20vh) rotate(360deg); opacity: 0; }
        }
    </style>
</head>
<body class="flex items-center justify-center">
    <!-- Background Elements -->
    <img src="IMAGE_PLACEHOLDER" class="bg-img" alt="Easter Background">
    <div class="gradient-overlay"></div>
    
    <!-- Floating Emojis Container -->
    <div id="emoji-container"></div>

    <!-- Main Card Content -->
    <div class="card">
        <div class="main-emoji">CHICK</div>
        <h1 class="text-4xl md:text-6xl font-extrabold text-gray-900 mb-6">
            Happy Easter! TULIP
        </h1>
        <p class="text-xl md:text-2xl text-gray-800 leading-relaxed mb-8">
            Wishing you a joyful and blessed Easter season filled with love, hope, and happiness!
        </p>
        
        <div class="h-px bg-gray-300 w-full mb-8"></div>
        
        <p class="text-gray-500 text-sm italic mb-1">Best regards,</p>
        <p class="text-3xl font-bold text-blue-600">Okiror Innocent</p>
    </div>

    <script>
        // Logic to create random floating background emojis
        const container = document.getElementById('emoji-container');
        const emojis = ['🐣', '🌷', '🥚', '🐰', '🌸', '🦋', '✨', '🌼'];
        
        function createEmoji() {
            const el = document.createElement('div');
            el.className = 'floating-bg';
            el.innerHTML = emojis[Math.floor(Math.random() * emojis.length)];
            el.style.left = Math.random() * 100 + 'vw';
            el.style.animationDuration = (Math.random() * 5 + 7) + 's'; // 7-12 seconds
            container.appendChild(el);
            
            // Clean up old emojis
            setTimeout(() => el.remove(), 12000);
        }

        // Start creating floating background emojis
        setInterval(createEmoji, 1500);
    </script>
</body>
</html>
"""

# Replace placeholders
final_html = HTML_CODE.replace("IMAGE_PLACEHOLDER", MY_IMAGE_URL)
final_html = final_html.replace("CHICK", E_CHICK).replace("TULIP", E_TULIP)

st.set_page_config(page_title="Happy Easter!", layout="wide")

# Remove Streamlit UI elements for a "Clean" link appearance
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0 !important;}
        iframe {border: none;}
    </style>
""", unsafe_allow_html=True)

# Render the final greeting
components.html(final_html, height=900, scrolling=False)
