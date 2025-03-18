"use client";

import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import ModelInputs from "@/components/ModelInputs";

export default function Page() {
  const text = "Lets get started...";
  const [displayedText, setDisplayedText] = useState("");
  const [isTypingDone, setIsTypingDone] = useState(false); // New state

  useEffect(() => {
    let i = 0;
    const interval = setInterval(() => {
      if (i < text.length) {
        setDisplayedText(text.slice(0, i + 1));
        i++;
      } else {
        clearInterval(interval);
        setIsTypingDone(true); // Set to true when typing is done
      }
    }, 150);

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <div
        className="h-[70px] pl-[50px] pr-[50px] space-x-[20px] justify-between items-center flex flex-row 
  bg-gradient-to-b from-[#38261d] via-[#2a1e17cc] to-[#00000000]"
      >
        {/* Logo Section */}
        <motion.div
          className="overflow-hidden cursor-pointer font-bold"
          initial={{ clipPath: "inset(0% 50% 0% 50%)", opacity: 0 }}
          animate={{ clipPath: "inset(0% 0% 0% 0%)", opacity: 1 }}
          transition={{ duration: 1, ease: [0.25, 0.46, 0.45, 0.94] }}
          whileHover={{ scale: 1.05 }}
        >
          <img
            src="/logo.avif"
            alt="Logo"
            className="h-[70px] w-[200px] object-contain"
          />
        </motion.div>
        <motion.div
          className="text-[30px] mt-[15px] pr-[80px] overflow-hidden cursor-pointer "
          initial={{ clipPath: "inset(0% 50% 0% 50%)", opacity: 0 }}
          animate={{ clipPath: "inset(0% 0% 0% 0%)", opacity: 1 }}
          transition={{ duration: 1, ease: [0.25, 0.46, 0.45, 0.94] }}
          whileHover={{ scale: 1.05 }}
        >
          Find your Score
        </motion.div>

        {/* Login Button with Highlight Animation */}
        <motion.button
          className="w-[100px] mt-[15px] h-[40px] bg-[#05070b] border border-[#404040] text-white 
    transition-[background-color,transform] duration-400 ease-[cubic-bezier(0.25,0.46,0.45,0.94)] 
    hover:bg-[#ff793f] hover:scale-105 active:bg-[#cc6133] rounded-lg shadow-md cursor-pointer"
          animate={
            isTypingDone
              ? {
                  backgroundColor: ["#05070b", "#ff793f", "#05070b"], 
                  scale: [1, 1.05, 1], // Slight bounce
                }
              : {}
          }
          transition={
            isTypingDone
              ? {
                  repeat: Infinity,
                  duration: 5,
                  ease: "easeInOut",
                }
              : {}
          }
        >
          Login
        </motion.button>
      </div>

      <div className="flex flex-col justify-center items-center mt-[100px]">
        <h1 className="text-[50px] text-transparent bg-clip-text bg-gradient-to-r from-orange-100 to-orange-300 font-bold text-center leading-[1.2] max-w-[850px] mx-auto">
          AI-Powered Resume Scoring: <br />
          <span className="block text-center">
            {" "}
            See How Well You Match the Job!
          </span>
        </h1>

        <motion.img
          src="/rotatingAI.avif"
          alt="Rotating AI"
          className="h-[300px] w-[300px] object-contain mt-[30px] z-[-1]"
          animate={{
            rotateZ: [360, 0],
          }}
          transition={{
            repeat: Infinity,
            duration: 15,
            ease: "linear",
          }}
        />
      </div>

      {/* Typing Text Animation */}
      <motion.div
        className="text-[40px] mt-[80px] text-transparent bg-clip-text bg-gradient-to-r from-orange-100 to-orange-300 font-bold text-center leading-[1.2] mx-auto"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.5 }}
      >
        {displayedText}
        <motion.span
          className="inline-block"
          animate={{ opacity: [0, 1, 0] }}
          transition={{ repeat: Infinity, duration: 0.8 }}
        >
          |
        </motion.span>
      </motion.div>
      <div>
        <ModelInputs />
      </div>
    </div>
  );
}
