from hashlib import sha256
from django.conf import settings

class Token:
    
    def _generate_salt(self, pan):
        return (settings.SECRET_KEY + pan[:6]).encode("utf-8")

    def tokenize(self, pan):
        token = sha256(pan.encode("utf-8") + self._generate_salt(pan)).hexdigest()
        return token
