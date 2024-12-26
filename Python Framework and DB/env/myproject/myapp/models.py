from django.db import models


class ProductMst(models.Model):
    product_id = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


class ProductSubCat(models.Model):
    product = models.ForeignKey(ProductMst, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_images/")
    model = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product.product_name} - {self.model}"


class Employee(models.Model):
    CHOICES = [
        ("Admin", "Admin"),
        ("Product Manager", "Product Manager"),
    ]
    name = models.CharField(max_length=50)
    employee_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    pin = models.IntegerField(blank=False, null=False)
    role = models.CharField(max_length=40, choices=CHOICES)

    def __str__(self):
        return f"{self.name} - {self.role}"
