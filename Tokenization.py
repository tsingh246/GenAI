"""

This program is to understand tokenization used by LLM    
 models
"""

import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hello, I am Tej"
# Tokenization
tokens= enc.encode(text)
print(tokens)

# Detokenization
decoded = enc.decode(tokens)
print(decoded)