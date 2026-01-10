from dotenv import load_dotenv
import os

from src.helper import combine_csv_to_txt,load_text_docs,filter_to_minimal_docs, text_split, download_embeddings

from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ['GOOGLE_API_KEY']= os.getenv('GOOGLE_API_KEY')
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

combine_csv_to_txt(
    csv_path="datasets/survey.csv",
    output_folder="datasets/txt_survey",
    batch_size=100,
    text_column="comments"   # replace if column name different
)
combine_csv_to_txt(
    csv_path="datasets/depression_dataset_reddit_cleaned.csv",
    output_folder="datasets/txt_depression",
    batch_size=100,
    text_column="clean_text"   # check actual column name!
)


docs1 = load_text_docs("datasets/txt_survey")
docs2 = load_text_docs("datasets/txt_depression")

documents = docs1 + docs2

filter_data = filter_to_minimal_docs(documents)
texts_chunk = text_split(filter_data)

embedding = download_embeddings()

pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)

index_name = "mental-health-chat-assistant"

if not pc.has_index(index_name):
    pc.create_index(
        name= index_name,
        dimension=384,     
        metric= "cosine",           
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)

docsearch = PineconeVectorStore.from_documents(
    documents=texts_chunk,
    embedding=embedding,
    index_name=index_name,
    pinecone_api_key=PINECONE_API_KEY
)
