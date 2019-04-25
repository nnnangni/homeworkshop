# 32workshop - 데이터베이스 시딩

- 아래는 Django에서 myapp의 Musician class에 저장된 기본 시드 데이터이다.
  이를 적용하기 위해 필요한 json 파일을 만들어 적용해보자.

![1556169003293](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1556169003293.png)

```json
[
    {
        "pk":1,
        "model":"myapp.musician,
        "fields":{
            "first_name":"John",
            "last_name":"Lennon"
        }
	},
	{
        "pk":2,
        "model":"myapp.musician,
        "fields":{
            "first_name":"Paul",
            "last_name":"McCartney"
    	},
	}
]
```

