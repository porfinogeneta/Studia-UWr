import './App.css'
import AddRecipe from './components/AddRecipe'
import RecipesList from './components/RecipesList'
import Searchbar from './components/Searchbar'

import { RecipeProvider } from './provider/RecipeContext'

function App() {

  return (
      <RecipeProvider>
        <h1>Recipes</h1>
        <Searchbar/>
        <AddRecipe></AddRecipe>
        <RecipesList/>
      </RecipeProvider>
  )
}

export default App
