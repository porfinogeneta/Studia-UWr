import { useState, useEffect, useRef } from "react";
import useGetGenres from "../hooks/useGetGenres";
import { Book, Genre } from "../types/types";

export default function Form({book, modifyBook, handleCloseModal}: {book: Book | undefined, modifyBook: (bk: Book) => void, handleCloseModal: () => void}) {

    const formRef = useRef<HTMLDivElement | null>(null)

    const initalGenre: Genre = {
        id: '',
        name: ''
    }

    const initialFormData: Book = {
        id: '',
        title: '',
        author: '',
        copies: 0,
        description: '',
        genre: initalGenre,
        genreId: '',
        price: 0,
        year: '',
        currency: 'USD'
    };
    

    const genres = useGetGenres()

        useEffect(() => {
            const handleClickOutside = (event: MouseEvent) => {
                if (formRef.current && !formRef.current.contains(event.target as Node)) {
                    handleCloseModal();
                }
            };
            document.addEventListener('click', handleClickOutside, true);
            
            return () => {
                document.removeEventListener('click', handleClickOutside, true);
            };

        
  }, [ formRef ]);


    const [formData, setFormData] = useState<Book>(
        book ? {...book} : initialFormData
    );

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };


    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        modifyBook(formData)
        // setFormData(initialFormData)
        handleCloseModal()
    };


    return(
        <div ref={formRef} className="rounded bg-orange-100 p-8 opacity-100 flex justify-center items-center">
            <form onSubmit={handleSubmit}>
                        <div className="my-3">
                            <label className="mx-4">Title:</label>
                            <input required type="text" name="title" value={formData.title} onChange={handleChange} className="w-3/4 bg-orange-100 border-2 rounded border-orange-200 p-2" />
                        </div>
                        <div className="my-3">
                            <label className="mx-4">Author:</label>
                            <input required type="text" name="author" value={formData.author} onChange={handleChange} className="w-3/4 bg-orange-100 border-2 rounded border-orange-200 p-2"  />
                        </div>
                        <div className="my-3">
                            <label className="mx-4">Copies:</label>
                            <input required type="number" name="copies" value={formData.copies} onChange={handleChange} className="bg-orange-100 border-2 rounded border-orange-200 p-2"  />
                        </div>
                        <div className="my-3">
                            <label  className="mx-4">Description:</label>
                            <textarea required name="description" value={formData.description} onChange={handleChange} className="bg-orange-100 border-2 rounded border-orange-200 p-2"  />
                        </div>
                        <div className="my-3">
                            <label className="mx-4">Genre:</label>
                            <select required name="genreId" value={formData.genreId} onChange={handleChange} className="bg-orange-100 border-2 rounded border-orange-200 p-2" >
                            <option value="">Select Genre</option>
                            {genres.isFetched && genres.data.map((g: Genre) => (
                                <option key={g.id} value={g.id}>{g.name}</option>
                            ))}
                            </select>
                        </div>
                        <div className="my-3">
                            <label className="mx-4">Price:</label>
                            <input required type="number" name="price" value={formData.price} onChange={handleChange} className="bg-orange-100 border-2 rounded border-orange-200 p-2" />
                        </div>
                        <div className="my-3">
                            <label className="mx-4">Year:</label>
                            <input required type="text" name="year" value={formData.year} onChange={handleChange} className="bg-orange-100 border-2 rounded border-orange-200 p-2"  />
                        </div>
                        <div className="my-3">
                            <label className="mx-4">Currency:</label>
                            <input required type="text" name="currency" value={formData.currency} onChange={handleChange} className="bg-orange-100 border-2 rounded border-orange-200 p-2" />
                        </div>
                        <button className="text-stone-100 px-4 py-2 rounded bg-orange-400" type="submit">
                            {book ? "Edit" : "Add"}
                        </button>
                    </form>
                </div>
    )
}