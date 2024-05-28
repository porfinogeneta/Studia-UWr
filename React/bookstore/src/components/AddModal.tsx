import usePost from "../hooks/usePost"
import { Book } from "../types/types"
import Form from "./Form"

export default function AddModal({handleCloseModal}: {handleCloseModal: () => void}) {

    const mutation = usePost()

    const addBook = (bk: Book) => {
        mutation.mutate(bk)
    }

    return (
        <div className="z-0 absolute inset-0 flex justify-center items-center" style={{ backgroundColor: 'rgba(0, 0, 0, 0.25)' }}>
            <Form handleCloseModal={handleCloseModal} modifyBook={addBook} book={undefined}/>
        </div>
        
    )
}