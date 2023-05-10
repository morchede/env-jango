from django.shortcuts import redirect, render , get_object_or_404
from .models import Produit
from .models import Fournisseur
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm,UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse_lazy

def index(request):
       if request.method == "POST" :
         form = ProduitForm(request.POST,request.FILES)
         if form.is_valid():
              form.save() 
              list=Produit.objects.all()
              return render(request,'magasin/vitrine.html',{'list':list})
       else : 
            form = ProduitForm() #créer formulaire vide 
            list=Produit.objects.all()
            return render(request,'magasin/majProduits.html',{'form':form,'list':list})

def indexA(request):
     return render(request,'magasin/acceuil.html' )


def indexF(request):
    fournisseurs = Fournisseur.objects.all()
    context = {'fournisseurs': fournisseurs}
    return render(request, 'magasin/mesFournisseurs.html', context)

def nouveauFournisseur(request):
    if request.method == "POST" :
         form = FournisseurForm(request.POST,request.FILES)
         if form.is_valid():
              form.save() 
              nouvFournisseur=Fournisseur.objects.all()
              return render(request,'magasin/vitrineF.html',{'nouvFournisseur':nouvFournisseur})
    else : 
            form = FournisseurForm() #créer formulaire vide 
            nouvFournisseur=Fournisseur.objects.all()
            return render(request,'magasin/fournisseur.html',{'form':form,'nouvFournisseur':nouvFournisseur})
def Catalogue(request):
        products= Produit.objects.all()
        context={'products':products}
        return render( request,'magasin/mesProduits.html',context )

def register(request):
     if request.method == 'POST' :
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password1')
               user = authenticate(username=username, password=password)
               login(request,user)
               messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
               return redirect('home')
     else :
          form = UserCreationForm()
     return render(request,'registration/register.html',{'form' : form})

def edit_product(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # Récupérer l'instance du modèle produit
            produit = form.save(commit=False)
            # Récupérer la nouvelle image téléchargée
            nouvelle_image = form.cleaned_data['img']
            # Si une nouvelle image a été téléchargée, la sauvegarder
            if nouvelle_image:
                produit.img = nouvelle_image
            # Sauvegarder le produit
            produit.save()
            return redirect('Catalogue')
    else:
        form = ProduitForm(instance=product)
    return render(request, 'magasin/edit_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('Catalogue')
    return render(request, 'magasin/delete_product.html', {'product': product})

def detail_product(request, product_id):
    produit = get_object_or_404(Produit, id=product_id)
    context = {'produit': produit}
    return render(request, 'magasin/detail_product.html', context)
