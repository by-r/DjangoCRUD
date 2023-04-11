# Basic CRUD Functions for Django (CBV)
Reference for CRUD operations
- CreateView 
- ListView
- UpdateView
- DeleteView

## MUST IMPORT
views.py
```py
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
```

## CreateView
views.py
```py
class MODELNAMECreateView(CreateView):
    model = MODELNAME
    fields = '__all__'
    template_name = "APPNAME/MODELNAME_create.html"
    success_url = reverse_lazy('MODELNAMEList')
```
template file
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="save">
</form>
```

## ListView
views.py
```py
class MODELNAMEListView(ListView):
    model = MODELNAME

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
```
template file
```html
<a href="{% url 'MODELNAMECreate' %}">Create</a>
<ul>
{% for MODELNAME in object_list %}
    <li>
        {{ MODELNAME.name }} | {{ MODELNAME.companyname}} | {{ MODELNAME.ic }} | {{ MODELNAME.date }} | 
        <a href="{% url 'MODELNAMEDelete' MODELNAME.pk %}">Delete</a> | 
        <a href="{% url 'MODELNAMEUpdate' MODELNAME.pk %}">Edit</a> 
    </li>    
    {% endfor %}
</ul>
```

## UpdateView
views.py
```py
class MODELNAMEUpdateView(UpdateView):
    model = MODELNAME
    fields = '__all__'
    template_name = "APPNAME/MODELNAME_update.html"
    success_url = reverse_lazy('MODELNAMEList')
```
template file
```html
<form method="post"> 
    {% csrf_token %} 
    {{ form.as_p }} 
    <input type="submit" value="Save"> 
</form> 
```

## DeleteView
views.py
```py
class MODELNAMEDeleteView(DeleteView):
    model = MODELNAME
    success_url = reverse_lazy('MODELNAMEList')
```
template file
```html
<form method="post">
    {% csrf_token %}
    <p>Are you sure you want to delete "{{ object }}"?</p>
    {{ form }}
    <input type="submit" value="Confirm">
</form>
```