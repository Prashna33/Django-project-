from .models import Pages


def pages_links(request):
    pages = Page.object.all()
    return {'pages': pages}
    