import urllib.request
urls = [
    'http://127.0.0.1:8000/api/analytics/pie/',
    'http://127.0.0.1:8000/api/analytics/bar/',
    'http://127.0.0.1:8000/api/analytics/treemap/'
]
for u in urls:
    try:
        with urllib.request.urlopen(u, timeout=20) as resp:
            data = resp.read().decode('utf-8')
            print('URL:', u)
            print('CODE:', resp.getcode())
            print('BODY:', data[:1600])
    except Exception as e:
        print('URL:', u)
        print('ERROR:', repr(e))
