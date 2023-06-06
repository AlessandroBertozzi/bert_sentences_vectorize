# from copy import deepcopy


def scrolling(client, index, query, scroll_size):
    response = client.search(index=index, query=query, size=scroll_size)
    result = []
    for hits in response["hits"]["hits"]:
        collection = hits["_source"]
        collection["_id"] = hits["_id"]
        result.append(collection)
    return result
