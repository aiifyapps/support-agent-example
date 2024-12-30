## Support agent with documentation example

In this example, you will find a very simple app that allows you to chat with LLM, but the answers are grounded with data from your documentation.

### Running the example
- Ensure you have Python 3 and pip installed on your machine.

- Install Ollama and ensure the `all-minilm` and `llama3.2` models are available on your machine:
```bash
# Pulling the models
ollama pull all-minilm
ollama pull llama3.2
```

- Navigate to the project folder.

- Use the provided Docker Compose file (with Milvus standalone and Attu) located in the project root:

```bash
# Running the docker
docker compose up -d
```

- Create a Python virtual environment:

```bash
# Create virtual environment (-m is for python module)
mkdir -p .venv
python -m venv .venv
```

- Activate the Python virtual environment:

```bash
# Activate virtual environment
source .venv/bin/activate
```

- Install Python dependencies:

```bash
# Install dependecies from requirements.txt
pip install -r requirements.txt
```

- Create a .env file in the project root
```bash
# You have an example of env file name .env.dist you can start from it
cp .env.dist .env
```

### Running the scripts

1. Run the start.py script

This script splitts your document into chunks, creates embeddings, and inserts the embeddings into the database:

```bash
# Running the script
./start.py
```

2. Run the ask.py script

This script performs a chat with LLM but it will first provide the data from your documentation:
```bash
# Running the script
./ask.py
```

###### HAPPY CODING!