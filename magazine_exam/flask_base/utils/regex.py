import re

REGEX_PRIMERA_MAYUSCULA = re.compile(r'^[A-Z][a-z0-9_-]{0,}$')
REGEX_CORREO_VALIDO = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')