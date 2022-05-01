import justpy as jp
from main import *


def index():
    wp = jp.WebPage()
    wp.add(jp.P(text='Welcome to ANCA Library', classes='text-2xl m-4 text-decoration-line: underline font-weight: 700'))
    wp.add(jp.P(text='Below is the list of all the books we have. Please scan the qr code on the book to borrow the book outside the department.', classes='text-base m-4'))
    d = jp.Div(classes='w-7/8 m-2 p-3 border rounded-lg item-start', a=wp)
    grid = wm_df.jp.ag_grid(a=d)
    for i in range(4):
      grid.options.columnDefs[i].cellStyle = ['justify-self-start']

    return wp


def bookView(request):
    wp = jp.WebPage()
    url = request.path_params["code"].upper()

    for i, (code,title,status,who,since) in enumerate(table_data):
            if code == url:
                wp.add(jp.P(text=f'{table_data[i]}!', classes='text-5xl m-2'))
                break
    
    return wp

def exceptionError(request):
    wp = jp.WebPage()
    url = request.path_params["any"]
    if AssertionError:
        wp.add(jp.P(text=f'NO URL!', classes='text-5xl m-2'))
    return wp


#URL LIST
jp.Route('/{any}', exceptionError)
jp.Route('/{code}', bookView)
jp.Route('/', index)

jp.justpy()