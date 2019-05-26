from django.contrib.auth import get_user_model

user = get_user_model()
print(user.objects.all())
