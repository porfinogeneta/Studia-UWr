import { ReactNode } from "react";
import classes from "./styles.module.scss"

export default function Section({id, title, children}: {id: string, title: string, children: ReactNode}) {
    return (
        <section id={id} className={classes.section}>
          <div className={classes.section_content}>
            <h2>{title}</h2>
            {children}
          </div>
        </section>
    )
}