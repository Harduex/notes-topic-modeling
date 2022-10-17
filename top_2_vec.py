import pandas as pd
from top2vec import Top2Vec

df = pd.read_json("data/corpus.json")
docs = df.data.values.tolist()

model = Top2Vec(docs)
topic_sizes, topic_nums = model.get_topic_sizes()
print(f"Topic Nums: {topic_nums}")

topic_words, topic_scores, topic_nums = model.get_topics(
    model.get_num_topics())

for words, num in zip(topic_words, topic_nums):
    print(num)
    print(f"Words: {words}")

documents, document_scores, document_ids = model.search_documents_by_topic(topic_num=0, num_docs=10)

for doc, score, doc_id in zip(documents, document_scores, document_ids):
    print(f"Document: {doc_id}, Score: {score}")
    print("----------------")
    print(doc)
    print("----------------")
    print()