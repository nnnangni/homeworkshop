30homework - M:N 관계



```python
class Post(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.(1)(settings.AUTH_USER_MODEL, (2)='like_post_set', blank=True)
```

1. ManyToMany
2. related_name

