import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import networkx as nx

nltk.download('punkt')

def summarize_text(text, num_sentences=3):
    # Step 1: Sentence Tokenization
    sentences = sent_tokenize(text)

    # Step 2: TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # Step 3: Similarity Matrix
    similarity_matrix = (tfidf_matrix * tfidf_matrix.T).toarray()

    # Step 4: Graph + TextRank
    graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(graph)

    # Step 5: Rank sentences
    ranked = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    summary = " ".join([sent for _, sent in ranked[:num_sentences]])

    return summary
