import PreviewGallery from "../../components/PreviewGallery/PreviewGallery"
import TechStack from "../../components/TechStack/TechStack"

export default function Projects() {

    const codeImgs = ["src/assets/codeImgs/c1.png", "src/assets/codeImgs/c2.png", "src/assets/codeImgs/c3.png"]

    const projects = [
        {
            name: "Fonts Maker",
            description: "Software utilizing Bezier Curves, that allows user to create custom fonts",
            tech: ["src/assets/tech/python.png", "src/assets/tech/tkinter.png"],
            code: "https://github.com/porfinogeneta/FontsMaker",
            preview: ["src/assets/preview/letter.png", "src/assets/preview/letter2.png"]
        },
        {
            name: "Spline Interpolation",
            description: "Software that utilizes Spline of 3rd order to recreate any writing",
            tech: ["src/assets/tech/python.png"],
            code: "https://github.com/porfinogeneta/SignatureRecreation",
            preview: ["src/assets/preview/nums1.png", "src/assets/preview/nums2.png"]
        },
        {
            name: "Blog for a friend",
            description: "Blog app, connected to external API, which allows user to make blog posts",
            tech: ["src/assets/tech/react.png", "src/assets/tech/js.png", "src/assets/tech/hygraph.png"],
            code: "https://github.com/porfinogeneta/blog",
            preview: ["src/assets/preview/blog1.png", "src/assets/preview/blog2.png"]
        }

    ]

    return (
        <div>
            <div className="flex justify-center content-center mx-auto my-20 text-center w-full md:w-1/2 mb-20 h-96">
                <h1 className="text-7xl font-bold my-auto w-full">Take a look at my projects!</h1>
            </div>
            {projects.map((p, idx) => (
                <div className="flex gap-5 mx-20 min-h-[60vh] my-24">
                    <div className=" w-1/3 flex-none">
                        <h3 className="text-5xl font-bold mb-12">{p.name}</h3>
                        <p className="w-2/3" >{p.description}</p>
                    </div>
                    <div className="w-2/3 min-h-60 grid grid-cols-5 grid-rows-5 gap-4">
                        <div className=" row-span-5 col-span-2">
                            <PreviewGallery urls={p.preview}/>
                        </div>
                        <div className="col-span-2 row-span-3 col-start-3 row-start-2">
                            <TechStack tech={p.tech}/>
                        </div>
                        <div className="row-span-3 col-start-5 row-start-3">
                            <a href={p.code} target="_blank">
                                <div style={{backgroundImage: `url(${codeImgs[idx % codeImgs.length]})`}}
                                className="w-full h-full bg-cover bg-center contrast-50 rounded hover:cursor-pointer"></div>
                            </a>
                            
                        </div>
                    </div>
                </div>
            ))}
        </div>
    )
}