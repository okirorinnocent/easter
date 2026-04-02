import streamlit as st
import streamlit.components.v1 as components

# Replace this URL with your actual background image link
BACKGROUND_IMAGE_URL = "https://unsplash.com"

# Note: We removed the 'f' from f''' to prevent Python from parsing the braces
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://tailwindcss.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>
    <style>
        body, html, #root { height: 100%; margin: 0; padding: 0; overflow: hidden; }
    </style>
</head>
<body>
    <div id="root"></div>
    <script type="text/babel">
        const { useState, useEffect } = React;
        const { motion, AnimatePresence } = FramerMotion;

        const EXPIRATION = new Date(2026, 3, 6, 18, 0); 

        const FloatingEmoji = ({ emoji, delay, x }) => (
            <motion.span
                className="absolute text-3xl md:text-5xl pointer-events-none select-none"
                initial={{ y: "100vh", x: `${x}vw`, opacity: 0, rotate: 0 }}
                animate={{ y: "-20vh", opacity: [0, 1, 1, 0], rotate: 360 }}
                transition={{ duration: 8, delay, repeat: Infinity, ease: "easeOut" }}
                style={{ left: `${x}%` }}
            >
                {emoji}
            </motion.span>
        );

        const Index = () => {
            const [expired, setExpired] = useState(false);
            const [timeLeft, setTimeLeft] = useState("");

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

            const emojis = ["🐣", "🌷", "🥚", "🐰", "🌸", "🦋", "✨", "🌼"];
            const floaters = emojis.flatMap((e, i) =>
                [0, 1].map((j) => (
                    <FloatingEmoji key={`${i}-${j}`} emoji={e} delay={i * 1.2 + j * 4} x={8 + ((i * 12 + j * 6) % 84)} />
                ))
            );

            if (expired) {
                return (
                    <div className="flex min-h-screen items-center justify-center bg-gray-100">
                        <motion.div initial={{ scale: 0.8, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} className="text-center p-12 rounded-2xl bg-white shadow-lg">
                            <p className="text-6xl mb-4">🌙</p>
                            <h1 className="text-2xl font-bold text-gray-800 mb-2">This Easter greeting has expired.</h1>
                            <p className="text-gray-500">See you next year! 🐣</p>
                        </motion.div>
                    </div>
                );
            }

            return (
                <div className="relative min-h-screen overflow-hidden bg-white">
                    <div className="absolute inset-0">
                        <img src="REPLACE_IMAGE_URL" alt="" className="w-full h-full object-cover opacity-40" />
                        <div className="absolute inset-0 bg-gradient-to-b from-white/60 via-transparent to-white/80" />
                    </div>
                    <div className="absolute inset-0 overflow-hidden">{floaters}</div>
                    <div className="relative z-10 flex min-h-screen items-center justify-center px-4 py-12">
                        <motion.div initial={{ y: 40, opacity: 0, scale: 0.95 }} animate={{ y: 0, opacity: 1, scale: 1 }} transition={{ duration: 0.8, ease: "easeOut" }} className="max-w-xl w-full">
                            <div className="rounded-3xl bg-white/80 backdrop-blur-xl p-8 md:p-12 shadow-2xl border border-gray-200 text-center">
                                <motion.div animate={{ y: [0, -12, 0] }} transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }} className="text-7xl md:text-8xl mb-6">🐣</motion.div>
                                <motion.h1 className="text-4xl md:text-5xl font-extrabold text-gray-900 mb-4" style={{ fontFamily: "'Georgia', serif" }}>Happy Easter! 🌷</motion.h1>
                                <div className="space-y-4">
                                    <p className="text-lg md:text-xl text-gray-800 leading-relaxed">Wishing you a joyful and blessed Easter season filled with love, hope, and happiness!</p>
                                    <div className="h-px bg-gray-200 my-6" />
                                    <p className="text-gray-500 text-sm italic">Best regards,</p>
                                    <p className="text-xl font-semibold text-blue-600">Okiror Innocent</p>
                                </div>
                                <div className="mt-8 py-3 px-5 rounded-xl bg-blue-50 inline-block">
                                    <p className="text-xs text-gray-500 uppercase tracking-wider mb-1">Greeting expires in</p>
                                    <p className="text-lg font-mono font-bold text-blue-600">{timeLeft}</p>
                                </div>
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
'''.replace("REPLACE_IMAGE_URL", BACKGROUND_IMAGE_URL)

# Streamlit setup
st.set_page_config(page_title="Easter Greeting", layout="wide")

# Hide Streamlit UI elements for a cleaner look
st.markdown(
    "<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}</style>", unsafe_allow_html=True)

# Render the component
components.html(HTML_TEMPLATE, height=1000, scrolling=False)
