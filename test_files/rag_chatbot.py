import os
from dotenv import load_dotenv
from google import genai
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key

# ── Step 1: Load the PDF ──────────────────────────
print("Loading PDF...")
loader = PyPDFLoader("document.pdf")
pages = loader.load()
print(f"Loaded {len(pages)} pages")

# ── Step 2: Split into chunks ─────────────────────
print("Splitting into chunks...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(pages)
print(f"Created {len(chunks)} chunks")

# ── Step 3: Store in vector database ─────────────
print("Storing in vector database...")
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vectorstore = Chroma.from_documents(chunks, embeddings)
print("Vector database ready")

# ── Step 4: Chat loop ─────────────────────────────
client = genai.Client(api_key=api_key)

print("\nRAG Chatbot ready! Ask anything about your document.")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    relevant_chunks = vectorstore.similarity_search(question, k=3)
    context = "\n\n".join([chunk.page_content for chunk in relevant_chunks])

    prompt = f"""You are a helpful assistant. Answer the question based ONLY on the context below.
If the answer is not in the context, say "I couldn't find that in the document."

Context:
{context}

Question: {question}

Answer:"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print(f"Bot: {response.text}\n")