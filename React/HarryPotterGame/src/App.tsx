import { useCallback, useEffect, useState } from 'react'

import './App.scss'
import Answers from './components/Answers/Answers'
import Loader from './components/Loader/Loader'


type PotionType = {
  id: string;
  characteristics: string;
  difficulty: string;
  effect: string;
  image: string;
  ingredients: string;
  inventors: string | null;
  manufacturers: string | null;
  name: string;
  side_effects: string | null;
  slug: string;
  time: string | null;
  wiki: string;

}

async function getPotions() {

  const urls = [
    "https://api.potterdb.com/v1/potions?page[number]=1",
    "https://api.potterdb.com/v1/potions?page[number]=2"
  ]

  const fetchData = (url: string) => fetch(url).then(response => response.json())

  const fetchPromises = urls.map(fetchData)


  try {
    const results = await Promise.all(fetchPromises)
    return results.flatMap(potionList => 
      potionList.data.map((p: {id: string, attributes: object}) => ({
        id: p.id,
        ...p.attributes
      }))
    )
  }catch(err) {
    throw err
  }

}

function App() {

  const [isLoading, setIsLoading] = useState<boolean>(false)
  const [potions, setPotions] = useState<PotionType[]>([])
  const [currentQuestion, setCurrentQuestion] = useState<number>(0)
  const [givenAnswer, setGivenAnswer] = useState<boolean>(true)

  // score
  const [score, setScore] = useState<number>(0)
  const [highScore, setHighScore] = useState(parseInt(localStorage.getItem("highscore") || "0", 10))


  const fetchData = useCallback(
    async function fetchPotionsData(ignore = false) {
      setIsLoading(true)
      const data: PotionType[] = await getPotions()
      
      if (!ignore){
        setPotions(data)
        setIsLoading(false)
      }
    },[]
  )

  useEffect(() => {
    
    let ignore = false

    fetchData(ignore)

    return () => {
      ignore = true
    }

  }, [fetchData])

  // funkcja generująca 4 indexy odpowiedzi
  const getAnswers = (idx: number) => {
    
    const indexes = Array.from({ length: potions.length }, (_, i) => i);

    for (let i = indexes.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [indexes[i], indexes[j]] = [indexes[j], indexes[i]];
    }

    const ans = [idx, ...indexes.slice(0, 3)]

    return ans
  }

  // co robimy z odpowiedziami gracza
  const handleAnswer = (ans: boolean) => {
    console.log(ans);
    // poprawna odpowiedź
    if (ans) {
      setCurrentQuestion(currentQuestion + 1)
      setGivenAnswer(true)
      // punkty
      setScore(prevScore => {
        console.log(highScore);
        const newPoints = prevScore + 1
        localStorage.setItem("highscore", newPoints.toString())
        setHighScore(Math.max(highScore, newPoints))
        return newPoints
      })
      
    }
    // błędna odpowiedź
    else {
      setGivenAnswer(false)
      setScore(0)
    }
  }


  return (
    <div className="container">
      <div className="game_container">
        {isLoading && <Loader/>}
        {!isLoading && potions.length > 0 &&
          <>
            <h1>Harry Potter Game</h1>
            <Answers
              answers={getAnswers(currentQuestion).map((a) => potions[a].name)} 
              question={potions[currentQuestion].effect}
              hasGivenAnswer={handleAnswer}
              />
              {!givenAnswer ?  <p className="wrong_answer">Wrong Answer!</p> : <></>}
              <div className="score_container">
                <p className="score">Score: {score}</p>
                <p style={{textAlign: "right"}} className="score">High Score: {highScore}</p>
              </div>
          </>
        }
        
      </div>
    </div>
  )
}

export default App
