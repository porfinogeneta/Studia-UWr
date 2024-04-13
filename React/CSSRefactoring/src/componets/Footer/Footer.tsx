import classes from "./styles.module.scss"

export default function Footer({name}: {name: string}){
    return (
        <footer className={classes.footer}>
            <div className="footer-content">
            <p>
                &copy; {new Date().getFullYear()} {name}
            </p>
            </div>
        </footer>
    )
}