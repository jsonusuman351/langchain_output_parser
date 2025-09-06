# 🔧 LangChain Output Parsers: From Text to Structured Data

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python) ![LangChain](https://img.shields.io/badge/LangChain-0086CB?style=for-the-badge&logo=langchain)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-FFD61E?style=for-the-badge&logo=huggingface) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai) ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic)



Welcome to this practical guide on using **Output Parsers** in LangChain! This repository tackles a fundamental challenge in AI development: Large Language Models (LLMs) naturally produce unstructured text, but real-world applications require structured, predictable data for tasks like database entries, API calls, or agentic workflows.

This collection of scripts demonstrates how to use various output parsers to transform raw LLM string outputs into clean, usable formats like strings, JSON, or Pydantic objects.

---

### 🤔 The Problem: Unstructured Text

While modern LLMs like OpenAI's GPT-4 can be forced into JSON mode using `with_structured_output`, many models cannot. When a model only returns a string, how can we reliably get structured data from it?

**This is where Output Parsers shine.** They take the raw string output from an LLM and parse it into a desired format, often by dynamically injecting formatting instructions into the prompt itself.

---

### ✨ Core Concepts Demonstrated

This repository explores the most essential output parsers available in LangChain, each suited for a different task:

1.  **`StrOutputParser`**:
    -   The most basic parser. It simply takes the LLM's output and returns it as a standard Python `str`.
    -   **Use Case**: Ideal for simple Q&A bots or when you just need the raw text response without any special formatting.

2.  **`JsonOutputParser`**:
    -   A powerful parser that instructs the LLM to generate a JSON string and then safely parses it into a Python `dict`.
    -   **Use Case**: Perfect for when you need a dictionary but don't require strict validation. Great for extracting multiple, loosely-defined fields.

3.  **`PydanticOutputParser`**:
    -   The most robust and recommended method for complex data. You define a Pydantic model as your desired schema, and the parser not only extracts the data but also **validates** it against your model.
    -   **Use Case**: Essential for production applications where data integrity is crucial. It returns a Pydantic object, allowing for clean attribute access (e.g., `result.name`).

4.  **`StructuredOutputParser`**:
    -   A LangChain-native way to specify multiple output fields using `ResponseSchema`. It's a good alternative to `JsonOutputParser` when you want to be very explicit about the required fields in your prompt.
    -   **Use Case**: Useful for extracting a fixed set of fields and generating clear instructions for the LLM.

---

### 🛠️ Tech Stack

-   **Core Framework**: LangChain
-   **LLM Provider**: OpenAI
-   **Data Validation & Schemas**: Pydantic
-   **Core Libraries**: `langchain-core`, `langchain-openai`, `python-dotenv`

---

### ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/jsonusuman351/langchain_output_parser.git](https://github.com/jsonusuman351/langchain_output_parser.git)
    cd langchain_output_parser
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # It is recommended to use Python 3.10 or higher
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables:**
    -   Create a file named `.env` in the root directory.
    -   Add your OpenAI API key to this file:
        ```env
        OPENAI_API_KEY="your-openai-api-key"
        ```

---

### 🚀 Usage Guide

Each script in this repository is a self-contained example of a specific output parser.

-   **Simple String Output:**
    *Returns the LLM response as a plain string.*
    ```bash
    python stroutputparser.py
    ```

-   **JSON Dictionary Output:**
    *Parses the LLM's response into a Python dictionary.*
    ```bash
    python jsonoutputparser.py
    ```

-   **Validated Pydantic Object Output:**
    *The most robust method; returns a validated Pydantic object.*
    ```bash
    python pydanticoutputparser.py
    ```

-   **Structured Dictionary Output with ResponseSchema:**
    *Uses LangChain's native schema to extract multiple fields into a dictionary.*
    ```bash
    python structuredoutputparser.py
    ```

**Example Output (from `pydanticoutputparser.py`):**
```
name='Suman' age=24
<class 'pydanticoutputparser.Person'>
```

---

### 🔬 A Tour of the Parsers

This repository is organized by parsing technique, allowing you to easily compare each method.

<details>
<summary>Click to view the code layout</summary>

```
langchain_output_parser/
│
├── stroutputparser.py          # Basic: Returns a string
├── jsonoutputparser.py         # Intermediate: Returns a JSON dictionary
├── pydanticoutputparser.py     # Advanced: Returns a validated Pydantic object
├── structuredoutputparser.py   # Alternative: Uses ResponseSchema for dictionary output
│
├── requirements.txt
├── .env                        # (need to create this for your API key)
└── README.md
```
</details>

---

---