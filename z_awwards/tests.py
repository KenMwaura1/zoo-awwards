from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
from z_awwards.models import UserProject


class TestZooAwwards(TestCase):
    """
    Test the zoo_awwards app
    """

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


class UserProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='zken')
        self.user_project = UserProject.objects.create(id=1, title='test project',
                                                       photo='"https://res.cloudinary.com/dd5ab8mp3/image/upload/v1634659738',
                                                       description='desc', user=self.user, url='http://test.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.user_project, UserProject))

    def test_save_user_project(self):
        self.user_project.save_post()
        user_project = UserProject.objects.all()
        self.assertTrue(len(user_project) > 0)

    def test_get_user_projects(self):
        self.user_project.save()
        user_projects = UserProject.all_posts()
        self.assertTrue(len(user_projects) > 0)

    def test_search_user_project(self):
        self.user_project.save()
        user_project = UserProject.search_project('test')
        self.assertTrue(len(user_project) > 0)

    def test_delete_user_project(self):
        self.user_project.delete_post()
        user_project = UserProject.search_project('test')
        self.assertTrue(len(user_project) < 1)