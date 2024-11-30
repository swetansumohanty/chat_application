from tokenize import group
from django.test import TestCase
from app.models import Group,Chat
# Create your tests here.

class GroupAppTest(TestCase):
    """
    class to test app.models
    """
    def setUp(self):
        Group.objects.create(name="aliens")

    def test_one(self):
        obj1 = Group.objects.get(name="aliens")
        self.assertEqual(obj1.name,"aliens")

# class ChatAppTest(TestCase):
    
#     def setUp(self):
#         # Group.objects.create(name="aliens")
#         Chat.objects.create(content="Hello")

#     def test_two(self):
#         obj1 = Chat.objects.get(content="Hello")
#         self.assertEqual(obj1.content,'Hello')
       