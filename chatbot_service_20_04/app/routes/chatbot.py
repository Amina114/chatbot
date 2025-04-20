from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from langchain_ollama import OllamaLLM

router = APIRouter()

# Initialize the Ollama model
ollama_model = OllamaLLM(model="gemma2:2b")

class AnalyzeRequest(BaseModel):
    user_input: str

@router.post("/analyze")
async def analyze_text(request: AnalyzeRequest):
    """
    Analyze the user input text using the Gemma2:2b model.
    """
    try:
        # Check if input is empty
        if not request.user_input.strip():
            raise HTTPException(status_code=400, detail="Input text cannot be empty")
        
        # Generate a response using the model
        prompt = f"""
        Analyze the following text and extract the following information:
        1. Client: The name of the client mentioned in the text (if any).
        2. Label: The system, product, or feature mentioned in the text (if any).
        3. Severity: Whether the issue is severe or not.

        Text: "{request.user_input}"

        Return the result as a JSON object with keys: client, label, severity.
        """
        response = ollama_model.generate(prompt)
        return {"status": "success", "data": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")