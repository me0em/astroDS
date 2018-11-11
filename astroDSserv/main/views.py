from django.views.decorators.http import *
from django.shortcuts import render
import numpy as np
import classification_model
import ugriz_to_UBVRI as phconv

def classify(MODEL, u, g, r, i, z):
    return MODEL.predict([(u, g, r, i, z)])

def stars_perf(ugriz):
    jester = phconv.Jester('star', ugriz)
    karaali = phconv.Karaali('star', ugriz)
    lupton = phconv.Lupton('star', ugriz)
    U_B = B_V = list()

    if jester is not None:
        U_B.append(jester['U_B'])
        B_V.append(jester['B_V'])

    if karaali is not None:
        B_V.append(karaali['B_V'])

    if lupton is not None:
        B_V.append(lupton['B_V'])

    result = dict()
    result['U_B'] = np.mean(U_B)
    result['B_V'] = np.mean(B_V)
    return result

#
# Login page
@require_http_methods(["GET", "POST"])
def render_main_page(request):
    if 'u_Band' in request.POST:
        u = request.POST['u_Band']
        g = request.POST['g_Band']
        r = request.POST['r_Band']
        i = request.POST['i_Band']
        z = request.POST['z_Band']

        ugriz = list(map(lambda x: float(x), (u, g, r, i, z)))

        obj = classify(classification_model.MODEL, u, g, r, i, z)
        TYPE = list(obj)[0]


        temperature = None
        if TYPE == 'STAR':
            TYPE = 'star'
            result = stars_perf(ugriz)
            U_B = result['U_B']
            B_V = result['B_V']
            temperature = round(4600*(1/(0.92*(B_V)+1.7) + 1/(0.92*(B_V)+0.62)), 3)

        if TYPE == 'GALAXY':
            TYPE = 'galaxy'

        if TYPE == 'QSO':
            TYPE = 'quasar'

        payload = {'TYPE': TYPE, 'TEMPERATURE': temperature}
    else:
        payload = dict()
    return render(request, 'main.html', payload)

@require_http_methods(["GET", "POST"])
def render_visualize_page(request, temp):
    temp = float(temp)
    if temp < 3500:
        res = ('M', 'red')
    if 3500<temp<5000:
        res = ('K', 'orange')
    if 5000<temp<6000:
        res = ('G', 'yellow')
    if 6000<temp<7500:
        res = ('G', 'yellow')
    if 7500<temp<10000:
        res = ('O', 'blue')
    if 10000<temp:
        res = ('O', 'blue')

    import webbrowser as wb
    PORT = 8555
    CLASS = res[0]
    url = f'http://127.0.0.1:{PORT}/wrapper/{CLASS}/index.html'
    wb.open(url, new=2)

    return render(request, 'main.html', {})
