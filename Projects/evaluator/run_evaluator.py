from langsmith import Client
import os
from chatbot.main import chat_bot
from evaluator.evaluator import correctness

LANGSMITH_PROJECT = os.getenv(
    "LANGSMITH_PROJECT",
    "chatbot-evaluation")

client = Client()

DATASET_NAME = "chatbot-evaluation"


def target(inputs: dict) -> dict:
    question = inputs["question"]
    answer = chat_bot(question)

    return {"response": answer}


if __name__ == "__main__":
    results = client.evaluate(
        target,
        data=DATASET_NAME,
        evaluators=[correctness],
        experiment_prefix="chatbot-v1",
        metadata={
            "project": LANGSMITH_PROJECT
        }
    )

    print("Evaluation completed.")
    print(results)