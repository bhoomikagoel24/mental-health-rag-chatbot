from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from typing import List
from langchain.schema import Document


import pandas as pd
import os

def combine_csv_to_txt(csv_path, output_folder, batch_size=100, text_column=None):
    df = pd.read_csv(csv_path)

    # detect text column if not provided
    if not text_column:
        text_column = df.columns[0]  # usually the text is first column
    
    os.makedirs(output_folder, exist_ok=True)

    batch = []
    file_index = 1

    for idx, row in df.iterrows():
        text = str(row[text_column]).strip()
        if text:
            batch.append(text)

        # if batch size complete → write file
        if len(batch) == batch_size:
            file_path = os.path.join(output_folder, f"combined_{file_index}.txt")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("\n\n".join(batch))
            
            batch = []
            file_index += 1

    # write the last batch
    if batch:
        file_path = os.path.join(output_folder, f"combined_{file_index}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n\n".join(batch))



def load_text_docs(path):
    loader = DirectoryLoader(
        path,
        glob="*.txt",
        loader_cls=TextLoader
    )
    return loader.load()

def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """
    Giving a list of Document objects,
    return a new list of Document objects containing only 'source' in metadata and 
    the original page content.
    """
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content = doc.page_content,
                metadata = {"source": src}
            )
        )
    return minimal_docs

# Split the document into smaller chunks
def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap=80,
        length_function=len
    )
    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk


def download_embeddings():
    """
    Downloading and returning the HuggingFace embeddings Model.
    """
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceBgeEmbeddings(
        model_name = model_name
        # ,model_kwargs = {"device": "cuda" if torch.cuda.is_available() else "cpu"}
    )

    return embeddings

