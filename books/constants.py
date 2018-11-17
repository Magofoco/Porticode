# EXCHANGE
FREE = "FR"
PAID = "PA"
BARTER = "BA"
EXCHANGE_CHOICES = (
    (FREE, 'Free'),
    (PAID, 'Paid'),
    (BARTER, 'Barter')
)

# CONDITIONS
NEW = 'NE'
USED_NEW = 'UN'
USED_GOOD = 'UG'
USED_JADED = 'UJ'
CONDITION_CHOICES = (
    (NEW, 'New - Never Used'),
    (USED_NEW, 'Used but seems still new'),
    (USED_GOOD, 'Used but in good conditions'),
    (USED_JADED, 'Used and you can see it')
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
