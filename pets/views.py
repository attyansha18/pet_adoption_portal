from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet
from .forms import PetForm

def pet_list(request):
    pets = Pet.objects.filter(available=True)
    return render(request, 'pets/pet_list.html', {'pets': pets})

def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'pets/pet_detail.html', {'pet': pet})

def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'pets/add_pet.html', {'form': form})
