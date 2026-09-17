import tiktoken

prompts = [
    "What is the capital of France?",
    "Explain quantum computing in simple terms.",
    "Write a 200-word essay on climate change..."
]

pricing = {
    "gpt-4o": 2.50,
    "claude-sonnet": 3.00,
}

def gptTokenizer(prompt):
    enc = tiktoken.encoding_for_model("gpt-4o")
    return len(enc.encode(prompt))

def anthropicTokenizer(prompt):
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(prompt))

def calculate(noTokenGpt,noTokenClaude):
    pricePertokenGpt = pricing["gpt-4o"]/1000000
    pricePertokenClaude = pricing["claude-sonnet"]/1000000

    print("OpenAi:\n","No Tokens:",noTokenGpt,"Pricing:",noTokenGpt*pricePertokenGpt)
    print("Anthropic:\n","No Tokens:",noTokenClaude,"Pricing:",noTokenClaude*pricePertokenClaude)

def main():
    for prompt in prompts:
        print(prompt)
        calculate(gptTokenizer(prompt),anthropicTokenizer(prompt))

if __name__ == "__main__":
    main()