import sys, os

cwd = os.getcwd()
sys.path.append(cwd)
#sys.path.append(cwd + '/_cms')

# Specify Interpreter
INTERP = os.path.expanduser("~/_venv/ssrd_v35/bin/python3")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0,'$HOME/_venv/ssrd_v35/bin')
sys.path.insert(0,'$HOME/_venv/ssrd_v35/lib/python3.5/site-packages/django')
sys.path.insert(0,'$HOME/_venv/ssrd_v35/lib/python3.5/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = '_cms.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


