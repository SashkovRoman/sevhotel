from django import forms

from django.contrib import messages
from django.core.mail import send_mail

from booking.models.models import Guest

from notifications.model.models import BookingConfirm
from django.template import Context, Template

from smtplib import SMTPException


class GuestForm(forms.ModelForm):
    _confirm = None
    _request = None

    def save(self, commit=True, request=None):
        self._request = request
        self._confirm = BookingConfirm.objects.filter(is_active=True).last()

        super(GuestForm, self).save(commit=commit)

        if self._confirm is None:
            return

        if self._confirm.send_emails:
            _subject = Template(self._confirm.subject_template).render(Context(self.cleaned_data))
            _message = Template(self._confirm.message_template).render(Context(self.cleaned_data))
            _from_email = self._confirm.from_email
            _recipient_list = [s.strip() for s in self._confirm.recipient_list.split(sep=',')]
            print(_recipient_list)
            _html_message = Template(self._confirm.html_message_template).render(Context(self.cleaned_data))
            try:
                send_mail(_subject, _message, _from_email, _recipient_list, html_message=_html_message,
                          fail_silently=False, )
            except SMTPException as ex:
                pass

            if self._confirm.send_messages and self._request is not None:
                messages.success(request,
                                 Template(self._confirm.success_message_template).render(Context(self.cleaned_data)))

    class Meta:
        model = Guest
        exclude = []
