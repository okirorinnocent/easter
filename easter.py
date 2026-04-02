import streamlit as st
import streamlit.components.v1 as components

# 1. Background Image (Change this URL to your desired image)
BG_URL = "https://unsplash.com"

# Emoji Unicode Escapes to avoid Python-level character errors
E_CHICK = "\U0001F423"
E_TULIP = "\U0001F337"
E_EGG = "\U0001F95A"
E_RABBIT = "\U0001F430"
E_FLOWER = "\U0001F338"
E_BUTTERFLY = "\U0001F98B"
E_SPARKLE = "\U00002728"
E_DAISY = "\U0001F33C"
E_MOON = "\U0001F319"

HTML_CODE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script crossorigin src="https://tailwindcss.com"></script>
    <script crossorigin src="https://unpkg.com"></script>
    <script crossorigin src="https://unpkg.com"></script>
    <script crossorigin src="https://unpkg.com"></script>
    <script crossorigin src="https://unpkg.com"></script>
    <style>
        body, html, #root { height: 100vh; margin: 0; padding: 0; overflow: hidden; background: transparent; }
    </style>
</head>
<body>
    <div id="root"></div>
    <script type="text/babel">
        const { useState, useEffect } = React;
        const { motion } = FramerMotion;

        const EXPIRATION = new Date(2026, 3, 6, 18, 0); 

        const FloatingEmoji = ({ emoji, delay, x }) => (
            <motion.span
                className="absolute text-3xl md:text-5xl pointer-events-none select-none"
                initial={{ y: "110vh", x: `${x}vw`, opacity: 0, rotate: 0 }}
                animate={{ y: "-20vh", opacity: [0, 1, 1, 0], rotate: 360 }}
                transition={{ duration: 8, delay, repeat: Infinity, ease: "easeOut" }}
                style={{ left: `${x}%` }}
            >
                {emoji}
            </motion.span>
        );

        const Index = () => {
            const [timeLeft, setTimeLeft] = useState("");
            const [expired, setExpired] = useState(false);

            useEffect(() => {
                const tick = () => {
                    const now = new Date();
                    if (now > EXPIRATION) {
                        setExpired(true);
                        return;
                    }
                    const diff = EXPIRATION.getTime() - now.getTime();
                    const d = Math.floor(diff / 86400000);
                    const h = Math.floor((diff % 86400000) / 3600000);
                    const m = Math.floor((diff % 3600000) / 60000);
                    const s = Math.floor((diff % 60000) / 1000);
                    setTimeLeft(`${d}d ${h}h ${m}m ${s}s`);
                };
                tick();
                const id = setInterval(tick, 1000);
                return () => clearInterval(id);
            }, []);

            const emojis = ["CHICK", "TULIP", "EGG", "RABBIT", "FLOWER", "BUTTERFLY", "SPARKLE", "DAISY"];
            const floaters = emojis.flatMap((e, i) =>
                [0, 1].map((j) => (
                    <FloatingEmoji key={`${i}-${j}`} emoji={e} delay={i * 1.2 + j * 4} x={8 + ((i * 12 + j * 6) % 84)} />
                ))
            );

            if (expired) {
                return (
                    <div className="flex h-screen items-center justify-center">
                        <motion.div initial={{ scale: 0.8, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} className="text-center p-12 rounded-2xl bg-white shadow-lg">
                            <p className="text-6xl mb-4">MOON</p>
                            <h1 className="text-2xl font-bold text-gray-800 mb-2">This Easter greeting has expired.</h1>
                            <p className="text-gray-500">See you next year! CHICK</p>
                        </motion.div>
                    </div>
                );
            }

            return (
                <div className="relative h-screen w-full overflow-hidden">
                    <div className="absolute inset-0">
                        <img src="BG_LINK" className="w-full h-full object-cover opacity-40" alt="" />
                        <div className="absolute inset-0 bg-gradient-to-b from-white/60 via-transparent to-white/80" />
                    </div>
                    
                    <div className="absolute inset-0">{floaters}</div>

                    <div className="relative z-10 flex h-full items-center justify-center px-4">
                        <motion.div 
                            initial={{ y: 20, opacity: 0 }} 
                            animate={{ y: 0, opacity: 1 }}
                            className="max-w-md w-full bg-white/90 backdrop-blur-lg p-8 rounded-3xl shadow-2xl border border-white/20 text-center"
                        >
                            <div className="text-6xl md:text-8xl mb-6">CHICK</div>
                            <h1 className="text-4xl md:text-5xl font-extrabold text-gray-900 mb-4" style={{ fontFamily: "'Georgia', serif" }}>
                                Happy Easter! TULIP
                            </h1>
                            <div className="space-y-4">
                                <p className="text-lg md:text-xl text-gray-800 leading-relaxed">
                                    Wishing you a joyful and blessed Easter season filled with love, hope, and happiness!
                                </p>
                                <div className="h-px bg-gray-200 my-6" />
                                <p className="text-gray-500 text-sm italic">Best regards,</p>
                                <p className="text-xl font-semibold text-blue-600">Okiror Innocent</p>
                            </div>
                            
                            <div className="mt-8 py-3 px-5 rounded-xl bg-blue-50 inline-block">
                                <p className="text-xs text-blue-400 uppercase tracking-wider mb-1">Greeting expires in</p>
                                <p className="text-lg font-mono font-bold text-blue-600">{timeLeft}</p>
                            </div>
                        </motion.div>
                    </div>
                </div>
            );
        };

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<Index />);
    </script>
</body>
</html>
"""

# Replace markers with actual values
final_html = HTML_CODE.replace("BG_LINK", BG_URL)
final_html = final_html.replace("CHICK", E_CHICK).replace(
    "TULIP", E_TULIP).replace("EGG", E_EGG)
final_html = final_html.replace("RABBIT", E_RABBIT).replace(
    "FLOWER", E_FLOWER).replace("BUTTERFLY", E_BUTTERFLY)
final_html = final_html.replace("SPARKLE", E_SPARKLE).replace(
    "DAISY", E_DAISY).replace("MOON", E_MOON)

# Streamlit App Setup
st.set_page_config(page_title="Easter Greeting", layout="wide")

# Hide default Streamlit padding and menu for a clean look
st.markdown("""
    <style>
        .block-container { padding: 0 !important; }
        footer { visibility: hidden; }
        #MainMenu { visibility: hidden; }
        header { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# Render the interactive greeting
components.html(final_html, height=800, scrolling=False)
