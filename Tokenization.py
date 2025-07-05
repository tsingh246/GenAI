"""

This program is to understand tokenization used by LLM
 models
"""

import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hellp, I am Tej"
tokens= enc.encode(text)
print(tokens)

decoded = enc.decode(tokens)
print(decoded)