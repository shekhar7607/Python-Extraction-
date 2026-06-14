from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer, util

reader = PdfReader("word.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"


 # characters

chunks = text.split("\n")



model = SentenceTransformer('all-MiniLM-L6-v2')


embeddings = model.encode(chunks)

print ("Embeddings:")
print(embeddings)

question = "What Ram is eating"
context = "\n".join(chunks)

query_embedding = model.encode(question)


prompt = f"""
Answer only Yes or No.

Context:
{context}

Question:
{question}
"""
scores = util.cos_sim(query_embedding, embeddings)

print(scores)
print(prompt)

best_index = scores.argmax()

print("Best Chunk:")
print(chunks[best_index])

