from django.db import models

# Customer model
class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Product model
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Order model
class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateField()
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order_id} by {self.customer.name}"