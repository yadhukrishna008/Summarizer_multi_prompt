from fastapi import FastAPI
from app.schema import SummarizeRequest, SummarizeResponseList, prompts
import requests
from fastapi.middleware.cors import CORSMiddleware


app= FastAPI()

# Configure CORS (allows frontend to call API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.post("/summarize", response_model= SummarizeResponseList)
async def summarize_text(request: SummarizeRequest):
    results= []

    for prompt_template in prompts:
        prompt = prompt_template.replace("{TEXT}", request.text)

        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3:latest",
                "prompt": prompt,
                "stream": False
            })

        data = res.json()

        if "response" not in data:
            raise RuntimeError(f"Unexpected Ollama response: {data}")

        results.append(data["response"].strip())
    return {"summaries" : results}

