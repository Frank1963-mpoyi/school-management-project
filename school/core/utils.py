import random
import string
from datetime import datetime
from string import ascii_uppercase, digits, ascii_lowercase

from django.utils.text import slugify


def get_timenow():
    today = datetime.now().strftime('%y%m%d-%H%M%S').split('-')
    date = today[0]
    now = today[1]
    return date, now


def randcode_gen():
    date, now = get_timenow()
    randcode = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode = (''.join(randcode))
    new_code = f"HOPE{date}{randcode}{now}TCLINIC"
    return new_code

def appointment_randcode_gen():
    date, now = get_timenow()
    randcode = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode = (''.join(randcode))
    new_code = f"HOPE{date}{randcode}{now}APPOINT"
    return new_code


def patient_randcode_gen():
    date, now = get_timenow()
    randcode = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode = (''.join(randcode))
    new_code = f"HOPE{date}{randcode}{now}PATIENT"
    return new_code


def doctor_randcode_gen():
    date, now = get_timenow()
    randcode = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode = (''.join(randcode))
    new_code = f"HOPE{date}{randcode}{now}DOCTOR"
    return new_code


def latest_news_randcode_gen():
    date, now = get_timenow()
    randcode = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode = (''.join(randcode))
    new_code = f"HOPE{date}{randcode}{now}LATESTNEWS"
    return new_code


def get_in_touch_randcode_gen():
    date, now = get_timenow()
    randcode = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode = (''.join(randcode))
    new_code = f"HOPE{date}{randcode}{now}GET"
    return new_code

def comment_randcode_gen():
    date, now = get_timenow()
    randcode = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode = (''.join(randcode))
    new_code = f"HOPE{date}{randcode}{now}COMMENT"
    return new_code

def address_randcode_gen():
    date, now = get_timenow()
    randcode = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode = (''.join(randcode))
    new_code = f"HOPE{date}{randcode}{now}ADDRESS"
    return new_code

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range (size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug