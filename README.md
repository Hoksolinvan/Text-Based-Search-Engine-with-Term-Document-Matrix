***Term-Document Matrix Construction:***

- **Generation**: Create a term-document matrix from a collection of text documents. Each row represents a term, and each column represents a document. The entries in the matrix capture the frequency of terms within each document.
  
- **Preprocessing**: Apply tokenization, stemming, and removal of stop words to prepare terms. This preprocessing ensures that terms are standardized for accurate analysis.


***Query Handling and Vectorization***

- ***Query Input***: Receive a text query from the user, which is preprocessed in the same manner as the documents to ensure consistency.
- **Query Vector Construction**: Convert the preprocessed query into a query vector. This vector aligns with the dimensions of the term-document matrix, enabling direct comparison with document vectors.

**Similarity Measurement**

**Cosine Similarity**: Calculate the cosine similarity between the query vector and each document vector in the term-document matrix. Cosine similarity measures the cosine of the angle between two vectors, providing a metric for their similarity.

**Formula**: The cosine similarity between vectors A and B is given by:
<br>
<img width="316" alt="Screenshot 2024-07-02 at 12 11 06 PM" src="https://github.com/Hoksolinvan/Text-Based-Search-Engine-with-Term-Document-Matrix/assets/158796823/59231ea4-34e2-4fc2-8bac-35569786ae50">
<br>

**Implementation**:Compute the dot product of the query vector and document vectors, and divide by the product of their magnitudes. This results in a similarity score between 0 and 1.

**Ranking and Output**

- **Document Ranking**: Rank the documents based on their similarity scores to the query vector. Higher scores indicate greater relevance to the query.

- **Output Format**: Present the ranked documents along with their similarity scores. The output is designed to be processed by a colleague's web interface, ensuring seamless integration and display.



