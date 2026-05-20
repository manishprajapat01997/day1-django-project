    

from django.db import models
import uuid

from accountapp.models import User
from django.core.validators import MinLengthValidator



def get_empty_response_json():
    return {
        "description": "", "hsn": "", "dims": "",
        "wastage_percent": "","max_qty": "","rack_no":"","shelf":"","level":""
    }
    
    
class Table_name(models.Model):
    TYPE_CHOICES = [
        ('ABC', 'abc'),
        ('XYZ', 'xyz'),
    ]
    id = models.CharField(max_length=20, primary_key=True)
    name=models.CharField(max_length=50,blank=True, null=True,)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    state=models.CharField(max_length=40,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=500,null=True,blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    company_package = models.IntegerField(default=1,null=True,blank=True)
    Accepted_Tc=models.BooleanField(default=True,null=True,blank=True,verbose_name='Accepted Terms and conditions')
    credit_amount=models.FloatField(default=0.0,blank=True)
    payment_date = models.DateField(null=True,blank = True)
    photo = models.ImageField(upload_to="product_photos/", blank=True, null=True)
    stock = models.JSONField(default=get_empty_response_json, blank=True)
    Referred_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name="employees")
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    user_details = models.JSONField(default=list,blank=True, null=True,help_text="List containing user details" )
    # updated_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True,null=True,verbose_name='next_1_date')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    
    
    
    
'''
blank=True →   field is optional in forms/admin/serializer validation
null=True →    database can store NULL value
default→       automatically sets a default value if no value is provided
max_length→    limits maximum number of characters (required for CharField)
unique=True→   prevents duplicate values in database
db_index=True→ creates database index for faster search/filter/query
verbose_name→  custom human-readable field name in Django admin/forms
choices→       restricts field values to predefined options
help_text→     displays help message in admin/forms/serializer docs
upload_to→     defines folder path where uploaded file/image will be stored
primary_key=True→ makes field primary key (unique identifier)
editable=False→   field hidden in admin/forms (cannot edit manually)
auto_now=True→    automatically updates current timestamp on every save
auto_now_add=True→ automatically sets timestamp only when object is created
on_delete=models.CASCADE→ deletes related child records automatically
related_name→             custom reverse relation name
validators→               custom validation before saving
'''
