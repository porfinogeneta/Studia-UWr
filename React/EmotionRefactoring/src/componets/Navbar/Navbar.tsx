import { useState } from "react"
import styled from "@emotion/styled"


const NavbarStyle = styled.div`
    position: sticky;
    top: 0;
    padding: 10px 0;
    text-align: center;
    z-index: 1000;
    background-color: ${props => props.theme.navbarBg};
`

const ATagStyle = styled.a`
    text-decoration: none;
    padding: 0 20px;
    color: ${props => props.theme.link};
`

const ToggleButtonStyle = styled.button`
    cursor: pointer;
    padding: 10px 20px;
    transition: background-color 0.3s ease;
    background-color: ${props => props.theme.buttonBg};
    color: ${props => props.theme.toggleText};
    :hover {
        background-color: ${props => props.theme.buttonHover};
    }
`

export default function Navbar({toggleTheme}: {toggleTheme: (mode: boolean) => void}) {

    const [darkMode, setDarkMode] = useState(false)

    const toggle = () => {
        setDarkMode(!darkMode)
        toggleTheme(darkMode)
    }
    return (
        <NavbarStyle>
            <ATagStyle href="#header">Home</ATagStyle>
            <ATagStyle href="#about">About</ATagStyle>
            <ATagStyle href="#services">Services</ATagStyle>
            <ATagStyle href="#team">Team</ATagStyle>
            <ATagStyle href="#blog">Blog</ATagStyle>
            <ATagStyle href="#contact">Contact</ATagStyle>
            <ToggleButtonStyle onClick={toggle}>
                {darkMode ? "Light Mode" : "Dark Mode"}
            </ToggleButtonStyle>
        </NavbarStyle>
            
        
    )
}