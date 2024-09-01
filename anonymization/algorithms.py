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
    segments = [segment.strip() for segment in re.split(r',\s*', data)]
    anonymized_segments = []
    for segment in segments:
        if technique == 'masking':
            anonymized_segments.append(
                apply_masking(segment, r'^[A-Za-z\s]+$', lambda m: m.group(0)[0] + '*'*(len(m.group(0)) - 2) + m.group(0)[-1]) or
                apply_masking(segment, r'[^@]+@[^@]+\.[^@]+', lambda m: m.group(0)[0] + '*'*(len(m.group(0).split('@')[0]) - 1) + '@' + m.group(0).split('@')[1]) or
                apply_masking(segment, r'\+?\d[\d\-\(\) ]{4,}\d', lambda m: m.group(0)[:len(m.group(0)) - 4] + '*'*4) or
                apply_masking(segment, r'\d{4} \d{4} \d{4} \d{4}', lambda m: '**** **** **** ' + m.group(0)[-4:]) or
                apply_masking(segment, r'\d+', lambda m: '*'*(len(m.group(0)) - 4) + m.group(0)[-4:]) or
                apply_masking(segment, r'\d{12}', lambda m: '**** **** **** ' + m.group(0)[-4:]) or
                apply_masking(segment, r'[A-Z]{2}\d+', lambda m: '*'*(len(m.group(0)) - 4) + m.group(0)[-4:]) or
                apply_masking(segment, r'[A-Z]{3}\d+', lambda m: '***' + m.group(0)[-7:]) or
                apply_masking(segment, r'[A-Z]{5}\d{4}[A-Z]', lambda m: '*'*5 + m.group(0)[-4:]) or
                apply_masking(segment, r'[A-Z]\d{7}', lambda m: '*'*3 + m.group(0)[-7:])
            )
        elif technique == 'generalization':
            anonymized_segments.append(generalize_data(segment))
        elif technique == 'randomization':
            anonymized_segments.append(randomize_data(segment))
        elif technique == 'perturbation':
            anonymized_segments.append(perturb_data(segment))
        elif technique == 'pseudonymization':
            anonymized_segments.append(pseudonymize_data(segment))
        elif technique == 'data_swapping':
            anonymized_segments.append(swap_data(segment))
        elif technique == 'synthetic_data':
            anonymized_segments.append(generate_synthetic_data(segment))
        else:
            anonymized_segments.append(segment)
    
    return ', '.join(anonymized_segments)