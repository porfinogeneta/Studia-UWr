import { useEffect, useState } from "react"
import { DeleteIcon, EditIcon } from "../assets/Icons/Icons"
import { Book } from "../types/types"




export default function Table({books, handleDelete, handleUpdate}: {books: Book[], handleDelete: (id: string) => void, handleUpdate: (id: string) => void}) {

    const [amountPerPage, setAmountPerPage] = useState<number>(5)
    const [currentPage, setCurrentPage] = useState<number>(0)
    


    const handlePrevPage = () => {
        setCurrentPage(prev => (prev === 0 ? 0 : prev - 1))
    }

    const handleNextPage = () => {
        setCurrentPage(prev => (prev === Math.floor(books.length / amountPerPage) ? prev : prev + 1))
    }


    // da się to zrobić bez useEffect?
    useEffect(() => {
        if (currentPage > 0 && currentPage + 1 > Math.ceil(books.length / amountPerPage)) {
            setCurrentPage(currentPage - 1);
        }
    }, [books, currentPage, amountPerPage]);

    return (
       <div className=" flex min-h-96">
            <div className="mx-auto w-9/12">
                <h3 className="py-12 ml-4 text-stone-600 font-serif text-3xl">Your books</h3>
                {!books ? (<div>Loading...</div>) : (
                    <table className="table-fixed w-full border-collapse">
                        <thead className="my-8">
                            <tr>
                                <th className="border-2 border-orange-400 text-2xl py-4 font-bold">Title</th>
                                <th className="border-2 border-orange-400 text-2xl py-4 font-bold">Published</th>
                                <th className="border-2 border-orange-400 text-2xl py-4 font-bold">Copies</th>
                                <th className="border-2 border-orange-400 text-2xl py-4 font-bold">Price</th>
                                <th className="border-2 border-orange-400 text-2xl py-4 font-bold">Genre</th>
                                <th className="border-2 border-orange-400 text-2xl py-4 font-bold">Add / Del</th>
                            </tr>
                        </thead>
                        <tbody>
                            {books.slice(currentPage * amountPerPage, currentPage * amountPerPage + amountPerPage).map((b) => (
                                <tr key={b.id}>
                                    <td className="p-4 border border-orange-200 truncate" >{b.title}</td>
                                    <td className="p-4 border border-orange-200">{b.year}</td>
                                    <td className="p-4 border border-orange-200">{b.copies}</td>
                                    <td className="p-4 border border-orange-200">{b.price} {!b?.currency ? "USD" : b.currency}</td>
                                    <td className="p-4 border border-orange-200">{b.genre.name}</td>
                                    <td className="p-4 border border-orange-200 flex justify-evenly">
                                        <button onClick={() => handleDelete(b.id)}><DeleteIcon size={24}/></button>
                                        <button onClick={() => handleUpdate(b.id)}><EditIcon size={24}/></button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
                <div className="text-right">
                    <button onClick={handlePrevPage} className=" m-4 border-orange-400 border-2 px-2 py-1 rounded">Previous</button>
                    <button onClick={handleNextPage} className=" m-4 border-orange-400 border-2 px-2 py-1 rounded">Next</button>
                    <p>{currentPage + 1} of {Math.ceil(books.length / amountPerPage)}</p>
                </div>
                
            </div>
       </div> 
    )
}