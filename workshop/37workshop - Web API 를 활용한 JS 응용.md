## 37workshop - Web API 를 활용한 JS 응용

#### Axios 를 활용해 GET / POST 요청을 보낸다.



- 브라우저/node 환경에서 Axios 를 활용해 GET/POST 요청을 보내보자.

- 요청 예시. 아래 형식으로 POST 요청을 보내면, 생성된 post Object 를 응답으로 보냅니다.

  

  13.125.249.144:8080

  | HTTP method | URI                            | Description     |
  | ----------- | ------------------------------ | --------------- |
  | GET         | ssafy/[region]/[classNo]/posts | 전체 posts list |
  | POST        | ssafy/[region]/[classNo]/posts | posts 작성      |

  

  ```javascript
  axios.get(URL).then(response=>{
      console.log(response)
  })
  ```

  