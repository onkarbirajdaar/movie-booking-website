from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = "customer", "Customer"
        THEATRE_ADMIN = "theatre_admin", "Theatre Admin"
        SUPER_ADMIN = "super_admin", "Super Admin"

    email = models.EmailField("email address", unique=True)
    mobile_number = models.CharField(
        max_length=10,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^[6-9]\d{9}$",
                message="Enter a valid 10 digit mobile number.",
            )
        ],
    )
    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)
    role = models.CharField(
        max_length=20, choices=Role.choices, default=Role.CUSTOMER
    )

    def save(self, *args, **kwargs):
        # a superuser is always a super admin
        if self.is_superuser:
            self.role = self.Role.SUPER_ADMIN
        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name() or self.email or self.username