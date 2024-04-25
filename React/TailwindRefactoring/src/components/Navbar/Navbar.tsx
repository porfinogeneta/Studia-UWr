import { useState } from "react"


export default function Navbar({toggleTheme}: {toggleTheme: (mode: boolean) => void}) {

    const [darkMode, setDarkMode] = useState(false)

    const toggle = () => {
        setDarkMode(!darkMode)
        toggleTheme(darkMode)
    }
    return (
        <div className="sticky top-0 py-2.5 mb-7 dark:text-white text-black text-center z-50 bg-gray-200 dark:bg-gray-800">
            <a href="#header" className="px-4">Home</a>
            <a href="#about" className="px-4">About</a>
            <a href="#services" className="px-4">Services</a>
            <a href="#team" className="px-4">Team</a>
            <a href="#blog" className="px-4">Blog</a>
            <a href="#contact" className="px-4">Contact</a>
            <button onClick={toggle} className="px-4 py-2 transition-colors
             duration-300 text-white dark:text-black bg-gray-950 hover:bg-slate-800 dark:bg-gray-300 dark:hover:bg-gray-400">
                {darkMode ? "Light Mode" : "Dark Mode"}
            </button>
        </div>
            
        
    )
}