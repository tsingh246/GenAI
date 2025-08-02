# GenAI Tokenization and Embeddings

This repository contains simple Python scripts to demonstrate tokenization and embeddings using OpenAI models.

## Files

- [`Tokenization.py`](Tokenization.py): Shows how to tokenize and detokenize text using the `tiktoken` library for OpenAI models.
- [`embeddings.py`](embeddings.py): Generates embeddings for a sample text using OpenAI's API.
- [`.env`](.env): Store your OpenAI API key and other environment variables.
- [`.gitignore`](.gitignore): Ensures sensitive files like `.env` are not tracked by git.

## Usage

1. Install dependencies:
    ```sh
    pip install tiktoken openai python-dotenv
    ```

2. Add your OpenAI API key to a `.env` file:
    ```
    OPENAI_API_KEY=your-api-key-here
    ```

3. Run tokenization example:
    ```sh
    python Tokenization.py
    ```

4. Run embeddings example:
    ```sh
    python embeddings.py
    ```

## License

This project is for educational purposes.
