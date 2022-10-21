from django.db import models

class Purchase(models.Model):
    name = models.TextField()
    phone = models.TextField()
    town = models.TextField()
    
def profile_create(name,phone,town):
    newp = Purchase(name = name, phone = phone, town = town)
    newp.save()
    return newp

def all_profiles():
    return Purchase.objects.all()

def find_by_name(customer):
    return Purchase.objects.get(name = customer)

def find_by_town(town):
    f = Purchase.objects.filter(name = town)
    if len(f) == 0:
        return None
    return Purchase.objects.get(name = town)

def delete(name):
    f = Purchase.objects.filter(name = name)
    if len(f) == 0:
        return None
    return Purchase.objects.filter(name = name).delete()