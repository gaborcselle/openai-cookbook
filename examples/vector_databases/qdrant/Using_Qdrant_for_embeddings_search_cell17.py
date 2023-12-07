vector_size = len(article_df['content_vector'][0])

qdrant.recreate_collection(
    collection_name='Articles',
    vectors_config={
        'title': rest.VectorParams(
            distance=rest.Distance.COSINE,
            size=vector_size,
        ),
        'content': rest.VectorParams(
            distance=rest.Distance.COSINE,
            size=vector_size,
        ),
    }
)