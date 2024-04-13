import { createContext, useContext, useReducer } from 'react';
import { RecipeType } from '../types/Recipe';

const initialState = {
  recipes: [
    { id: 0, title: 'A very nice Vegan dish', desc: "A beautiful description of the recipe", liked: false, making: "vegan making"},
    { id: 1, title: 'Good Italinan Pizza', desc: "Delicious mafia pizza", liked: true, making: "pizza making"}
  ],
  lastKey: 2,
  query: "",
  likedOnly: false
}


type state = {
  recipes: Array<RecipeType>,
  lastKey: number,
  query: string
  likedOnly: boolean
}

type RecipeAction = 
| {
  type: "added",
  id: number,
  title: string,
  desc: string,
  making: string
}
| {
  type: "liked",
  recipe:RecipeType
}
| {
  type: "deleted",
  id:number
}
| {
  type: "queried",
  query: string
}
| {
  type: "likedOnly",
  likedOnly: boolean
}




const RecipeContext = createContext(initialState)
const RecipeDispatchContext = createContext<React.Dispatch<any>|null>(null)

export function RecipeProvider({children}: {children?: React.ReactNode}) {
    const [state, dispatch] = useReducer(
        recipesReducer,
        initialState
    )

    return (
        <RecipeContext.Provider value={{...state}}>
          <RecipeDispatchContext.Provider
            value={dispatch}
          >
            {children}
          </RecipeDispatchContext.Provider>
        </RecipeContext.Provider>
      );
}

export function useRecipes() {
    return useContext(RecipeContext);
}


export function useRecipesDispatch() {
    const context = useContext(RecipeDispatchContext);
    if (context == null){
      throw Error
    }
    return context
}

function recipesReducer(state: state, action: RecipeAction) {
  
    switch (action.type) {
      case 'added': {
        return {
          ...state,
          recipes: [...state.recipes, {
            id: action.id,
            title: action.title,
            desc: action.desc,
            liked: false,
            making: action.making
          }],
          lastKey: state.lastKey + 1,
          query: ""
        }
      }
      case 'liked': {
        return {
          ...state,
          recipes: state.recipes.map(r => {
            if (r.id == action.recipe.id){
                return {...r, liked: !r.liked}
            }else {
              return r
            }
          })
        }
      }
      case 'deleted': {
        return {
          ...state,
          recipes: state.recipes.filter(r => r.id !== action.id)
        } ;
      }
      case 'queried': {
        return {
          ...state,
          query: action.query
        }
      }
      case 'likedOnly': {
        return {
          ...state,
          likedOnly: action.likedOnly
        }
      }
      // default: {
      //   throw Error('Unknown action: ' + action.type);
      // }
    }
  }


