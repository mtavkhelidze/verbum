import os

from sentence_transformers import SentenceTransformer

from logging_setup import logging_setup


logging_setup()

model_name = os.getenv("model_name")
model = SentenceTransformer(model_name)
model.save("./model.bin")
