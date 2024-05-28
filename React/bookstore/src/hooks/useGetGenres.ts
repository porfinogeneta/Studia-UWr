import {useQuery} from "@tanstack/react-query"

async function fetchGenres() {    
    const res = await fetch("http://localhost:3000/genres")
    return await res.json()
}

function useGetGenres() {
    return useQuery({
        queryKey: ["genres", "list"],
        queryFn: fetchGenres
    })
}

export default useGetGenres;