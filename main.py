import openai

openai.api_key = ''

def generate_text(prompt, model="text-davinci-003", max_tokens=100, temperature=0.7):
    """
    Function to generate text using OpenAI's GPT models.
    :param prompt: The prompt or question to ask the model.
    :param model: The GPT model to use (e.g., text-davinci-003).
    :param max_tokens: Maximum number of tokens to generate.
    :param temperature: Controls randomness; lower values = more focused, higher values = more creative.
    :return: Generated text.
    """
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response.choices[0].text.strip()
if __name__ == "__main__":
    prompt = "Explain the importance of Natural Language Processing in AI."
    generated_text = generate_text(prompt)
    print("Generated Text:\n", generated_text)
