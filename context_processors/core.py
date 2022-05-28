from main.models import Website
def core_processors(request):
    website = Website.objects.last()
    return {
        "website": website
        }