from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.embeddings.create(
    input="Hello, I am Tej",
    model ="text-embedding-3-small"
)

# print(response)

print("embeddings ", response.data[0].embedding)
print("Length of embeddings ", len(response.data[0].embedding))