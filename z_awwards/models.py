from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    """
    User Profile model
    """
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    username = models.TextField(max_length=150)
    bio = models.TextField(max_length=500, blank=True, default="default bio")
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='images/profile_pic/', blank=True)
    contact_email = models.EmailField(max_length=100, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    def __str__(self):
        return f'{self.user.username}: profile'


class UserProject(models.Model):
    """
    User Post model
    """
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=250)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='images/user_post/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userposts")
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def delete_post(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        """
        Method to search for a project by title
        :param title:
        :return: search results
        """
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_posts(cls):
        """
        Method to get all posts
        :return: all posts
        """
        return cls.objects.all()

    def save_post(self):
        self.save()

    def __str__(self):
        return f'Title: {self.title}'


class ProjectRating(models.Model):
    """
    Project Rating model
    """
    rating = ()
    for x in enumerate(range(1, 11)):
        rating_tuple = (x[1], f'{x[1]}')
        rating += (rating_tuple,)

    # print(rating)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userratings", null=True)
    project = models.ForeignKey(UserProject, on_delete=models.CASCADE, related_name="projectratings", null=True)
    content = models.IntegerField(choices=rating, default=1)
    design = models.IntegerField(choices=rating, default=1)
    usability = models.IntegerField(choices=rating, default=1)
    content_average = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    rating = models.FloatField(choices=rating, default=0, blank=True)

    def __str__(self):
        return f'{self.user}: {self.project}'

    @classmethod
    def get_ratings(cls, project):
        """
        Method to get all ratings for a project
        :param project:
        :return: all ratings
        """
        return cls.objects.filter(project=project).all()

    def save_rating(self):
        self.save()
