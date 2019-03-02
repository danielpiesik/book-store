from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        super().save(*args, **kwargs)
