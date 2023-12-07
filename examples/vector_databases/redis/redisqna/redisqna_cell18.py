import os
from openai import OpenAI

client = OpenAI()

directory = './assets/'
model='text-embedding-ada-002'
i = 1
for file in os.listdir(directory):
    with open(os.path.join(directory, file)) as f:
        content = f.read()
        vector = client.embeddings.create(input = [content], model = model)['data'][0]['embedding']
        client.json().set(f'doc:{i}', '$', {'content': content, 'vector': vector})
    i += 1