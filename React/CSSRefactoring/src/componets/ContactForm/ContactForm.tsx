import classes from "./styles.module.scss"

export default function ContactForm() {

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
      };

    return (
        <form onSubmit={handleSubmit} className={classes.contact_form}>
            <div className={classes.form_group}>
            <input type="text" placeholder="Name" required />
            </div>
            <div className={classes.form_group}>
            <input type="email" placeholder="Email" required />
            </div>
            <div className={classes.form_group}>
            <textarea rows={5} placeholder="Message" required></textarea>
            </div>
            <button type="submit">Send Message</button>
        </form>
    )
}