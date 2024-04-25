import { ReactNode } from "react";


export default function Section({id, title, children}: {id: string, title: string, children: ReactNode}) {
    return (
      <section className="py-10 odd:bg-gray-300 even:bg-gray-200 dark:even:bg-gray-600 dark:odd:bg-gray-800" id={id}>
            <div className="max-w-4xl mx-auto px-4">
                <h2 className="text-5xl font-extrabold mb-6">{title}</h2>
                <div>{children}</div>
            </div>
        </section>
    )
}