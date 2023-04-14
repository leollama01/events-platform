# from django.http import JsonResponse
from django.shortcuts import redirect, render
from user.models import Event, Payment, User

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


def event_insert(request):
    if request.method == 'POST':
        can_save = True
        name = request.POST.get('name')
        date = request.POST.get('date')
        local = request.POST.get('local')
        description = request.POST.get('description')
        free_space = request.POST.get('free_space')

        for i in request.POST:
            if request.POST[i] == '':
                can_save = False

        if can_save:
            try:
                Event(
                    name=name, date=date, local=local, description=description,
                    free_space=free_space
                ).save()

                my_context = {
                    'success': True
                }

            except Exception:
                my_context = {
                    'fail': 'Não foi possível adicionar um novo evento.'
                }

        else:
            my_context = {
                'fail': 'Preencha todos os campos.'
            }

        return render(request, 'user/event_insert.html', my_context)

    return render(request, 'user/event_insert.html')


def event_info(request, id):
    my_context = {}

    if id == 0:
        my_context['events'] = Event.objects.all()
        return render(request, 'user/event.html', my_context)

    else:
        try:
            event = Event.objects.get(id=id)
            _date = f"{str(event.date.year)}-{str(event.date.month).zfill(2)}-{str(event.date.day).zfill(2)}"

            my_context['event_info'] = {
                'id': event.id,
                'name': event.name,
                'date': _date,
                'local': event.local,
                'description': event.description,
                'free_space': event.free_space,
            }

            return render(request, 'user/event.html', my_context)

        except Exception:
            return redirect('/')


def event_update(request, id):
    my_context = {
        'events': Event.objects.all()
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        local = request.POST.get('local')
        description = request.POST.get('description')
        free_space = request.POST.get('free_space')

        try:
            Event.objects.filter(id=id).update(
                name=name, date=date, local=local, description=description,
                free_space=free_space
            )

            my_context['success'] = 'Evento atualizado com sucesso.'

        except Exception:
            my_context['fail'] = 'Falha ao atualizar evento.'

        return render(request, 'user/event.html', my_context)

    else:
        return redirect('/event/info/' + str(id) + '/')


def event_delete(request, id):
    my_context = {
        'events': Event.objects.all()
    }

    try:
        Event.objects.get(id=id).delete()
        my_context['success'] = 'Evento excluído com sucesso.'

    except Exception:
        my_context['fail'] = 'Não foi possível excluir o evento selecionado.'

    return render(request, 'user/event.html', my_context)


def payment_insert(request):
    my_context = {
        'payment_method': dict(Payment.payment_method)
    }

    if request.method == 'POST':
        can_save = True
        value = request.POST.get('value')
        date = request.POST.get('date')
        status = request.POST.get('status')
        method = request.POST.get('method')

        status = True if status is not None else False

        for i in request.POST:
            if request.POST[i] == '':
                can_save = False

        if can_save:
            try:
                Payment(
                    value=value, date=date, status=status, method=method
                ).save()

                my_context['success'] = True

            except Exception:
                my_context['fail'] = 'Não foi possível adicionar um novo pagamento.'

        else:
            my_context['fail'] = 'Preencha todos os campos.'

        return render(request, 'user/payment_insert.html', my_context)

    return render(request, 'user/payment_insert.html', my_context)


def payment_info(request, id):
    my_context = {}

    if id == 0:
        my_context['payments'] = Payment.objects.all()
        return render(request, 'user/payment.html', my_context)

    else:
        try:
            payment = Payment.objects.get(id=id)
            _date = f"{str(payment.date.year)}-{str(payment.date.month).zfill(2)}-{str(payment.date.day).zfill(2)}"

            my_context['payment_info'] = {
                'id': payment.id,
                'value': payment.value,
                'date': _date,
                'status': payment.status,
                'method': payment.method,
                'payment_method': dict(Payment.payment_method)
            }

            return render(request, 'user/payment.html', my_context)

        except Exception:
            return redirect('/')


def payment_update(request, id):
    my_context = {
        'payments': Payment.objects.all()
    }

    if request.method == 'POST':
        value = request.POST.get('value')
        date = request.POST.get('date')
        status = request.POST.get('status')
        method = request.POST.get('method')

        status = True if status is not None else False

        try:
            Payment.objects.filter(id=id).update(
                value=value, date=date, status=status, method=method
            )

            my_context['success'] = 'Pagamento atualizado com sucesso.'

        except Exception:
            my_context['fail'] = 'Falha ao atualizar pagamento.'

        return render(request, 'user/payment.html', my_context)

    else:
        return redirect('/payment/info/' + str(id) + '/')


def payment_delete(request, id):
    my_context = {
        'payments': Payment.objects.all()
    }

    try:
        Payment.objects.get(id=id).delete()
        my_context['success'] = 'Pagamento excluído com sucesso.'

    except Exception:
        my_context['fail'] = 'Não foi possível excluir o pagamento selecionado.'

    return render(request, 'user/payment.html', my_context)
