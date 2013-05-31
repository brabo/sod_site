from django.forms import ModelChoiceField

class Countries(ModelChoiceField):
    def country(self, obj):
        return "Country #%i" % obj.country
