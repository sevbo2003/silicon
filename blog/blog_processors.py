from accounts.forms import SubscriberForm


def blog(request):
    return {
        'email_form': SubscriberForm,
    }