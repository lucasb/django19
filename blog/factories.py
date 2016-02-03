import factory # from FactoryBoy

from .models import Post
from django.contrib.auth.models import User


class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    id      = factory.Sequence(lambda n: n)
    title   = factory.Sequence(lambda n: 'title {}'.format(n))
    text    = 'Standard Text'
    author  = factory.SubFactory('blog.factories.UserFactory')

    # @factory.post_generation
    # def author(self, create, extracted, **kwargs):
    #     if not create:
    #         return
    #
    #     if extracted:
    #         for user in extracted:
    #             self.author = user


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    id       = factory.Sequence(lambda n: n)
    username = factory.Sequence(lambda n: 'username_%s' % n)
