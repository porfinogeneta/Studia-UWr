import { useState } from 'react'
import Navbar from './components/Navbar'
import Table from './components/Table'
import useDelete from './hooks/useDelete'
import useGetBooks from './hooks/useGetBooks'
import EditModal from './components/EditModal'
import AddModal from './components/AddModal'
import DeleteNotification from './components/DeleteNotification'

function App() {

  const [isShowingModal, setIsShowingModal] = useState<boolean>(false)
  const [isShowingNotification, setIsShowingNotification] = useState<boolean>(false)
  const [bookToUpdate, setBookToUpdate] = useState<string | undefined>("")

  const mutation = useDelete()

  const books = useGetBooks()
  console.log(books.data);
  

  const bookDelete = (id: string) => {
    console.log(id);
    mutation.mutate(id)
    

    setIsShowingNotification(true)

    setTimeout(() => {
      setIsShowingNotification(false);
    }, 500);
  }


  const bookUpdate = (id: string) => {
    setIsShowingModal(true)
    setBookToUpdate(id)
  }
    

  const handleCloseModal = () => {    
    setIsShowingModal(false)
  }

  const handleOpenModal= () => {
    setIsShowingModal(true)
    setBookToUpdate(undefined)
  }




  return (
    <div className="relative h-lvh">
      <Navbar handleOpenModal={handleOpenModal}/>
      {books.isFetched ? <Table handleDelete={bookDelete} handleUpdate={bookUpdate} books={books.data}/> : "Loading"}
      {bookToUpdate && isShowingModal && (
        <EditModal bookId={bookToUpdate} handleCloseModal={handleCloseModal} />
      )}
      {!bookToUpdate && isShowingModal && (
        <AddModal handleCloseModal={handleCloseModal}/>
      )}
      {isShowingNotification ? <DeleteNotification/> : ""}
    </div>
  )
}

export default App
