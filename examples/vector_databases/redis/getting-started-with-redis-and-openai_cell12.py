# Constants
VECTOR_DIM = len(data['title_vector'][0]) # length of the vectors
VECTOR_NUMBER = len(data)                 # initial number of vectors
INDEX_NAME = "embeddings-index"           # name of the search index
PREFIX = "doc"                            # prefix for the document keys
DISTANCE_METRIC = "COSINE"                # distance metric for the vectors (ex. COSINE, IP, L2)