import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import networkx as nx

text = """Artificial Intelligence is transforming the world.
It is used in healthcare, education, and transportation.
Summarization tools help people save time.
Extractive summarization selects key sentences from the input."""

# Step 1: Sentence Tokenization
sentences = sent_tokenize(text)
print("\n📄 Tokenized Sentences:\n")
for i, s in enumerate(sentences, start=1):
    print(f"{i}. {s}")

# Step 2: TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(sentences)
print("\n📐 TF-IDF Matrix Shape:", tfidf_matrix.shape)

# Step 3: Cosine Similarity Matrix
similarity_matrix = (tfidf_matrix * tfidf_matrix.T).toarray()
print("\n🔗 Sentence Similarity Matrix:\n")
for row in similarity_matrix:
    print(["{0:.2f}".format(score) for score in row])

# Step 4: Build Similarity Graph 
graph = nx.from_numpy_array(similarity_matrix)

# Apply TextRank (PageRank) Algorithm
scores = nx.pagerank(graph)

# Sort sentences by score
ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

# Pick top N sentences for summary
summary = " ".join([sent for _, sent in ranked_sentences[:3]])
print("\n📝 Final Summary:\n", summary)
