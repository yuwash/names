from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random
import datetime


__title__ = 'names'
__version__ = '0.3.0.post1'
__author__ = 'Trey Hunner'
__license__ = 'MIT'


full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'first:male': full_path('dist.male.first'),
    'first:female': full_path('dist.female.first'),
    'last': full_path('dist.all.last'),
}


def get_name(filename):
    selected = random.random() * 90
    with open(filename) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            if float(cummulative) > selected:
                return name
    return ""  # Return empty string if file is empty


def get_first_name(gender=None):
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return "{0} {1}".format(get_first_name(gender), get_last_name())


def get_username(gender=None):
    formats = (
        '{f}{l}',
        '{f}_{l}',
        '{f}{yy:02d}',
        '{f}{yyyy:04d}',
        '{f}{l}{yy:02d}',
        '{f}{l}{yyyy:04d}',
    )
    # in decreasing order of probability
    choicei = int(2 * len(formats) * random.expovariate(2))
    try:
        choice = formats[choicei]
    except IndexError:  # in rare cases too big
        choice = formats[-1]
    first = get_first_name(gender).lower()
    last = get_last_name().lower()
    thisyyyy = datetime.date.today().year
    yyyy = random.randint(thisyyyy - 80, thisyyyy - 10)
    yy = yyyy % 100
    uniquefy = (
        '{}',
        'iam{}',
        'real{}',
        '{}_',
        '{}1',
    )
    choicei = int(len(uniquefy) * random.expovariate(2))
    try:
        uniquefy = uniquefy[choicei]
    except IndexError:  # in rare cases too big
        uniquefy = uniquefy[-1]
    return uniquefy.format(
        choice.format(f=first, l=last, yyyy=yyyy, yy=yy))
