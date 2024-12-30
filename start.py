#!/usr/bin/env python

import db
import embeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Database connect
db.connect()

# Create and select collection
db.createCollection("knowledege")
knowledge = db.Collection("knowledege")

loader = PyPDFLoader('knowledge-source/Tuscon.pdf')
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1200,
    chunk_overlap=120,
)

pages = loader.load_and_split(splitter)

documentEmbeddings = []

count = 0
for page in pages:
    count += 1
    print(f"Embedding the page number: {count}")
    documentEmbeddings.append({
        "representation": page.page_content,
        "embedding": embeddings.getEmbedding(page.page_content)
    })


print("Inserting into database")
db.insertEmbeddings(knowledge, documentEmbeddings)

print("Loading the collection")
knowledge.load()

