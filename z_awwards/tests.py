from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
from z_awwards.models import UserProject, ProjectRating


class TestZooAwwards(TestCase):
    """
    Test the zoo_awwards app
    

    def test_login_page_status_code(self):
        response = self.client.get('/accounts/login/')
        self.assertEquals(response.status_code, 200)

    def test_register_page_status_code(self):
        response = self.client.get('/accounts/register/')
        self.assertEquals(response.status_code, 200)
    """

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


class ProjectRatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='zken')
        self.user_project = UserProject.objects.create(id=1, title='test user_project', photo="https://res.cloudinary.com/dd5ab8mp3/image/upload/v1634659738", description='desc',
                                                       user=self.user, url='https://test.com')
        self.rating = ProjectRating.objects.create(id=1, design=6, usability=7, content=9, user=self.user,
                                                   project=self.user_project)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, ProjectRating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = ProjectRating.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_update_rating(self):
        self.rating.design = 5
        self.rating.save()
        rating = ProjectRating.objects.get(id=1)
        self.assertEquals(rating.design, 5)

    def test_delete_rating(self):
        self.rating.delete()
        rating = ProjectRating.objects.all()
        self.assertTrue(len(rating) < 1)

    def test_get_user_project_rating(self):
        id =1
        self.rating.save()
        rating = ProjectRating.get_ratings(project=id)
        self.assertTrue(len(rating) == 1)
