1.Ціль-зробити навчальний проект, сайт для школи.
-------------------------------------------------
2.Осноні апки:
1) Реєстрація
2) Головна сторінка
3) Розклад
4) Контакти
5) Інформація
-------------------------------------------------
3.Реєстрація
pass
_________________________________________________
4.Головна сторінка
pass
_________________________________________________
5.Розклад
pass
__________________________________________________
6.Контакти
pass
__________________________________________________
7.Інформація
pass
_________________________________________________

from django.test import TestCase

from accounts.models import CustomUser, get_user_display


class CustomUserModelTests(TestCase):

    def test_create_user(self):

        user = CustomUser.objects.create_user(
            email='test@mail.com',
            first_name='Fname',
            last_name='Lname',
            phone_number='505555555',
            password='testpass123'
        )

        self.assertEqual(user.email, 'test@mail.com')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertNotEqual(user.password, 'testpass123')

    def test_create_superuser(self):

        admin = CustomUser.objects.create_superuser(
            email='test@mail.com',
            first_name='Fname',
            last_name='Lname',
            phone_number='505555555',
            password='testpass123'
        )

        self.assertEqual(admin.email, 'test@mail.com')
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        self.assertNotEqual(admin.password, 'testpass123')

    def test_user_display(self):
        user = CustomUser.objects.create_user(
            email='test@mail.com',
            first_name='Fname',
            last_name='Lname',
            phone_number='505555555',
            password='testpass123'
        )
        self.assertEqual(get_user_display(user), 'Fname Lname')

    class CustomUserManager(BaseUserManager):

        def create_user(self, email, first_name, last_name, phone_number, password, **kwargs):

            if not email:
                raise ValueError(_('You must provide an email'))
            email = self.normalize_email(email)
            user = self.model(
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                **kwargs
            )
            user.set_password(password)
            user.save()
            return user

        def create_superuser(self, email, first_name, last_name, phone_number, password, **kwargs):
            kwargs.setdefault('is_staff', True)
            kwargs.setdefault('is_active', True)
            kwargs.setdefault('is_superuser', True)

            if kwargs.get('is_staff') is not True:
                raise ValueError(_('Superuser must be assigned to is_staff=True'))
            if kwargs.get('is_superuser') is not True:
                raise ValueError(_('Superuser must be assigned to is_superuser=True'))

            return self.create_user(email, first_name, last_name, phone_number, password, **kwargs)

    class CustomUser(AbstractBaseUser, PermissionsMixin):
        email = models.EmailField(_('Email address'), unique=True)
        first_name = models.CharField(_('First Name'), max_length=50)
        last_name = models.CharField(_('Last Name'), max_length=50)
        phone_number = models.CharField(_('Phone Number'), max_length=9)  # ukrainian numbers have 9 digits without +380
        phone_verified = models.BooleanField(default=False)
        is_staff = models.BooleanField(default=False)
        is_active = models.BooleanField(default=False)
        is_superuser = models.BooleanField(default=False)

        objects = CustomUserManager()

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def get_user_display(user: CustomUser):
        return f'{user.first_name} {user.last_name}'