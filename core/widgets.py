from django import forms
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.urls import reverse


class BlobImagePickerWidget(forms.ClearableFileInput):
    """
    A custom widget that extends Django's ClearableFileInput to add a button
    for selecting images from the Azure Blob Storage gallery.
    """
    template_name = 'widgets/blob_image_picker.html'
    
    class Media:
        css = {
            'all': ('css/blob_image_picker.css',)
        }
        js = ('js/blob_image_picker.js',)
    
    def render(self, name, value, attrs=None, renderer=None):
        # First, render the standard file input
        standard_widget = super().render(name, value, attrs, renderer)
        
        # Add our custom gallery picker button
        gallery_url = reverse('admin:blob_image_gallery')
        
        context = {
            'standard_widget': standard_widget,
            'name': name,
            'gallery_url': gallery_url,
            'value': value,
        }
        
        return mark_safe(render_to_string(self.template_name, context))
