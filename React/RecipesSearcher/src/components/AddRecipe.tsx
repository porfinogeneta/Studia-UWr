import { useState } from "react";
import { useRecipes, useRecipesDispatch } from "../provider/RecipeContext";


export default function AddRecipe() {
    const [title, setTitle] = useState<string>('')
    const [desc, setDesc] = useState<string>('')
    const [making, setMaking] = useState<string>('')

    const dispatch = useRecipesDispatch();

    const {lastKey} = useRecipes()

    const handleAdd = (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault()
      setTitle('')
      setDesc('')
      setMaking('')
      dispatch({
        type: 'added',
        id: lastKey,
        title,
        desc,
        making
      })
    }


    return (
        <>
        <form onSubmit={handleAdd}>
          <input
              placeholder="Name"
              value={title}
              onChange={e => setTitle(e.target.value)}
            />
            <input
              placeholder="Description"
              value={desc}
              onChange={e => setDesc(e.target.value)}
            />
            <input
              placeholder="Making"
              value={making}
              onChange={e => setMaking(e.target.value)}
            />
            <button type="submit">Add</button>
        </form>
        </>
      );
}