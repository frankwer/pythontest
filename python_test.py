import psycopg2
from jinja2 import Template, Environment

t = Template("Hello {{ something }}!")
t.render(something="World")

HTML = """
<html>
<head>
<title>{{ title }}</title>
</head>
<body>
Hello.
</body>
</html>
"""


print("NAME: ", __name__)

def print_html_doc():
    print(Environment().from_string(HTML).render(title='En test Frank Johansen'))

if __name__ == '__main__':
    print_html_doc()



