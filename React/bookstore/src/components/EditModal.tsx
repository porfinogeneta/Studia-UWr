import useGetOne from "../hooks/useGetOne"
import usePut from "../hooks/usePut"
import { Book } from "../types/types"

import Form from "./Form"

export default function EditModal({bookId, handleCloseModal}: {bookId: string, handleCloseModal: () => void}) {


    const book = useGetOne(bookId)
    const mutation = usePut()

    const editBook = (bk: Book) => {
        mutation.mutate(bk)
    }
    
    
    return (
        <div className="z-0 absolute inset-0 flex justify-center items-center" style={{ backgroundColor: 'rgba(0, 0, 0, 0.25)' }}>
            {book.isFetched && (<Form handleCloseModal={handleCloseModal} modifyBook={editBook} book={book.data}/>)} 
        </div>
        
    )
}