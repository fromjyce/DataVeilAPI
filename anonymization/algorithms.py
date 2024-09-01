import random
import re
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

def apply_masking(data, pattern, replacement_func):
    return re.sub(pattern, replacement_func, data)

def generalize_data(data):
    data = re.sub(r'\d{4}-\d{2}-\d{2}', r'****-**-**', data)
    data = re.sub(r'\d+', r'##', data)
    return data

def randomize_data(data):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=len(data)))

def perturb_data(data):
    def perturb_date(date_str):
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            delta = timedelta(days=random.randint(-30, 30))
            new_date = date_obj + delta
            return new_date.strftime('%Y-%m-%d')
        except ValueError:
            return date_str
        
    def perturb_number(num_str):
        try:
            number = int(num_str)
            delta = random.randint(-10, 10)
            new_number = max(0, number + delta)
            return str(new_number)
        except ValueError:
            return num_str

    if re.match(r'\d{4}-\d{2}-\d{2}', data):
        return perturb_date(data)
    elif re.match(r'\d+', data):
        return perturb_number(data)
    else:
        return 'Unsupported data format'
    
def pseudonymize_data(data):
    if re.match(r'[^@]+@[^@]+\.[^@]+', data):
            return fake.email()
    elif re.match(r'^[A-Za-z\s]+$', data):
        return fake.name()
    elif re.match(r'\+?\d[\d\-\(\) ]{4,}\d', data):
        return fake.phone_number()
    elif re.match(r'\d{16}', data):
        return fake.credit_card_number()
    elif re.match(r'\d{12}', data):
        return fake.aadhaar_number()
    elif re.match(r'[A-Z]{2}\d+', data):
        return fake.license_plate()
    else:
        return fake.sentence()
    
def swap_data(data):
    data_list = data.split()
    random.shuffle(data_list)
    return ' '.join(data_list)

def generate_synthetic_data(data):
    length = len(data)
    
    if re.match(r'[^@]+@[^@]+\.[^@]+', data):
        return fake.email()[:length] + fake.email()[length:].replace('@', '')
    elif re.match(r'^\+?\d[\d\-\(\) ]{4,}\d$', data):
        return ''.join(random.choices('0123456789+-()', k=length))
    elif re.match(r'\d{4} \d{4} \d{4} \d{4}', data):
        return ''.join(random.choices('0123456789 ', k=length)).strip()
    else:
        return ' '.join(fake.words(nb=length // 5 + 1))[:length]


def anonymize_data(data, technique):
    if not data:
        return 'No data provided'

    if technique == 'masking':
        data = apply_masking(data, r'^[A-Za-z\s]+$', lambda m: m.group(0)[0] + '*'*(len(m.group(0)) - 2) + m.group(0)[-1])
        data = apply_masking(data, r'[^@]+@[^@]+\.[^@]+', lambda m: m.group(0)[0] + '*'*(len(m.group(0).split('@')[0]) - 1) + '@' + m.group(0).split('@')[1])
        data = apply_masking(data, r'\+?\d[\d\-\(\) ]{4,}\d', lambda m: m.group(0)[:len(m.group(0)) - 4] + '*'*4)
        data = apply_masking(data, r'\d{4} \d{4} \d{4} \d{4}', lambda m: '**** **** **** ' + m.group(0)[-4:])
        data = apply_masking(data, r'\d+', lambda m: '*'*(len(m.group(0)) - 4) + m.group(0)[-4:])
        data = apply_masking(data, r'\d{12}', lambda m: '**** **** **** ' + m.group(0)[-4:])
        data = apply_masking(data, r'[A-Z]{2}\d+', lambda m: '*'*(len(m.group(0)) - 4) + m.group(0)[-4:])
        data = apply_masking(data, r'[A-Z]{3}\d+', lambda m: '***' + m.group(0)[-7:])
        data = apply_masking(data, r'[A-Z]{5}\d{4}[A-Z]', lambda m: '*'*5 + m.group(0)[-4:])
        data = apply_masking(data, r'[A-Z]\d{7}', lambda m: '*'*3 + m.group(0)[-7:])
        return data

    elif technique == 'generalization':
        return generalize_data(data)

    elif technique == 'randomization':
        return randomize_data(data)

    elif technique == 'perturbation':
        return perturb_data(data)

    elif technique == 'pseudonymization':
        return pseudonymize_data(data)

    elif technique == 'data_swapping':
        return swap_data(data)

    elif technique == 'synthetic_data':
        return generate_synthetic_data(data)

    else:
        return data