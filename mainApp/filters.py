import django_filters.filters
from django_filters import FilterSet
from .models import Notice, Response


class ResponseFilter(FilterSet):

    class Meta:
        model = Response
        fields = ['responseNotice']

    def get_queryset(self):
        queryset=Notice.objects.all().filter(noticeAuthor=self.request.user)
        return queryset
    # def __init__(self, *args, **kwargs):
    #     super(FilterSet, self).__init__(*args, **kwargs)
    #     self.fields['responseNotice'].label='Объвление'
