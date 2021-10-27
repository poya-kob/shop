from settings.models import SiteSetting


def context_setting(request):
    setting = SiteSetting.objects.first()

    return {
        "setting": setting
    }
