from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # 다른앱에 있는 모델 참조
    # 방법 1.(권장하지 않음)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 방법 2.(권장)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 방법 3.(권장)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


