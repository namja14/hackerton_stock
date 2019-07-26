from django.db import models

# Create your models here.
class Apply(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title# 이거 쓰면 제목이 써진다
    
    def summary(self):
        return self.body[:100]#클래스에 정의된 body에서 100글자만 출력하라는 의미입니다.
        