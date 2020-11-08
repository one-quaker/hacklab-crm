from prismo.models import SiteConfig


def get_site_config(request):
    ctx = {}
    ctx['site_conf'] = SiteConfig.objects.first()
    return ctx
