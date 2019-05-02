# 37homework - Web API 를 활용한 JS 응용

#### Web API 에 Axios 라이브러리를 활용해 요청 보내기



1. Axios 를 사용하는 아래 코드를 완성하시오.
- Browser 는 axios CDN을 통해,
- Node 는 npm install 과 require 를 통해 axios 를 가져와야 합니다.

```javascript
const URL = "https://dog.ceo/api/breeds/image/random"

axios.get(URL)
    .then(res => {
    // imgSrc 상수에 res 에서 개 image의 URL을 뽑아서 저장한다.
    const imgSrc = res.data.message
    // console.log(res.data.message)
    // imgSrc를 return한다.
    return imgSrc
})
    .then(imageSource => {
    // imageSource를 콘솔에 출력한다.
    console.log(imageSource)
})
```

```javascript
const script = document.
script.type = "text/javascript"
script
script.src = "https://unpkg.com/axios/dist/axios/min/js"
script
document.head.appendChild(script)
axios
```

