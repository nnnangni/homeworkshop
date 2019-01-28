## 함수

#### 1. List는 for 문을 실행하면 모든 요소를 순차적으로 돌면서 반복문을 수행합니다. 임의의 리스트 my_list의 값을 하나씩 출력하는 코드를 아래에 작성하시오.

```python
my_list = ["a","b","c","d","e","f","g","h"]
for i in my_list:
    print(i)
```

#### 2. 위에 작성한 코드를 인덱스(index) 값과 함께 출력하는 코드로 변경하시오.

```python
my_list = ["a","b","c","d","e","f","g","h"]
for i in enumerate(my_list):
    print(i)
```

#### 3. 딕셔너리는 key, value로 구성되어 있습니다. 따라서, 딕셔너리 my_dict 각각의 상 황에 따라 반복문을 수행할 수 있도록 빈칸을 채우시오. 

key : my_dict.keys()

value : my_dict.values()

key와 value : my_dict.items()

#### 4. result에 저장된 값은?

1+5 = 6



- return 이 없으면 print값은 None을 반환해줌
- print도 없고 어떤 값을 입력하면 None만 출력됨.
- 즉, return값을 만들어줘야 값이 return됨.