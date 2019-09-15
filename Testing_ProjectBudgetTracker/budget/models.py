from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Project(models.Model):
    name   = models.CharField(max_length=100)
    slug   = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def budget_left(self):
        project_expense_list = Expense.objects.filter(project=self)
        total_expense_amount = 0
        for expense in project_expense_list:
            total_expense_amount += int(expense.amount)

        return self.budget - total_expense_amount

    @property
    def total_transactions(self):
        project_expense_list = Expense.objects.filter(project=self)
        return project_expense_list.count()

    def get_absolute_url(self):
        return reverse('budget:detail', kwargs={'project_slug': self.slug})


class Category(models.Model):
    name    = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Expense(models.Model):
    title    = models.CharField(max_length=100)
    amount   = models.DecimalField(max_digits=8, decimal_places=2)
    project  = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-amount',)

