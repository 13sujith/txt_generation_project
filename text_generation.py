# text_generation.py

from transformers import pipeline

# Load the GPT-2 text generation pipeline
generator = pipeline('text-generation', model='gpt2')

def generate_paragraph(prompt, max_length=120):
    """Generate a paragraph on a given prompt using GPT-2."""
    results = generator(prompt, max_length=max_length, num_return_sequences=1)
    return results[0]['generated_text']

if __name__ == "__main__":
    user_prompt = input("Enter your topic or prompt: ")
    paragraph = generate_paragraph(user_prompt)
    print("\nGenerated Paragraph:\n")
    print(paragraph)
