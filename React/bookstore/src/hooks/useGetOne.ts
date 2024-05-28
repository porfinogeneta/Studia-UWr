import { useQuery } from "@tanstack/react-query";

async function fetchBook(id: string) {
  const res = await fetch(`http://localhost:3000/books/${id}`);
  return await res.json();
}

function useGetOne(id: string) {
  return useQuery({
    queryKey: ["books", "list", id],
    queryFn: () => fetchBook(id),
  });
}

export default useGetOne;