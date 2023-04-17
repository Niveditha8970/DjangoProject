'''
def middlewarename(get_response):
    code to be written that need to be executed
    only once i.e for initialization or for configuration

    def your_functionname(request):
        code need to executed before views function is called
        varable=get_response(request)
        code need to executed after views function is executed.

        return variable

    return your_functionname

'''

def wolf_middleware(get_response):

    #print("code need to be executed only once ")
    #print("Code required for initalization and configration")

    def my_middleware(request):
        #print("code to be executed before views function calls")
        #print("Program control is in my_middleware function")

        res=get_response(request)

        #print("code to be executed after view function called")
        #print("program control is in my_middleware after views called")

        return res

    return my_middleware