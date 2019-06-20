from django.views.generic import TemplateView


class DashboardView(TemplateView):

    template_name = 'djblog/dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context

