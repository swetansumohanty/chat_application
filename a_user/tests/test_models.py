from django.test import TestCase
from a_user.models import ChatUser


class TestChatUser(TestCase):
    """
    testing models.
    """
    def setUp(self):
        ChatUser.objects.create(
            username="sampad3",
            first_name="sekhar",
            last_name="mohanty",
            email="sampark@gmail.com",
            mobile=8018898592,
            password="sampad12"
        )

    def test_1(self):
        obj1= ChatUser.objects.get (username="sampad3",password="sampad12")
        self.assertEqual(obj1.username,"sampad3")
        self.assertEqual(obj1.password,"sampad12")



        