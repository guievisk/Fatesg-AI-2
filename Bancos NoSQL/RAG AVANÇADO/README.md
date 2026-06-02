# Advanced RAG: Pre-retrieval and Re-ranking

This repository contains the practical implementation of an **Advanced Retrieval-Augmented Generation (RAG)** pipeline. The project was developed to demonstrate how data preparation techniques and refined filtering can overcome the limitations of "Naive RAG," mitigating hallucinations and delivering highly relevant context to the LLM (Large Language Model).

## Architecture and Implemented Techniques

The application flow was structured into three main enhancement stages:

### 1. Pre-retrieval
* **Intelligent Chunking:** Utilization of the `RecursiveCharacterTextSplitter` to divide documents respecting the semantics of the text (such as paragraphs and periods).
* **Metadata Addition:** Structuring chunks with identifiers and tags, preparing the foundation for precise filtering before vector search.

### 2. Retrieval
* **Embeddings:** Generation of mathematical vectors using HuggingFace models (`all-MiniLM-L6-v2`).
* **Vector Database:** In-memory storage and fast similarity search (retrieving the *Top K* results) using **ChromaDB**.

### 3. Post-retrieval and Re-ranking
* **Cross-Encoder:** The core of the project. Application of the `ms-marco-MiniLM-L-6-v2` model (Sentence-Transformers) as a "judge" to re-evaluate the true relevance between the user's question and the passages retrieved by the database.
* **Rigorous Selection (Top N):** Extraction of only the perfect context and elimination of noise before constructing the final prompt, optimizing token usage and the AI's focus.

## Technologies Used

* **Language:** Python
* **Orchestration Framework:** LangChain
* **Vector Database:** ChromaDB
* **AI Models:** Sentence-Transformers (HuggingFace)

## How to Run the Project

The project was built in a notebook format, making it ideal for execution in **Google Colab** or **Jupyter Notebook / VS Code**.

1. Clone the repository to your environment:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)
