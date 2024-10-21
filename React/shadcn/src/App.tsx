import './App.css'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { useState } from 'react'
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

function App() {

  const [count, setCount] = useState(0)

  const incrementCount = () => {
    setCount(prevCount => prevCount + 1)
  }

  return (
    <div className="flex flex-col items-center space-y-4">
      {/* <Button 
        onClick={incrementCount}
        variant={'outline'}
        size={'lg'}
        // className="rounded-full bg-secondary hover:bg-secondary/90 text-secondary-foreground px-6 py-3 text-lg font-medium transition-colors"
      >
        Increment
      </Button>
      <p className="text-xl font-semibold">Count: {count}</p>
      <div className="w-full max-w-sm">
        <Label
          htmlFor="textInput"
          className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1"
        >
          Enter your text
        </Label>
        <Input
          type="text"
          id="textInput"
          placeholder="Type here..."
          className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm placeholder-gray-400 dark:placeholder-gray-500 text-gray-900 dark:text-gray-100 bg-white dark:bg-gray-800 focus:ring-0 focus:border-gray-500 dark:focus:border-gray-400"
        /> */}
        <Card>
          <CardHeader>
            <CardTitle>Card Title</CardTitle>
            <CardDescription>Card Description</CardDescription>
          </CardHeader>
          <CardContent>
            <p>Card Content</p>
          </CardContent>
          <CardFooter>
            <p>Card Footer</p>
          </CardFooter>
        </Card>

    {/* </div> */}
    </div>
  )
}

export default App
