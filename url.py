from logging import exception
import justpy as jp
from main import *
import csv

button_classes='m-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 rounded w-56 text-center'
session_data = {}

def index():
    wp = jp.WebPage()
    wp.add(jp.P(text='Welcome to ANCA Library', classes='text-2xl m-4 text-decoration-line: underline font-weight: 700'))
    wp.add(jp.P(text='Below is the list of all the books we have. Please scan the qr code on the book or type /CODE in the url to borrow the book outside the department.', classes='text-base m-4'))
    d = jp.Div(classes='w-7/8 m-2 p-3 border rounded-lg item-start', a=wp)
    grid = wm_df.jp.ag_grid(a=d)
    for i in range(4):
      grid.options.columnDefs[i].cellStyle = ['justify-self-start']

    return wp

def submit_form(self, msg):
    # print(msg)
    msg.page.redirect = '/'
    session_data[msg.session_id] = msg.form_data
    for d in msg.form_data:
        print(d["value"])
    # print(msg.form_data)


def writecsv(filename,data):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def bookView(request):
    wp = jp.WebPage()
    url = request.path_params["code"].upper()
    loadcount = 0
    for i, (code,title,status,who,since) in enumerate(table_data):
        if code == url:
            wp.add(jp.P(text=f'Book Title: {table_data[i][1]}', classes='text-base m-2 font-bold'))
            wp.add(jp.P(text=f'Book Code: {table_data[i][0]}', classes='text-base m-2'))
            wp.add(jp.P(text=f'Status: {table_data[i][2]}', classes='text-base m-2'))
            wp.add(jp.P(text=f'Checked out by: {table_data[i][3]}', classes='text-base m-2'))
            wp.add(jp.P(text=f'Since: {table_data[i][4]}', classes='text-base m-2'))
            wp.add(jp.Br())

            form1 = jp.Form(a=wp, classes='border m-1 p-1 w-72')
            user_label = jp.Label(text='Enter your name before clicking button', classes='block uppercase tracking-wide text-gray-700 text-xs mb-2', a=form1)
            in1 = jp.Input(placeholder='Enter your name', a=form1, classes='form-input')
            # user_label.for_component = in1

            submit_button = jp.Input(value='Click to Borrow', type='submit', a=form1, classes=button_classes)
            loadcount +=1
            form1.on('submit', submit_form)

            print(session_data)
            
            # table_data[i][2] = 'Unavailable'
            # table_data[i][3] = user


            # break
    
    if loadcount == 0:
        wp.add(jp.P(text='NO URL!', classes='text-5xl m-2'))
    wp.add(jp.A(text='Book list', href='/', classes='m-2 text-base text-blue-600 underline'))
    return wp


jp.Route('/{code}', bookView)
jp.Route('/', index)
jp.justpy()