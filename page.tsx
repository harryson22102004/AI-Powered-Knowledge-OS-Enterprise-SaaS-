"use client"
import { useState } from "react"

export default function Home() {
  const [query, setQuery] = useState("")
  const [response, setResponse] = useState("")

  async function askAI() {
    const res = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    })

    const data = await res.json()
    setResponse(data.answer)
  }

  return (
    <div>
      <h1>CortexFlow AI</h1>
      <textarea onChange={e => setQuery(e.target.value)} />
      <button onClick={askAI}>Ask</button>
      <p>{response}</p>
    </div>
  )
}
