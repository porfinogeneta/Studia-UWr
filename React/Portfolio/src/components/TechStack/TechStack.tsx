export default function TechStack({tech} : {tech: string[]}) {
    return (
        <div className="w-full h-full grid place-items-center ">
            {tech.map((t, idx) => (
                <img key={idx} className="w-16 h-16" src={t}/>
            ))}
        </div>
    )
}