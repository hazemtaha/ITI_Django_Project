from django import forms

from .models import Properties, PropertiesPhotos

from django.forms.models import inlineformset_factory

class PropertiesForm(forms.ModelForm):
<<<<<<< HEAD
    # then telling which model should be used to create this form

    class Meta:
        model = Properties
        fields = ('title', 'prop_type', 'city', 'neighborhood', 'category',
                  'description', 'price', 'size', 'yt_url', 'position')
# another form for the PropertiesPhotos
# class PropertiesPhotosForm(forms.ModelForm):
# 	class Meta:
# 		model = PropertiesPhotos
# 		fields = ('prop_photo')
=======
	#then telling which model should be used to create this form
	class Meta:
		model = Properties
		fields = ('owner','title', 'prop_type', 'city', 'neighborhood', 'category', 'description', 'price', 'size','yt_url','position')

PropertiesFormSet = inlineformset_factory(
	Properties, PropertiesPhotos, can_delete=False, fields=['prop_photo'])
>>>>>>> 6861b14749aa793cea12a53c76b2a876339ad2c2
