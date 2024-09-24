def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    doc_entry = (new_doc, )
    return documents + doc_entry