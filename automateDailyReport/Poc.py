import pycurl
from io import BytesIO
try:
    from urllib.parse import urlencode
except:
    from urllib import urlencode

headers = {}
def header_function(header_line):
    # HTTP standard specifies that headers are encoded in iso-8859-1.
    # On Python 2, decoding step can be skipped.
    # On Python 3, decoding step is required.
    header_line = header_line.decode('iso-8859-1')

    # Header lines include the first status line (HTTP/1.x ...).
    # We are going to ignore all lines that don't have a colon in them.
    # This will botch headers that are split on multiple lines...
    if ':' not in header_line:
        return

    # Break the header line into header name and value.
    name, value = header_line.split(':', 1)

    # Remove whitespace that may be present.
    # Header lines include the trailing newline, and there may be whitespace
    # around the colon.
    name = name.strip()
    value = value.strip()

    # Header names are case insensitive.
    # Lowercase name here.
    name = name.lower()

    # Now we can actually record the header name and value.
    # Note: this only works when headers are not duplicated, see below.
    headers[name] = value


buffer = BytesIO()

c = pycurl.Curl()

c.setopt(c.URL, "http://trringology.com/users/login")

post_data = {
                'field': "1919191919",
                'password': "marketing",
            }

post_fields = urlencode(post_data)
c.setopt(c.POSTFIELDS, post_fields)
c.setopt(c.HEADERFUNCTION, header_function)
c.perform()
print(headers.get("set-cookie"))
print(c.getinfo(c.RESPONSE_CODE))
c.close()