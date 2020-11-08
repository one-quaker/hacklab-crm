from django.views import generic
from django.db.models import Q

from .models import UserProfile


class IndexView(generic.ListView):
    model = UserProfile
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
