from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import ProjectsListView, ProjectsCreateView, project_detail_view


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('budget:list')
        self.assertEquals(resolve(url).func.view_class, ProjectsListView)

    def test_add_url_resolves(self):
        url = reverse('budget:add')
        self.assertEquals(resolve(url).func.view_class, ProjectsCreateView)

    def test_detail_url_resolves(self):
        url = reverse('budget:detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, project_detail_view)
