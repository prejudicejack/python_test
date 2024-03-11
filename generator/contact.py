from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys



try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def randomstring(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def randomstring_for_emails(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def randomstring_for_phones(prefix, maxlen):
    symbols = string.digits + "+" + "()" + "-"
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_month():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    return random.choice(months)


def random_day():
    return str(random.randint(1, 31))


def random_year():
    return str(random.randint(1940, 2060))


testdata = [Contact(first_name="", lastname="")] + [
    Contact(first_name=randomstring("f_name", 10),
            middlename=randomstring("m_name", 15),
            lastname=randomstring("l_name", 10),
            nickname=randomstring("n_name", 10),
            title=randomstring("title", 10),
            company=randomstring("company", 10),
            address=randomstring("address", 60),
            home_phone=randomstring_for_phones("h_phone", 15),
            mobile_phone=randomstring_for_phones("m_phone", 15),
            work_phone=randomstring_for_phones("w_phone", 15),
            fax=randomstring_for_phones("fax", 15),
            email1=randomstring_for_emails("email1", 30),
            email2=randomstring_for_emails("email2", 30),
            email3=randomstring_for_emails("email3", 30),
            homepage=randomstring("homepage", 25),
            birthday_day=random_day(),
            birthday_month=random_month(),
            birthday_year=random_year(),
            anniversary_day=random_day(),
            anniversary_month=random_month(),
            anniversary_year=random_year(),
            address2=randomstring("address2", 60),
            phone2=randomstring_for_phones("phone2", 15),
            notes=randomstring("notes", 100))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
