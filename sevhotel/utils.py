from django.http import HttpResponseRedirect


def update_request_session(request, form):
    for field in form.fields:
        request.session.update({field: str(form.cleaned_data[field])})


class BookingMixin:
    template = None
    context = None

    def post(self, request, *args, **kwargs):
        form = self.context['form'](request.POST)
        if form.is_valid():
            update_request_session(request, form)
            form.save(request=request)
        return HttpResponseRedirect(request.path_info)


# from django import forms
# password = forms.CharField(max_length=32, widget=forms.PasswordInput)
