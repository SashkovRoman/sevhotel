from notifications.model.common import EmailNotificationBaze, MessageNotificationBaze, NotificationBaze


class BookingConfirm(NotificationBaze, EmailNotificationBaze, MessageNotificationBaze):
    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'
