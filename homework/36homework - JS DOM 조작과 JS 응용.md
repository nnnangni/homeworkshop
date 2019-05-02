# 36homework - JS DOM 조작과 JS 응용

#### • DOM 요소 선택과 조작

#### • EventListener 개념 이해



1. DOM에서 특정 요소를 선택할 때 document.querySelector() 뿐만 아니라 document.querySelectorAll() 역시 사용할 수 있다. 둘의 차이를 검색하여 기술하시오.

  

  document.querySelector() 는 특정요소에 대한 첫번째 하나만 나옴.

  document.querySelectorAll() 는 조건에 부합하는 전체를 가져온다.

  

2. JS에서 자주 사용하는 EventListener 들 중 아래와 같은 것들이 있다. 각각 간략하게 어떤 Trigger 를 의미하는지 조사하여 간략하게 기술하시오.

  

  – click : 클릭했을 때 이벤트 발생
  – mouseover : 내가 선택한 요소위에 마우스가 위치했을 때 발생 / mouseout : 반대로 요소에서 마우스가 나갔을 때 / mousemove : 마우스가 움직일때마다 이벤트 발생
  – keypress : 키가 눌렸을 때 발생(누르고 있으면 계속 이벤트 발생) / keydown : 눌린 시점(순간)에 이벤트 발생 / keyup : 키가 눌렸다가 떼진 순간 이벤트 발생
  – load : 데이터가 불러와졌을 때
  – scroll : 스크롤을 내리거나 올라갈 때
  – change : 값이 바꼈을 때



3. DOM 에 요소를 추가할 때, innerHTML += 의 방법과 appendChild() 함수를 통해 추가하는 방법이 있다. 둘의 차이를 간략하게 기술하시오.

  

  appendChild() : 스트링을 그대로 넣을 수 없고 이미 만들어진 오브젝트 형태여야 넣을 수 있음.

   innerHTML += : 스트링을 그대로 넣을 수 있음, 기존에 있는 정보를 불러와야해서 약간 속도가 느리다.