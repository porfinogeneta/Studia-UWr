
import { useMutation, useQueryClient } from "@tanstack/react-query";


async function deleteBook(id: string) {
    const res = await fetch(`http://localhost:3000/books/${id}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application.json",
        },
    })
    return await res.json()
}

function useDelete(){
    const queryClient = useQueryClient()

    return useMutation({
        mutationFn: deleteBook,
        onSuccess: () => {
            queryClient.invalidateQueries({
                queryKey: ["books", "list"]
            })
        }
    })
}

export default useDelete;