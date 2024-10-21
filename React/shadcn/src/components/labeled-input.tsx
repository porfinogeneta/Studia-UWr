'use client'

import * as React from "react"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

export function LabeledInput() {
  return (
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
      />
    </div>
  )
}