from .models import *
from bootstrap_modal_forms.forms import BSModalModelForm


class BusModelForm(BSModalModelForm):
    class Meta:
        model = Buss
        fields = ['plate_no', 'driver_assigned', 'attendant_assigned', 'capacity', 'status']