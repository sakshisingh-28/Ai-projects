from transformers import pipeline

summarizer = pipeline("summarization")

article = """
Artificial Intelligence is transforming industries worldwide. It powers recommendation systems, 
virtual assistants, medical diagnosis tools, autonomous vehicles, and so much more. 
With the rise of language models, AI is now capable of understanding and generating human-like language. 
This opens doors to efficient content creation, automated summarization, and enhanced customer support systems.
"""

summary = summarizer(article, max_length=60, min_length=30, do_sample=False)

print("📄 Original Article:\n", article)
print("\n📝 Summary:\n", summary[0]['summary_text'])
