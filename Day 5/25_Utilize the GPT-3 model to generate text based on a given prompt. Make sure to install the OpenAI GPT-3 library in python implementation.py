import openai

# Set your OpenAI GPT-3 API key
openai.api_key = 'your-api-key'

# Define a prompt for text generation
prompt = "Once upon a time, in a land far, far away,"

# Generate text using GPT-3
response = openai.Completion.create(
    engine="text-davinci-002",  # You can choose a different engine
    prompt=prompt,
    max_tokens=100  # You can adjust the desired length of the generated text
)

# Extract and print the generated text
generated_text = response['choices'][0]['text']
print("Generated Text:")
print(generated_text)
