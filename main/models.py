from django.db import models


class Route(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=70, null=True, blank=True)
    start_address = models.CharField(max_length=70, null=True, blank=True)
    end_address = models.CharField(max_length=70, null=True, blank=True)
    way_points = models.TextField(max_length=400, null=True, blank=True)
    time = models.CharField(max_length=20, null=True, blank=True)
    distance = models.CharField(max_length=20, null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
    	return f'{self.name}'
          

class Trip(models.Model):
    trip = models.ForeignKey(Route, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    trip_ref_no = models.PositiveIntegerField(null=True, blank=True)
    type = models.CharField(max_length=50, null=True, default="PickUp")
    details = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return f'{self.trip_ref_no}'


class Buss(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    plate_no = models.CharField(max_length=25, null=True, blank=True)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    condition = models.BooleanField(default=False)
    driver_assigned = models.CharField(max_length=100, null=True, blank=True)
    attendant_assigned = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, default="Parking")
    current_address = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return f'{self.plate_no}'
    
    class Meta:
        unique_together = ['plate_no', 'driver_assigned', 'attendant_assigned']
