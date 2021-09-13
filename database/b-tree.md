# B-Tree

https://velog.io/@emplam27/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-B-Tree

일반적인 Binary Search Tree(BST)의 경우에는 좌우 균형이 맞지 않으면 비효율적이다. 따라서, Balanced Tree가 필요하다

* Balanced Tree : 삽입과 삭제시 스스로 균형을 유지하는 트리. (e.g. AVL Tree, Red-Black Tree, B-Tree)
* 항상 O(log N)의 검색 성능을 유지한다.