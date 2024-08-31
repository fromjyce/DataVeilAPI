import random
from faker import Faker

fake = Faker()

def anonymize_data(data, technique):
    if technique == 'masking':
        return data[:5] + '*****'
    elif technique == 'generalization':
        return data[:5] + '...'
    elif technique == 'k-anonymity':
        return data[:len(data)//2] + '****'
    elif technique == 'randomization':
        return ''.join(random.choices(data, k=len(data)))
    elif technique == 'aggregation':
        return 'Aggregated Data'
    elif technique == 'perturbation':
        return ''.join([chr(ord(c) + random.randint(1, 5)) for c in data])
    elif technique == 'pseudonymization':
        return fake.name()
    elif technique == 'data_swapping':
        return 'Swapped Data'
    elif technique == 'synthetic_data':
        return fake.sentence()
    else:
        return data