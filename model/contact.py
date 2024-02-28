from sys import maxsize


class Contact:
    def __init__(self, first_name=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None, email1=None,
                 email2=None, email3=None, homepage=None, birthday_day=None, birthday_month=None, birthday_year=None,
                 anniversary_day=None, anniversary_month=None, anniversary_year=None, address2=None, phone2=None,
                 notes=None, all_phones_from_homepage=None, all_emails_from_homepage=None, id=None):
        self.first_name = first_name
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.first_name)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id or self.first_name is None
                or other.first_name is None or self.lastname is None or other.lastname is None)
                and self.first_name == other.first_name and self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


class SelectContactByName:
    def __init__(self, first_name, lastname):
        self.first_name = first_name
        self.lastname = lastname
