import re
import hashlib
from bs4 import BeautifulSoup


class ValidateInputs:
    def str_strip_tags_sc(self,a):
        soup  = BeautifulSoup(a,"html.parser")
        str   = soup.get_text()
        clean = re.sub('\W+','', str )
        return clean.strip()

    def str_strip_title_tags_sc(self,a):
        soup  = BeautifulSoup(a,"html.parser")
        str   = soup.get_text()
        clean = re.sub('\W+','', str )
        return clean.strip().title()

    def strong_password(self,a):
        password = hashlib.md5(a.encode('utf-8')).hexdigest()
        return password
