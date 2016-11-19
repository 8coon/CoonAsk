from cgi import parse_qs


def application(env, start_response):
    query = parse_qs(env['QUERY_STRING'], keep_blank_values=True)
    body = list()

    body.append('<h1>it kinda works...</h1>')
    body.append('<strong>CONSIDER THIS:</strong><br><GET parameters:<br>')

    for k, v in query.items():
        for item in v:
            body.append(k + ' = ' + item + "<br>")

    body.append('<br>POST parameters:<br>')
    query = parse_qs(env['wsgi.input'].readline().decode())

    for k, v in query.items():
        for item in v:
            body.append(k + ' = ' + item + "<br>")

    start_response('200 OK', [('Content-Type', 'text/html')])
    return body
