import os
from google.genai import Client
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

judge_client = judge_client = Client(api_key=GEMINI_API_KEY)

def correctness(inputs, outputs, reference_outputs):
    question = inputs["question"]
    expected = reference_outputs["answer"]
    actual = outputs["response"]

    prompt = f"""
    You are an expert chatbot evaluator.

    Question: {question}
    Expected answer: {expected}
    Chatbot answer: {actual}

    Decide whether the chatbot answer is factually correct
    and answers the question consistently with the expected answer.

    Ignore minor wording differences.

    Reply with exactly one word: CORRECT or INCORRECT.
    """

    response = judge_client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    judgment = (response.text or "").strip().upper()

    if judgment not in {"CORRECT", "INCORRECT"}:
        raise ValueError(f"Unexpected judge response: {judgment}")

    return {
        "key": "correctness",
        "score": int(judgment == "CORRECT"),
        "comment": judgment
    }