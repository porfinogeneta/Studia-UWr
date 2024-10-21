import { useState, useEffect } from "react"
import styles from "./styles.module.scss"


type AnswersProps = {
    answers: string[],
    question: string,
    hasGivenAnswer: (ans: boolean) => void
}

// element 0 to zawsze odpowiedź
export default function Answers({answers, question, hasGivenAnswer}: AnswersProps) {

    const [wrongAnswers, setWrongAnswers] = useState<number[]>([])
    const [shuffledAns, setShuffledAns] = useState<string[]>([]);
    const [correctIdx, setCorrectIdx] = useState<number>(0)

    

    useEffect(() => {
        const correctAnswer = answers[0]
        const shuffledArray = shuffleArray(answers);
        setCorrectIdx(shuffledArray.indexOf(correctAnswer))
        setShuffledAns(shuffledArray);
        setWrongAnswers([])
    }, [question]);

    function shuffleArray(array: string[]) {
        for (let i = array.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }


    // sprawdzamy czy wybrana odpowiedź jest taka jak poprawna
    const handleChooseAnswer = (idx: number) => {
        
        if (idx === correctIdx){
            hasGivenAnswer(true)
        }else {
            const newArr = [...wrongAnswers, idx]
            setWrongAnswers(newArr)
            hasGivenAnswer(false)
        }
    }

    return (
        <div className={styles.container}>
            <h1>{question}</h1>
            <div className={styles.answersGrid}>
                {shuffledAns.map((a, i) => (
                    <button 
                    disabled={wrongAnswers.includes(i)} 
                    className={`${wrongAnswers.includes(i) ? styles.disabled : ''}`}
                    key={i} onClick={() => handleChooseAnswer(i)}>
                        {a}
                    </button>
                ))}
            </div>
            

            
        </div>
    )
}