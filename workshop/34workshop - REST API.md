# 34workshop - REST API

### REST API의 일반적인 설계에 대해 알아본다.

- 일반적인 REST API에서 게시글(Post)에 대한 각각의 CRUD에 대응되는 HTTP methods와 Url을 작성하시오.

|        CRUD         | HTTP methods |        URL        |
| :-----------------: | :----------: | :---------------: |
|    리소서의 목록    |     GET      |      posts/       |
|     리소스 생성     |     POST     |      posts/       |
| 리소스 중 하나 표시 |     GET      | `posts/<int:id>/` |
|     리소스 수정     |     PUT      | `posts/<int:id>/` |
|     리소스 삭제     |    DELETE    | `posts/<int:id>/` |

