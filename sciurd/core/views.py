from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.core.urlresolvers import reverse_lazy

from core.models import Pastor, Esposa, Filho, Igreja, Carro
from core.forms import (PastorForm, EsposaForm, FilhoForm, IgrejaForm, CarroForm,
)


class HomeView(TemplateView):
    template_name = 'index.html'


class PastorCreateView(CreateView):
    template_name = 'add.html'
    form_class = PastorForm
    model = Pastor
    success_url = reverse_lazy('pastor-add')

    def salva(request):
        if request.method == 'POST':
            form = PastorForm(request.POST)
            if form.is_valid():
                context['is_valid'] = True
                form =PastorForm()

    #def get_context_data(self, **kwargs):
     #   context = super(PastorCreateView, self).get_context_data(**kwargs)
     #   context['cadastro'] = 'Pastor'
     #   form = PastorForm()
      #  if form.is_valid():
       #     context['is_valid']= True
      #  form = PastorForm()
      #  return context


class PastorListView(ListView):
    template_name = 'pastor_list.html'
    model = Pastor
    context = 'pastor_list'
    paginate_by = 5

    def get_queryset(self, **kwargs):
        pastor_list = Pastor.objects.filter.all()
        return Pastor.objects.filter(status='nome')



class PastorDetailView(DetailView):
    slug_field = 'nome'
    model = Pastor
    template_name = 'detalhe_pastor.html'
    context_object_name = 'pastor'

    
    #def get_queryset(self)
     #   return self.model.filter(user=self.request.user)
    
class PastorUpdateView(UpdateView, ):
    template_name = 'pastor-add.html'
    form_class = PastorForm
    model = Pastor
    success_url = reverse_lazy('pastor-edit')




#def pastor_listing(request):
 #   """ A view of all bands. """
  #  pastores = Pastor.objects.all()
   # template_name = pastor_edit.html
    #var_get_search = request.GET.get('search_box')
    #if var_get_search is not None:
    #    pastores = pastores.filter(name__icontains=var_get_search)
    #return render(request, 'pastor_edit.html', {'pastor': pastor})




class PastorDeleteView(DeleteView):
    template_name = 'pastor_delete.html'
    model = Pastor
    success_url = reverse_lazy('pastor-list')




class EsposaCreateView(CreateView):
    form_class = EsposaForm
    template_name = 'esposa.html'
    model = Esposa
    success_url = reverse_lazy('esposa-list')

    def get_context_data(self, **kwargs):
        context = super(EsposaCreateView, self).get_context_data(**kwargs)
        context['cadastro'] = 'Esposa'

        return context


class EsposaListView(ListView):
    model = Esposa
    success_url = reverse_lazy('listar')


class EsposaDetailView(DetailView):
    model = Esposa


class EsposaUpdateView(UpdateView):
    model = Esposa
    success_url = reverse_lazy('esposa-list')


class EsposaDeleteView(DeleteView):
    model = Esposa
    success_url = reverse_lazy('esposa-list')


class FilhoListView(ListView):
    model = Filho


class FilhoDetailView(DetailView):
    model = Filho


class FilhoCreateView(CreateView):
    form_class = FilhoForm
    model = Filho
    success_url = reverse_lazy('filho-list')
    template_name = 'add.html'

    def get_context_data(self, **kwargs):
        context = super(FilhoCreateView, self).get_context_data(**kwargs)
        context['cadastro'] = 'Filho'
        return context


class FilhoUpdateView(UpdateView):
    model = Filho
    success_url = reverse_lazy('filho-list')


class FilhoDeleteView(DeleteView):
    model = Filho
    success_url = reverse_lazy('filho-list')


class IgrejaListView (ListView):
    model = Igreja


class IgrejaDetailView(DetailView):
    model = Igreja


class IgrejaCreateView(CreateView):
    form_class = IgrejaForm
    model = Igreja
    success_url = reverse_lazy('igreja-list')
    template_name = 'add.html'

    def get_context_data(self, **kwargs):
        context = super(IgrejaCreateView, self).get_context_data(**kwargs)
        context['cadastro'] = 'Igreja'
        return context


class IgrejaUpdateView(UpdateView):
    model = Igreja
    success_url = reverse_lazy


class IgrejaDeleteView(DeleteView):
    model = Igreja


class CarroListView(ListView):
    model = Carro


class CarroDetailView(DetailView):
    model = Carro


class CarroCreateView(CreateView):
    form_class = CarroForm
    model = Carro
    success_url = reverse_lazy('carro-list')
    template_name = 'add.html'

    def get_context_data(self, **kwargs):
        context = super(CarroCreateView, self).get_context_data(**kwargs)
        context['cadastro'] = 'Carro'
        return context


class CarroUpdateView(UpdateView):
    model = Carro
    success_url = reverse_lazy('carro-list')


class CarroDeleteView(DeleteView):
    model = Carro
    success_url = reverse_lazy('carro-list')
