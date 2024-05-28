import {useQuery} from "@tanstack/react-query"

async function fetchBooks() {    
    const res = await fetch("http://localhost:3000/books?_expand=genre")
    console.log("eeee");
    
    return await res.json()
}

function useGetBooks() {
    return useQuery({
        queryKey: ["books", "list"],
        queryFn: () => fetchBooks()
    })
}

export default useGetBooks;