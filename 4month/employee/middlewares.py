from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class ExperienceJobMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience = int(request.POST.get('experience'))
            if experience < 2:
                return HttpResponseBadRequest('Experience cannot be less than 2.')
            elif experience >  2:
                request.category = "Junior"
            elif 2 <= experience <= 4:
                request.category = "Strong Junior"
            elif 4 <= experience <= 8:
                request.category = "Middle"
            elif 8 <= experience <= 12:
                request.category = "Strong Middle"
            elif 12 <= experience <= 18:
                request.category = "Senior"
            elif 18 <= experience <= 30:
                request.category = "Strong Senior"
            else:
                request.category = "Category is not Defined"
        elif request.path == '/register/ ' and request.method == 'GET':
            setattr(request, 'experience', 'Category of employee is not defined')
