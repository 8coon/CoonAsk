from cgi import parse_qs


def application(env, start_response):
    query = parse_qs(env['QUERY_STRING'], keep_blank_values=True)
    body = list()

    body.append('<h1>it kinda works...</h1>')
    body.append('<strong>CONSIDER THIS:</strong><br>')

    for key, values in query.items():
        for item in values:
            body.append(key + ' = ' + item + "<br>")

    start_response('200 OK', [('Content-Type', 'text/html')])
    return body
