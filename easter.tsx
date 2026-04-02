import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import easterBg from "@/assets/easter-bg.jpg";

const EXPIRATION = new Date(2026, 3, 6, 18, 0); // April 6, 2026 6PM

const FloatingEmoji = ({ emoji, delay, x }: { emoji: string; delay: number; x: number }) => (
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
            setTimeLeft(`${d}d ${h}h ${m}m ${s}s`);
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
            <div className="flex min-h-screen items-center justify-center bg-muted">
                <motion.div
                    initial={{ scale: 0.8, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    className="text-center p-12 rounded-2xl bg-card shadow-lg"
                >
                    <p className="text-6xl mb-4">🌙</p>
                    <h1 className="text-2xl font-bold text-foreground mb-2">This Easter greeting has expired.</h1>
                    <p className="text-muted-foreground">See you next year! 🐣</p>
                </motion.div>
            </div>
        );
    }

    return (
        <div className="relative min-h-screen overflow-hidden bg-background">
            {/* Background image */}
            <div className="absolute inset-0">
                <img src={easterBg} alt="" className="w-full h-full object-cover opacity-40" />
                <div className="absolute inset-0 bg-gradient-to-b from-background/60 via-transparent to-background/80" />
            </div>

            {/* Floating emojis */}
            <div className="absolute inset-0 overflow-hidden">{floaters}</div>

            {/* Content */}
            <div className="relative z-10 flex min-h-screen items-center justify-center px-4 py-12">
                <motion.div
                    initial={{ y: 40, opacity: 0, scale: 0.95 }}
                    animate={{ y: 0, opacity: 1, scale: 1 }}
                    transition={{ duration: 0.8, ease: "easeOut" }}
                    className="max-w-xl w-full"
                >
                    <div className="rounded-3xl bg-card/80 backdrop-blur-xl p-8 md:p-12 shadow-2xl border border-border text-center">
                        <motion.div
                            animate={{ y: [0, -12, 0] }}
                            transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                            className="text-7xl md:text-8xl mb-6"
                        >
                            🐣
                        </motion.div>

                        <motion.h1
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.3 }}
                            className="text-4xl md:text-5xl font-extrabold text-foreground mb-4"
                            style={{ fontFamily: "'Georgia', serif" }}
                        >
                            Happy Easter! 🌷
                        </motion.h1>

                        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.5 }} className="space-y-4">
                            <p className="text-lg md:text-xl text-foreground/80 leading-relaxed">
                                Wishing you a joyful and blessed Easter season filled with love, hope, and happiness!
                            </p>
                            <div className="h-px bg-border my-6" />
                            <p className="text-muted-foreground text-sm italic">Best regards,</p>
                            <p className="text-xl font-semibold text-primary">Okiror Innocent</p>
                        </motion.div>

                        {/* Countdown */}
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            transition={{ delay: 0.8 }}
                            className="mt-8 py-3 px-5 rounded-xl bg-primary/10 inline-block"
                        >
                            <p className="text-xs text-muted-foreground uppercase tracking-wider mb-1">Greeting expires in</p>
                            <p className="text-lg font-mono font-bold text-primary">{timeLeft}</p>
                        </motion.div>
                    </div>
                </motion.div>
            </div>
        </div>
    );
};

export default Index;
