from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import User


class UserModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            password='Password123',
            bio='My name is John Doe.',
        )

    def test_valid_user(self):
        self._assert_user_is_valid()

    def test_username_cannot_be_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid()

    def test_username_can_be_thirty_characters(self):
        self.username = '' + 'x' * 30
        self._assert_user_is_valid()

    def test_username_can_be_thirty_characters(self):
        self.username = ''
        self._assert_user_is_invalid()

    def test_username_must_be_unique(self):
        User.objects.create_user('@janedoe',
                                 first_name='Jane',
                                 last_name='Doe',
                                 email='janedoe@example.com',
                                 password='Password123',
                                 bio='My name is JaneDoe.', )
        self.username='@janedoe'
        self._assert_user_is_invalid();

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except ValidationError:
            self.fail('User must be valid!')

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()
