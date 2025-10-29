from django.shortcuts  import render
from .forms import TacheForm

def home(request):
    return render(request,'taches/home.html')

def new(request):
    form = TacheForm()
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            # Crée une instance du modèle sans sauvegarder (commit=False)
            tache = form.save(commit=False)
            tache.title = tache.title.capitalize()
            print('Enregistrement en bdd')
            tache.save()  # Enregistre en BDD !
            form = TacheForm() # Reset le formulaire
    return render(request,'taches/new.html', {'form':form})