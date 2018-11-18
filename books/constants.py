# EXCHANGE
FREE = "FR"
PAID = "PA"
BARTER = "BA"
EXCHANGE_CHOICES = (
    (FREE, 'FREE'),
    (PAID, 'PAID'),
    (BARTER, 'BARTER')
)

# CONDITIONS
NEW = 'NE'
USED_NEW = 'UN'
USED_GOOD = 'UG'
USED_JADED = 'UJ'
CONDITION_CHOICES = (
    (NEW, 'NEW'),
    (USED_NEW, 'USED_NEW'),
    (USED_GOOD, 'USED_GOOD'),
    (USED_JADED, 'USED_JADED')
)

# STATUS
OPEN = 'OP'
PENDING = 'PE'
EXCHANGED = 'EX'
STATUS_CHOICES = (
    (OPEN, 'Open to trade'),
    (PENDING, 'Pending for approval'),
    (EXCHANGED, 'Exhanged already')
)

GENDER_CHOICES = (
    ('m', 'Masculine'),
    ('f', 'Feminine'),
    ('o', 'Other')
)

PREFERENCE_CHOICES = (
    ('Science fiction', 'Science fiction'),
    ('Romance', 'Romance'),
    ('Horror', 'Horror'),
    ('Travel', 'Travel'),
    ('Satire', 'Satire'),
    ('Religion', 'Religion'),
    ('History', 'History'),
    ('Science', 'Science'),
    ('Poetry', 'Poetry'),
    ('Encyclopedias', 'Encyclopedias'),
    ('Dictionaries', 'Dictionaries'),
    ('Comics', 'Comics'),
    ('Art', 'Art'),
    ('Cookbooks', 'Cookbooks'),
    ('Diaries', 'Diaries'),
    ('Journals', 'Journals'),
    ('Prayer', 'Prayer'),
    ('Series', 'Series'),
    ('Biographies', 'Biographies'),
    ('Fantasy', 'Fantasy'),
)
