import {useQuery} from "@tanstack/react-query"

async function fetchBooks(urls: string[]) {    
    // const booksPromise = fetch("http://localhost:3000/books?_embed=genre")
    // const genresPromise = fetch("http://localhost:3000/genres")
    const promiseUrls = urls.map((u) => fetch(u))
    // const res = await Promise.all([booksPromise, genresPromise])
    const res = await Promise.all(promiseUrls)
    const jsonPromises = res.map((v) => v.json())
    return await Promise.all(jsonPromises)
    // const [books, genres] = await Promise.all(jsonPromises)
    // return {books, genres}
}

function useGet(links: string[]) {
    return useQuery({
        queryKey: ["books", "list"],
        queryFn: () => fetchBooks(links)
    })
}

export default useGet;