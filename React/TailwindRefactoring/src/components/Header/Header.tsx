


export default function Header({children}: {children: {name: string, slogan: string}}){
    return (
        <header className="pt-12 pb-8 text-center">
            <div className=" bg-gray-100 dark:bg-gray-900">
                <h1 className="text-6xl font-extrabold mb-6">{children.name}</h1>
                <p className="text-2xl">{children.slogan}</p>
            </div>
        </header>
        
    )
}