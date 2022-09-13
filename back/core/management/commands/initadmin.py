from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
	help = 'Create admin user'
	requires_migrations_checks = True
	stealth_options = ("stdin",)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.UserModel = get_user_model()

	def handle(self, *args, **options):
		username = 'test'
		email = 'test@mail.com'
		password = 'testqwe123'

		if not self.UserModel.objects.filter(username=username).exists():
			print('Creating account for %s (%s)' % (username, email))
			self.UserModel.objects.create_superuser(email=email, username=username, password=password)
		else:
			print('Admin account has already been initialized.')
