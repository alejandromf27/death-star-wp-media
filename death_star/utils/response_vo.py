def json_data(data=None, status='success', message=''):
    """
    this function is a standard Virtual Object (VO) Response, to return a standard response
    :param data: VO with data we are goint to return
    :param status: response status handled independent of http response
    :param message: response message
    :return: standard json data
    """
    return {
        'data': data,
        'status': status,
        'message': message
    }
