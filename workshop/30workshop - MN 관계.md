# 30workshop - M:N 관계

* 게시물의 해시태그를 구현하기 위하여 아래와 같이 객체-관계 다이어그램을 작성하였다. 다이어그램을 바탕으로 models.py 에 Post 모델과 Hashtag 모델을 정의해본다.

  ![1556166806858](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1556166806858.png)

```python
class Hashtag(models.Model):
    content = models.TextField()
    
class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    # blank 해시태그가 없을수도 있음
```

