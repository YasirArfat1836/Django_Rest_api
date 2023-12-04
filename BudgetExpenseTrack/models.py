from django.db import models


class Users(models.Model):
    user_id = models.IntegerField(null=False, primary_key=True,auto_created=True)
    user_name = models.TextField(max_length=200)


class Category(models.Model):
    category_id = models.IntegerField(null=False, primary_key=True)
    category_name = models.TextField(max_length=200)


class Expenses(models.Model):
    expense_id = models.IntegerField(null=False, primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    Expense_name = models.TextField(max_length=200)
    Expense_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return f"{self.Expense_name} - {self.Expense_amount}"
