import { useRecipes } from '../provider/RecipeContext';
import Recipe from './Recipe';

export default function RecipesList() {

  const {recipes, query, likedOnly} = useRecipes()
 
  const ShowRightRecipes = () => {    
    let displayedRecipes = recipes.filter(r => r.title.toLocaleLowerCase().includes(query)
     || r.desc.toLocaleLowerCase().includes(query))
    if (likedOnly){      
      displayedRecipes = displayedRecipes.filter(r => r.liked == true)
    }

    return displayedRecipes
  }

  return (
    <ul>
      {ShowRightRecipes().map((recipe) => (
        <li key={recipe.id}>
          <Recipe recipe={recipe}/>
        </li>
      ))}
    </ul>
  );
}