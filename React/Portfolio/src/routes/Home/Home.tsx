import { FacebookIcon, GithubIcon, LinkedIn } from "../../assets/icons"
export default function Home() {
    return(
        <div className="min-h-screen flex gap-8 flex-col justify-center content-center text-center">
            <img className="w-72 mx-auto" src="src/assets/circle-galata.png" alt="me"/>
            <h1 className="mx-auto font-bold text-6xl text-indigo-400 mb-4">Szymon Mazurek</h1>
            <p className="mx-auto w-2/5">Student of Computer Science at the University of Wrocław. Passionate about learning new technologies and widening IT horizons.</p>
            <div className="mx-auto flex gap-8 justify-center w-1/3 h-8">
                <FacebookIcon/>
                <GithubIcon/>
                <LinkedIn/>
            </div>
        </div>
    ) 
}