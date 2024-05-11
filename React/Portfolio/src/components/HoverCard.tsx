import { ReactNode } from "react";

export default function HoverCard({url, children}: {url: string, children: ReactNode}) {
    return (
        <div className="relative w-11/12" >
            <div className="rounded absolute inset-0 z-10 bg-slate-700 flex 
            flex-col justify-center gap-5 px-5
            opacity-0 hover:opacity-100 bg-opacity-90 duration-300">
                {children}
            </div>
            <div className="rounded w-full h-full flex items-center justify-center overflow-hidden">
                <img src={url} className="object-cover object-center h-full w-full" alt="company image"/>
            </div>
        </div>
    )
}