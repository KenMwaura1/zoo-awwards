from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class TestZooAwwards(TestCase):
    """
    Test the zoo_awwards app
    """

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_login_page_status_code(self):
        response = self.client.get('/accounts/login/')
        self.assertEquals(response.status_code, 200)

    def test_register_page_status_code(self):
        response = self.client.get('/accounts/register/')
        self.assertEquals(response.status_code, 200)


class TestUserProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='zoo', password='testpwsd123')
        self.user.save()

    def tearDown(self):
        self.user.delete()
        self.user = None

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

    def test_update_user(self):
        self.user.username = 'zken'
        self.user.save()

    def test_get_user(self):
        self.user.username = 'zken'
        self.user.save()
        user = User.objects.get(id=1)
        self.assertEquals(user.username, 'zken')

    def test_get_all_users(self):
        self.user.username = 'zken'
        self.user.save()
        users = User.objects.all()
        self.assertEquals(len(users), 1)

    def test_get_all_users_by_id(self):
        self.user.username = 'zken'
        self.user.save()
        users = User.objects.all()
        self.assertEquals(users[0].id, 1)

    def test_get_all_users_by_username(self):
        self.user.username = 'zken'
        self.user.save()
        users = User.objects.all()
        self.assertEquals(users[0].username, 'zken')

    def test_get_all_users_by_password(self):
        self.user.username = 'zken'
        self.user.save()
        users = User.objects.all()
        self.assertEquals(users[0].password, 'testpwsd123')


