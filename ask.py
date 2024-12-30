#!/usr/bin/env python

import os
import ollama
from pymilvus import Hit
import db
import embeddings
from langchain_community.document_loaders import PyPDFLoader
from openai import OpenAI
from dotenv import load_dotenv

# Database connect
db.connect()

# select collection
knowledge = db.Collection("knowledege")
knowledge.load()


def askLLM(question: str):
    embedding = embeddings.getEmbedding(question)

    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}

    searchResults = knowledge.search(
        data=[embedding],
        anns_field="embedding",
        param=search_params,
        limit=5,
        output_fields=['representation']  
    )

    context = ""
    for hits in searchResults:
        for hit in hits:    
            context += "\r\n" + hit.entity.get('representation') + "\r\n"


    prompt = f"""
    Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Answer the question like support agent. 
    Context: 
    {context}
    Question:
    {question}
    """

    response = ollama.generate(
        model='llama3.2',
        prompt=prompt
    )
    print("============================================\r\n")
    print("QUESTION:" + question + "\n\r")
    print("============================================\r\n")
    print(response.response)


print("Please, enter the search query and hit Enter key. \r\n")
print("To exit the app type 'quit' and hit Enter key. \r\n")

while True:
    term = input('Your query: ')

    if 'quit' == term:
        print("\r\nThank you for using this example app.\r\n")
        break

    askLLM(term)
