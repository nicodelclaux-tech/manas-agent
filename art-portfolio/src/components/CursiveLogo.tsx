import React from 'react';
import { motion } from 'framer-motion';

export const CursiveLogo = () => {
  // SVG Path for "Art" in a cursive style
  // This is a simplified path represention
  const pathVariants = {
    hidden: { pathLength: 0, opacity: 0 },
    visible: {
      pathLength: 1,
      opacity: 1,
      transition: {
        pathLength: { duration: 2, ease: "easeInOut" },
        opacity: { duration: 0.01 }
      }
    }
  };

  return (
    <div className="flex items-center space-x-2">
      <svg
        width="120"
        height="50"
        viewBox="0 0 120 50"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        className="drop-shadow-sm"
      >
        <motion.path
          d="M10 35C15 35 20 15 25 5C28 -1 35 5 35 15C35 25 25 45 15 45C10 45 8 40 12 30C18 15 40 10 50 25C55 35 50 45 45 45M55 25C65 25 70 15 75 15M65 15L65 45M80 15C90 15 95 25 95 35C95 45 85 45 80 40C75 35 75 25 80 15ZM100 15C105 10 115 10 115 25C115 40 105 45 100 45"
          stroke="currentColor"
          strokeWidth="2.5"
          strokeLinecap="round"
          strokeLinejoin="round"
          variants={pathVariants}
          initial="hidden"
          animate="visible"
        />
      </svg>
    </div>
  );
};
