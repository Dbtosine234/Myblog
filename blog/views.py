from rest_framework.viewsets import ModelViewSet
from blogemmax.utils import (Helper, get_query)
from .models import (TagModel, BlogModel, CommentModel, ImageModel)
from .serializers import (TagSerializer, BlogSerializer, CommentSerializer, ImageSerializer)
from django.db.models import (Count, Q)


class TagView(ModelViewSet):
	queryset = TagModel.objects.all()
	serializer_class = TagSerializer


class BlogView(ModelViewSet):
	queryset = BlogModel.objects.all()
	serializer_class = BlogSerializer
	lookup_field = 'slug'

	def get_queryset(self):
		if self.request.method.lower() != 'get':
			return self.queryset

		params = self.request.query_params.dict()
		keyword = params.pop('keyword', None)
		params.pop('page', None)
		results = self.queryset.filter(**params)
		if keyword:
			search_fields = ['tag__name ', 'title']
			query = get_query(keyword, search_fields)
			results = results.filter(query)

		return results


class CommentView(ModelViewSet):
	queryset = CommentModel.objects.all()
	serializer_class = CommentSerializer


class ImageView(ModelViewSet):
	queryset = ImageModel.objects.all()
	serializer_class = ImageSerializer


class TopBlogView(ModelViewSet):
	queryset = BlogModel.objects.all()
	serializer_class = BlogSerializer
	http_method_names = ['get']

	def get_queryset(self):
		results = self.queryset.annotate(Comments_count=Count('Comments')).order_by('-Comments_count')[:5]

		return results
