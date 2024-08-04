from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, phone_number, password):
        if not email:
            raise ValueError('باید ایمیل خود را وارد کنید')
        if not full_name:
            raise ValueError('باید نام خود را وارد کنید')
        if not phone_number:
            raise ValueError('باید شماره موبایل خود را وارد کنید')

        user = self.model(email=self.normalize_email(email), full_name=full_name, phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, phone_number, password):
        user = self.create_user(email, full_name, phone_number, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self.db)
        return user
