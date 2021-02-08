import datetime


def get_filename(filename, request):
    return str(int(datetime.datetime.now().timestamp())) + filename.upper()
