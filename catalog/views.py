from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        actual_versions = []
        for product in self.object_list:
            current_version = Version.objects.filter(is_current=True, product=product).first()
            actual_versions.append(current_version)
        context['actual_versions'] = actual_versions
        return context


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product
    template_name = 'catalog/product.html'


class ContactsTemplateView(TemplateView):
    model = Product
    template_name = 'catalog/contacts.html'


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.salesman = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class VersionCreateView(CreateView, LoginRequiredMixin):
    model = Version
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
