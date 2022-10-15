from django.shortcuts import render
from django.views import View
from .forms import NumbersForm


class HomeView(View):
    form_class =NumbersForm

    def get(self, request):
        return render(request, 'num/form_numbers.html', {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            if 'soudi' in request.POST:
                print('soudi')
                lis = form.cleaned_data.values()
                dic = form.cleaned_data
                key_form = list(dic.keys())
                int_lis = [eval(i) for i in lis]
                sort_list = sorted(int_lis)
                new_dic = {}
                for i in range(0, 10):
                    new_dic[key_form[i]] = sort_list[i]
                form = NumbersForm(initial=new_dic)
                return render(request, 'num/form_numbers.html', {'form': form})
            if 'nozouli' in request.POST:
                lis = form.cleaned_data.values()
                int_lis = [eval(i) for i in lis]
                sort_list = sorted(int_lis)
                sort_list.reverse()
                form.value = sort_list
                dic = form.cleaned_data
                new_dic = {}
                key_form = list(dic.keys())
                for i in range(0, 10):
                    new_dic[key_form[i]] = sort_list[i]
                form = NumbersForm(initial=new_dic)
                return render(request, 'num/form_numbers.html', {'form': form})
