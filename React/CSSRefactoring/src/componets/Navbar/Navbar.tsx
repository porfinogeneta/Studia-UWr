import { useState } from "react"
import classes from "./styles.module.scss"

export default function Navbar({toggleTheme}: {toggleTheme: (mode: boolean) => void}) {

    const [darkMode, setDarkMode] = useState(false)

    const toggle = () => {
        setDarkMode(!darkMode)
        toggleTheme(darkMode)
    }
    return (
        <div className={classes.navbar}>
            <a href="#header">Home</a>
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#team">Team</a>
            <a href="#blog">Blog</a>
            <a href="#contact">Contact</a>
            <button onClick={toggle} className={classes.theme_toggle_button}>
            {darkMode ? "Light Mode" : "Dark Mode"}
            </button>
        </div>        
    )
}