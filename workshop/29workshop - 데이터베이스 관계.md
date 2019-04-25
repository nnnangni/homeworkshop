# 29workshop - 데이터베이스 관계

### 개체-관계 다이어그램을 작성해본다.

* 아래의 Django 코드를 바탕으로 개체-관계 다이어그램을 작성해본다.

```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```

![1556166706354](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1556166706354.png)