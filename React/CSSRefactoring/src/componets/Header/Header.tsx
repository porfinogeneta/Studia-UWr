import classes from "./styles.module.scss"

export default function Header({darkMode, children}: {darkMode: boolean, children: {name: string, slogan: string}}){
    return (
        <div className={`${darkMode ? classes.dark_theme : classes.light_theme}`}>
            <header id="header" className={classes.header}>
                <div className="header-content">
                <h1>{children.name}</h1>
                <p>{children.slogan}</p>
                </div>
            </header>
        </div>
        
    )
}