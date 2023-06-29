from django.contrib import admin
from .models import (TagModel, BlogModel, CommentModel, ImageModel)


admin.site.register(
	(TagModel, BlogModel, CommentModel, ImageModel)
)
