from elasticsearch import Elasticsearch


# Elasticsearch 클러스터에 연결합니다.

es = Elasticsearch(["http://localhost:9200"])
print(es)

# Content-Type 설정 변경
# elasticsearch.ApiError: ApiError(406, 'Content-Type header [application/vnd.elasticsearch+json; compatible-with=8] is not supported', 'Content-Type header [application/vnd.elasticsearch+json; compatible-with=8] is not supported') 에러 해
결
#settings = {
#    "http": {
#        "content_type": "application/json"
#    }
#}
#response = es.cluster.put_settings(body=settings)
#print(response)


# 클러스터와의 연결을 확인합니다.
if es.ping():
    print("Elasticsearch 클러스터에 연결되었습니다.")
else:
    print("Elasticsearch 클러스터에 연결할 수 없습니다.")



# 문서 색인화 (Indexing a document)
document = {
    "field1": "value1",
    "field2": "value2"
}

res = es.index(index="test-index", body=document, headers={"Content-Type": "application/json"})
print(res)

# 검색 쿼리 수행 (Performing a search query)
query = {
    "query": {
        "match": {
            "field1": "value1"
        }
    }
}

#res = es.index(index="test-index", body=document, headers={"Content-Type": "application/json"})
#print(res)


res = es.search(index="test-index", body=query)
print(res)
