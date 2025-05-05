# load a multiple document from the directory
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()  # A generator of document object it not loaded documents at once. they are fetched one at a time as needed.

for document in docs:
    print(document.metadata)