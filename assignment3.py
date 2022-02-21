import argparse
import pandas as pd
import re


def image_format_func(text):
    image_format = ['.jpg', '.png', '.gif']
    for i in image_format:
        if bool(re.search(i, text)) == True:
            return True
    return False


def browser_func(text):
    if bool(re.search('Firefox', text)) == True:
        return 'Mozilla Firefox'
    elif bool(re.search('Chrome', text)) == True:
        return 'Google Chrome'
    elif bool(re.search('Explorer', text)) == True:
        return 'Internet Explorer'
    elif bool(re.search('Safari', text)) == True:
        return 'Safari'


def hour_func(text):
    return list(text.split())[-1][:2]


# PART II
df = pd.read_csv('ENTER YOUR CSV FILE NAME HERE')


# PART III
df['image_bool'] = df['path_to_file'].apply(lambda x: image_format_func(x), axis=1)
percentage = (len(df[df['image_bool'] == True]) / len(df['image_bool'])) * 100
print('Image requests account for {} of all requests'.format(percentage))

# PART IV
df['browser'] = df['browser'].apply(lambda x: browser_func(x), axis=1)
print('Browsers with maximum occurences: ', df['browser'].mode().to_list())

# PART VI
df['hour'] = df['datetime_accessed'].apply(lambda x: hour_func(x), axis=1)
hour_dict = df['hour'].value_counts().to_dict()

for hour, hits in hour_dict.items():
    print('Hour {} has {} hits'.format(hour, hits))