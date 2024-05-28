export default function Navbar({handleOpenModal}: {handleOpenModal: () => void}) {


    const handleOpenAddBookModal = () => {
        handleOpenModal()
    }

    return (
        <nav className="bg-orange-300 py-4 flex justify-between">
            <h1 className="ml-4 text-stone-600 font-serif text-5xl">Bookwormy</h1>
            <div className="">
                <button onClick={handleOpenAddBookModal} className="bg-lime-500 py-2 px-2 rounded text-slate-100 text-right mr-8">Add Book</button>
            </div>
    
        </nav>
    )
}