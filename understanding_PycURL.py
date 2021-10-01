import pycurl
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

c = pycurl.Curl()

c.setopt(pycurl.URL, 'https://httpbin.org/post')
# post_data = {'amrish': 'topa'}
# postfields = urlencode(post_data)
c.setopt(pycurl.POSTFIELDS, urlencode({}))
# c.setopt(c.UPLOAD, 1)
# data = '{"json":true}'
# READDATA requires an IO-like object; a string is not accepted
# encode() is necessary for Python 3
# buffer = BytesIO(data.encode('utf-8'))
# c.setopt(c.READDATA, buffer)

c.perform()
c.close()