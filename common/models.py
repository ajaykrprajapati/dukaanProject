import uuid

from django.db import models

from django.contrib.auth import get_user_model


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by_user = models.ForeignKey(
        get_user_model(),
        related_name="%(class)s_created_by",
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
