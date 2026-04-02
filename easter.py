import streamlit as st
import streamlit.components.v1 as components

# 1. Background Image
BACKGROUND_IMAGE_URL = "https://unsplash.com"

# Using hex codes for emojis to avoid Python encoding/SyntaxErrors during deployment
E_CHICK = "\U0001F423"
E_TULIP = "\U0001F337"
E_EGG = "\U0001F95A"
E_RABBIT = "\U0001F430"
E_FLOWER = "\U0001F338"
E_BUTTERFLY = "\U0001F98B"
E_SPARKLE = "\U00002728"
E_DAISY = "\U0001F33C"
E_MOON = "\U0001F319"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://unpkg.com/framer-motion@10.16.4/dist/framer-motion.js"></script>
    <style>
        body, html, #root { height: 100vh; margin: 0; overflow: hidden; background: white; }
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
                    setTimeLeft(`${d}d ${h}h ${m}s`);
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
                    <div className="flex min-h-screen items-center justify-center bg-gray-100">
                        <motion.div initial={{ scale: 0.8, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} className="text-center p-12 rounded-2xl bg-white shadow-lg">
                            <p className="text-6xl mb-4">MOON</p>
                            <h1 className="text-2xl font-bold text-gray-800 mb-2">This Easter greeting has expired.</h1>
                            <p className="text-gray-500">See you next year! CHICK</p>
                        </motion.div>
                    </div>
                );
            }

            return (
                <div className="relative h-screen w-full overflow-hidden bg-slate-50">
                    <div className="absolute inset-0">
                        <img src="BG_URL" className="w-full h-full object-cover opacity-40" />
                        <div className="absolute inset-0 bg-gradient-to-b from-white/60 via-transparent to-white/80" />
                    </div>
                    
                    <div className="absolute inset-0">{floaters}</div>

                    <div className="relative z-10 flex h-full items-center justify-center px-4">
                        <motion.div 
                            initial={{ y: 20, opacity: 0 }} 
                            animate={{ y: 0, opacity: 1 }}
                            className="max-w-md w-full bg-white/80 backdrop-blur-md p-8 rounded-3xl shadow-2xl border border-white/20 text-center"
                        >
                            <div className="text-6xl mb-4">CHICK</div>
                            <h1 className="text-4xl font-bold text-gray-800 mb-4">Happy Easter! TULIP</h1>
                            <p className="text-gray-600 mb-6">Wishing you a joyful and blessed season!</p>
                            <div className="h-px bg-gray-200 w-full mb-6" />
                            <p className="text-sm text-gray-500 italic">Best regards,</p>
                            <p className="text-lg font-bold text-blue-600 mb-6">Okiror Innocent</p>
                            
                            <div className="bg-blue-50 p-3 rounded-xl">
                                <p className="text-xs text-blue-400 uppercase">Expires in</p>
                                <p className="text-xl font-mono font-bold text-blue-600">{timeLeft}</p>
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

# Replace markers with emojis and background URL to avoid Python-level SyntaxErrors
final_html = HTML_TEMPLATE.replace("BG_URL", BACKGROUND_IMAGE_URL)
final_html = final_html.replace("CHICK", E_CHICK)
final_html = final_html.replace("TULIP", E_TULIP)
final_html = final_html.replace("EGG", E_EGG)
final_html = final_html.replace("RABBIT", E_RABBIT)
final_html = final_html.replace("FLOWER", E_FLOWER)
final_html = final_html.replace("BUTTERFLY", E_BUTTERFLY)
final_html = final_html.replace("SPARKLE", E_SPARKLE)
final_html = final_html.replace("DAISY", E_DAISY)
final_html = final_html.replace("MOON", E_MOON)

st.set_page_config(page_title="Easter Greeting", layout="wide")
components.html(final_html, height=800)
