import "./components.css"
import { useRecipesDispatch } from "../provider/RecipeContext";
import { RecipeType } from '../types/Recipe';

interface IProps {
    recipe: RecipeType
}

export default function Recipe({ recipe }: IProps){

    const dispatch = useRecipesDispatch()

    return (
        <div className={`${recipe.liked ? "liked" : ""} recipe`}>
            <div className="liking">
                <input
                    type="checkbox"
                    checked={recipe.liked}
                    onChange={e => {
                        dispatch({
                            type: "liked",
                            recipe: {
                                ...recipe,
                                liked: e.target.checked
                            }
                        })
                    }}
                />
            </div>
            <h3>{recipe.title}</h3>
            <p>{recipe.desc}</p>
            <p>{recipe.making}</p>
            <div>
                <button onClick={() => {
                    dispatch({
                    type: 'deleted',
                    id: recipe.id
                    });
                }}>
                    Delete
                </button>
            </div>
            
        </div>
    )

}