from django.db import models
from django.conf import settings
from datetime import datetime
from django.shortcuts import reverse


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    discount_price = models.FloatField(blank=True, null=True,default=0)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("store:shopsingle", kwargs={
            'slug': self.slug

        })

    def get_add_to_cart_url(self):
        return reverse("store:add-to-cart", kwargs={
            'slug': self.slug

        })

    def get_remove_from_cart_url(self):
        return reverse("store:remove-from-cart", kwargs={
            'slug': self.slug

        })


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, )
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=False)

    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    ordered_date = models.DateTimeField(default=datetime.now, blank=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()

        return total
