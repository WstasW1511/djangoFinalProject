from collections import Counter
from itertools import groupby
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from posts.models import Like, Posts
from django_filters import rest_framework as filters
from posts.filters import DateRangeFilterSet


class AnaliticViewSet(GenericAPIView):
    queryset = Like.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DateRangeFilterSet

    def get(self, request, format=None):

        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)

        ordered_queryset = filtered_queryset.order_by('created_at')
        likes_by_date = groupby(ordered_queryset, lambda like: like.created_at.strftime("%Y-%m-%d"))

        response = []
        for date, likes in likes_by_date:
            count = Counter(like.kind for like in likes)
            response.append(
                {
                    'Date': date,
                    'Likes': count['Like'],
                    'Dislikes': count['Dislake'],

                }
            )

        return Response(data=response, status=status.HTTP_200_OK)