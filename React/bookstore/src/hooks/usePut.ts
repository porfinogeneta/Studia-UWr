import { useMutation, useQueryClient } from "@tanstack/react-query";
import { Book } from "../types/types";


async function updateBook(book: Book) {
    const res = await fetch(`http://localhost:3000/books/${book.id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({...book})
    })
    return await res.json()
}

function usePut() {
    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: updateBook,
        onSuccess: () => {
            queryClient.invalidateQueries({
                queryKey: ["books", "list"]
            })
        }
    })
}

export default usePut