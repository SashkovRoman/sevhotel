from django.db import models
from sevhotel.settings_prod import EMAIL_HOST, EMAIL_HOST_USER


class NotificationBaze(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=256, blank=True, null=True, default=None,
                            help_text='Название.')

    def __str__(self):
        if self.name:
            return "%s" % self.name
        return '%s object (%s)' % (self.__class__.__name__, self.pk)


class EmailNotificationBaze(models.Model):
    send_emails = models.BooleanField(default=True)

    email_host = EMAIL_HOST
    from_email = EMAIL_HOST_USER
    # from_email = 'sashkovroman@yandex.ru'

    recipient_list = models.TextField(blank=True, null=True, default=None,
                                      help_text='Список получателей (через запятую).')
    subject_template = models.TextField(blank=True, null=True, default=None,
                                        help_text='Шаблон темы письма.')
    message_template = models.TextField(blank=True, null=True, default=None,
                                        help_text='Шаблон текстового сообщения.')
    html_message_template = models.TextField(blank=True, null=True, default=None,
                                             help_text='Шаблон HTML сообщения.')

    class Meta:
        abstract = True


class MessageNotificationBaze(models.Model):
    send_messages = models.BooleanField(default=True)
    info_message_template = models.TextField(blank=True, null=True, default=None,
                                             help_text='Шаблон информационного сообщения.')
    success_message_template = models.TextField(blank=True, null=True, default=None,
                                                help_text='Шаблон сообщения об успешной операции.')
    warning_message_template = models.TextField(blank=True, null=True, default=None,
                                                help_text='Шаблон предупреждающего сообщения.')
    error_message_template = models.TextField(blank=True, null=True, default=None,
                                              help_text='Шаблон сообщения об ошибке.')

    class Meta:
        abstract = True
