from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
	USER = (
		(None, '---User Type---'),
        ('Recruiter', 'Recruiter'),
        ('Prospective Employer', 'Prospective Employer'),
        ('Friend', 'Friend')
        )
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	message = models.CharField(max_length=255)
	user_type = models.CharField(max_length=255, choices=USER, default=None)

	def __unicode__(self):
		return self.name + " - " + self.email
