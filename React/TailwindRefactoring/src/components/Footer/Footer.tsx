


export default function Footer({name}: {name: string}){
    return (
        <footer className="py-8 text-center">
            <div>
                <p>
                    &copy; {new Date().getFullYear()} {name}
                </p>
            </div>
        </footer>
    )
}