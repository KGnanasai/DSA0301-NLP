from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

# Query
query = "This is the second document."

def retrieve_documents(query, documents):
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Compute TF-IDF scores for the documents and the query
    tfidf_matrix = vectorizer.fit_transform(documents + [query])

    # Calculate the cosine similarity between the query and each document
    cosine_similarities = linear_kernel(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    # Rank the documents based on cosine similarity
    ranked_documents = sorted(list(enumerate(cosine_similarities)), key=lambda x: x[1], reverse=True)

    return ranked_documents

# Retrieve and print the ranked documents
ranked_documents = retrieve_documents(query, documents)

print("Query:", query)
print("\nRanked Documents:")
for index, score in ranked_documents:
    print(f"Document {index + 1}: Score = {score:.4f}")
    print(f"   '{documents[index]}'")
    print()
