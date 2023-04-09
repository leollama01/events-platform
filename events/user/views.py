# from django.http import JsonResponse
from django.shortcuts import redirect, render
from user.models import User

# Create your views here.

'''
    Some strings will be in portuguese to use in templates.
    Again, feel free to translate if u need.
'''


def index(request):
    return render(request, 'index.html')


def user_insert(request):
    if request.method == 'POST':
        can_save = True
        name = request.POST.get('name')
        age = request.POST.get('age')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        for i in request.POST:
            if request.POST[i] == '':
                can_save = False

        if can_save:
            try:
                User(
                    name=name, age=age, country=country, state=state,
                    city=city, phone_number=phone_number, email=email
                ).save()

                my_context = {
                    'success': True
                }

            except Exception:
                my_context = {
                    'fail': 'Não foi possível adicionar um novo usuário.'
                }

        else:
            my_context = {
                'fail': 'Preencha todos os campos.'
            }

        return render(request, 'user/user_insert.html', my_context)

    return render(request, 'user/user_insert.html')


def user_info(request, id):
    my_context = {}

    if id == 0:
        my_context['users'] = User.objects.all()
        return render(request, 'user/user.html', my_context)

    else:
        try:
            user = User.objects.get(id=id)
            my_context['user_info'] = {
                'id': user.id,
                'name': user.name,
                'age': user.age,
                'country': user.country,
                'state': user.state,
                'city': user.city,
                'phone_number': user.phone_number,
                'email': user.email
            }

            return render(request, 'user/user.html', my_context)

        except Exception:
            return redirect('/')


def user_update(request, id):
    my_context = {
        'users': User.objects.all()
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        try:
            User.objects.filter(id=id).update(
                name=name, age=age, country=country, state=state,
                city=city, phone_number=phone_number, email=email
            )

            my_context['success'] = 'Usuário atualizado com sucesso.'

        except Exception:
            my_context['fail'] = 'Falha ao atualizar usuário.'

        return render(request, 'user/user.html', my_context)

    else:
        return redirect('/user/info/' + str(id) + '/')


def user_delete(request, id):
    my_context = {
        'users': User.objects.all()
    }

    try:
        User.objects.get(id=id).delete()
        my_context['success'] = 'Usuário excluído com sucesso.'

    except Exception:
        my_context['fail'] = 'Não foi possível excluir o usuário selecionado.'

    return render(request, 'user/user.html', my_context)
