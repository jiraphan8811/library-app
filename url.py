import justpy as jp

# @jp.SetRoute('/hello')
# def hello_function():
#     wp = jp.WebPage()
#     wp.add(jp.P(text='Hello there!', classes='text-5xl m-2'))
#     return wp

# @jp.SetRoute('/bye')
# def bye_function():
#     wp = jp.WebPage()
#     wp.add(jp.P(text='Goodbye!', classes='text-5xl m-2'))
#     return wp

# def greeting_function(request):
#     wp = jp.WebPage()
#     wp.add(jp.P(text=f'Hello there, {request.path_params["name"]}!', classes='text-base'))
#     return wp
# jp.Route('/hello/{name}', greeting_function)

def home():
    wp = jp.WebPage()
    wp.add(jp.P(text='ANCA Library', classes='text-lg m-4'))
    wp.add(jp.P(text='Book Title: ', classes='text-base m-4'))
    

    return wp

jp.justpy(home)