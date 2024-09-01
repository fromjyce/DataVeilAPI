import random
import re
from faker import Faker

fake = Faker()

def anonymize_data(data, technique):
    if not data:
        return 'No data provided'
    is_email = re.match(r'^[^@]+@[^@]+\.[^@]+$', data)
    is_phone = re.match(r'^\+?(\d[\d\-\(\) ]{4,}\d)$', data)
    is_aadhaar = re.match(r'^\d{4}\s\d{4}\s\d{4}$', data)
    is_pan = re.match(r'^[A-Z]{5}\d{4}[A-Z]$', data)
    is_passport = re.match(r'^[A-Z]{1}[0-9]{7}$', data)
    is_name = re.match(r'^[A-Za-z\s]+$', data)
    is_date = re.match(r'\d{4}-\d{2}-\d{2}', data)
    is_cc_number = re.match(r'\d{4}-\d{4}-\d{4}-\d{4}', data)
    is_bank_account = re.match(r'\d{9,18}', data)

    if is_email:
        if technique == 'masking':
            return re.sub(r'([a-zA-Z0-9._%+-])[^@]+(@[a-zA-Z0-9.-]+)', r'\1***\2', data)
        elif technique == 'pseudonymization':
            return fake.email()
        else:
            return data
    
    elif is_phone:
        if technique == 'masking':
            return re.sub(r'\d(?=\d{4})', '*', data)
        elif technique == 'randomization':
            return ''.join(random.choices(data, k=len(data)))
        else:
            return data
    
    elif is_aadhaar:
        if technique == 'masking':
            return '**** **** ****'
        elif technique == 'pseudonymization':
            return fake.ssn()
        else:
            return data
    
    elif is_pan:
        if technique == 'masking':
            return '*****' + data[-4:]
        elif technique == 'pseudonymization':
            return fake.ssn()
        else:
            return data
    
    elif is_passport:
        if technique == 'masking':
            return '****' + data[-4:]
        elif technique == 'pseudonymization':
            return fake.ssn()
        else:
            return data
    
    elif is_name:
        if technique == 'masking':
            return data[0] + '*' * (len(data) - 1)
        elif technique == 'pseudonymization':
            return fake.name()
        else:
            return data
    
    elif is_date:
        if technique == 'generalization':
            return data[:4] + '-**-**'
        elif technique == 'perturbation':
            return (data[:4] + '-' + str(int(data[5:7]) + random.randint(-1, 1)).zfill(2) + '-' + str(int(data[8:]) + random.randint(-1, 1)).zfill(2))
        else:
            return data
    
    elif is_cc_number:
        if technique == 'masking':
            return '****-****-****-' + data[-4:]
        elif technique == 'randomization':
            return ''.join(random.choices('0123456789-', k=len(data)))
        else:
            return data
    
    elif is_bank_account:
        if technique == 'masking':
            return '****' + data[-4:]
        elif technique == 'randomization':
            return ''.join(random.choices('0123456789', k=len(data)))
        else:
            return data

    else:
        return 'Data type not recognized or technique not applicable'