from django.shortcuts import HttpResponse

# Create your views here.
def book_list(request):
    response = """
    <html>
    <head>
        <title>Book list</title>
    </head>
    <body>
    <h1>Kitoblar ro'yxati</h1>
    <ul>
        <li><a href="/alibobo">Alibobo va qirq qaroqchi</a></li>
        <li><a href="/mening_urgigina_bolama">Mening ug'rigina bolama</a></li>
        <li><a href="zumrad_va_qimmat">Zumrad va Qimmat</a></li>
    </ul>
    </body>
    
    """

    return HttpResponse(response)

def alibobo(request):
    response = """
        <html>
        <head>
            <title>Alibobo va qirq qaroqchi</title>
        </head>
        <body>
        <h1>Alibobo va qirq qaroqchi</h1>
        <p><strong>Author:</strong> Arab xalq ertaklari</p>
        <p>Burun zamonda o'tgan xalqlarning rivoyatlariga ko'ra, Eron...</p>
        <a href="../">Back to list</a>
        </body>
        """

    return HttpResponse(response)

def mening_urgigina_bolama(request):
    response = """
        <html>
        <head>
            <title>Mening ug'rigina bolama</title>
        </head>
        <body>
        <h1>Mening ug'rigina bolama</h1>
        <p><strong>Author:</strong> G'afur Gʻulom</p>
        <p>Hadeb zarbdorlarni maqtayverish ham zeriktiradi. Ora-sira...</p>
        <a href="../">Back to list</a>
        </body>
        """

    return HttpResponse(response)

def zumrad_va_qimmat(request):
    response = """
        <html>
        <head>
            <title>Zumrad va Qimmat</title>
        </head>
        <body>
        <h1>Zumrad va Qimmat</h1>
        <p><strong>Author:</strong> O'zbek xalq ertaklari</p>
        <p>Bir zamonda katta bir soy bo'yida kichkina uy bo'lar ekan. Bu uyda...</p>
        <a href="../">Back to list</a>
        </body>
        """

    return HttpResponse(response)