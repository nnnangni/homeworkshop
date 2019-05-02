# 36workshop - JS DOM 조작과 JS 응용

#### Python 기초 개념 코드를 JS 코드로 번역.

- 아래 Instruction 에 따라 JS 코드를 작성해 보자.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<title>Clicked</title>
</head>
<body>
<h1>0</h1>
<button id="change-btn">Click it</button>
<script>
    // #change-btn 을 button 상수에 할당한다.
    const button = document.querySelector("#chnage-btn")
    // h1 태그를 header 상수에 할당한다.
    const header = document.querySelector("h1")
    // clickCount 변수를 0으로 초기화 한다.
    let clickCount = 0
    // button에 'click' eventListner를 추가한다. 클릭이 일어나면,
    button.addEventListener('click', function(e){
    // clickCount 가 1씩 올라간다.
        clickCount += 1
    // header 안의 내용을 clickCount 로 바꾼다.
        header.innerText = clickCount
        // header.innerText = ++ clickCount 도 가능
    })
</script>
</body>
</html>
```

