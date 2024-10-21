import {useRef, useState} from "react"
import { useClickedOutside } from "../../hooks/useClickedOutside"

export default function PreviewGallery({urls} : {urls: string[]}) {

    const [selectedPhoto, setSelectedPhoto] = useState<string>("")
    const divRef = useRef(null)



    useClickedOutside(divRef, setSelectedPhoto)

    const handleClick = (url: string) => {
        setSelectedPhoto(selectedPhoto === url ? "" : url)
    }
    

    return (
        <div ref={divRef} className="grid auto-cols-fr w-full h-full">
            {urls.map((url, idx) => (
                <div 
                    key={idx} 
                    onClick={() => handleClick(url)}  
                    className="hover:cursor-pointer"
                >
                    <img 
                        className={`${url === selectedPhoto ? "scale-150 z-40" : "scale-100 z-0"}`} 
                        src={url} 
                        alt={`Preview ${idx + 1}`}
                    />
                </div>
            ))}
        </div>
    )
}
