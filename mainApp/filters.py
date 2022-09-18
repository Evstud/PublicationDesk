from django_filters import FilterSet
from .models import Response
from django_currentuser.middleware import get_current_user


class ResponseFilter(FilterSet):
    class Meta:
        model = Response
        fields = ['responseNotice']

    def __init__(self, *args, **kwargs):
        super(FilterSet, self).__init__(*args, **kwargs)
        self.filters['responseNotice'].label = 'Объявление'
        user_test2 = get_current_user()
        self.filters['responseNotice'].queryset = self.filters['responseNotice'].queryset.filter(noticeAuthor=user_test2)






