
from django_filters import rest_framework as filters

from posts.models import Posts, Like
from utils.const import ViewChoise

class PostsFilterSet(filters.FilterSet):

    view = filters.ChoiceFilter(choices=ViewChoise.choice(), field_name='view', label='По типу')
    title = filters.CharFilter(label='По названию', lookup_expr='contains', field_name='title')

    class Meta:
        model = Posts
        fields = ('view', 'title', 'author', 'created_at')

class DateRangeFilterSet(filters.FilterSet):
    date_from = filters.DateFilter(field_name='created_at', lookup_expr='gte', label='От')
    date_to = filters.DateFilter(field_name='created_at', lookup_expr='lte', label='До')

    class Meta:
        model = Like
        fields = (
            'date_from',
            'date_to',
            'post'
        )


