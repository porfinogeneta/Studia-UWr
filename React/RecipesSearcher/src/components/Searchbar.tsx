import "./components.css"
import { useState } from "react"
import { useRecipesDispatch } from "../provider/RecipeContext"

export default function Searchbar(){

    const [query, setQuery] = useState<string>("")
    const [toggleLiked, setToggleLiked] = useState(false)

    const dispatch = useRecipesDispatch()

    const handleSearchSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        console.log(query);
        
        event.preventDefault()
        dispatch({
            type: "queried",
            query: query.toLocaleLowerCase()
        })
    }

    const handleInput = (event: React.ChangeEvent<HTMLInputElement>) => {
        setQuery(event.target.value)
    }

    const handleToggleLiked = () => {
        setToggleLiked(!toggleLiked)
        dispatch({
            type: "likedOnly",
            likedOnly: toggleLiked
        })
    }

    return (
        <form onSubmit={handleSearchSubmit}>
            <input type="text" placeholder="Search" onChange={handleInput}></input>
            <button type="submit">Search</button>
            <button onClick={handleToggleLiked}>{toggleLiked == false ? "Liked" : "All"}</button>
        </form>
        
    )
}