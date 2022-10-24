import pandas as pd
from top2vec import Top2Vec

# load text corpus
df = pd.read_json("data/corpus.json")
docs = df.data.values.tolist()

# generate and save model
model = Top2Vec(docs)
model.save("corpus_model")