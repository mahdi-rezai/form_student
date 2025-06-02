from django.contrib import admin
from .models import Student  # Import your model

# Register Student model with admin panel
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'major')  # Fields to display in list view
    search_fields = ('first_name', 'last_name', 'major')  # Enable search for these fields
    list_filter = ('age', 'major')  # Add filters on the right sidebar

    # (Optional) Customize how fields are grouped in add/edit form
    fieldsets = [
        ('Personal Info', {'fields': ('first_name', 'last_name', 'age')}),
        ('Academic Info', {'fields': ('major',)}),
    ]