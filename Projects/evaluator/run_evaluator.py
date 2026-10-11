from langsmith import Client
from langsmith.evaluation import aevaluate
import os
from chatbot.main import chat_bot
from evaluator.evaluator import correctness
import asyncio

LANGSMITH_PROJECT = os.getenv(
    "LANGSMITH_PROJECT",
    "chatbot-evaluation")

client = Client()

DATASET_NAME = "clichatbot-evalation"

async def target(inputs: dict) -> dict:
    question = inputs["question"]

    answer = await chat_bot(question)

    return {"response": answer}


async def main():
    results = await aevaluate(
    target,
    data=DATASET_NAME,
    evaluators=[correctness],
    experiment_prefix="chatbot-v1",
)

    print("Evaluation completed!")
    print(results)


if __name__ == "__main__":
    asyncio.run(main())