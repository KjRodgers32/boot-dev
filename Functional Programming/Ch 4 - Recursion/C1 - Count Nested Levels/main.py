def count_nested_levels(nested_documents, target_document_id, level=1):
    for key in nested_documents:
        if key == target_document_id:
            return level 
        else:
            result = count_nested_levels(nested_documents[key], target_document_id, level+1)
            if result != -1:
                return result
    return -1