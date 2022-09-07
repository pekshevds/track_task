import json
import datetime, time
import itertools

import config

def read_records_from_database():
    """
    it reads all data in a file
    """

    file = open(config.DATABASE_DATA_NAME, mode='r', encoding="utf-8")
    
    try:
        records = json.loads(file.read())
    except:
        records = []
    return records


def add_record_to_database(project_name='', min_count=0):
    """
    it writes data in a file
    """
    records = read_records_from_database()
                    
    record = {
        'date': datetime.date.today().strftime('%Y-%m-%d'),
        'project_name': project_name,
        'min_count': min_count,
    }
    records.append(record)

    with open(config.DATABASE_DATA_NAME, mode='w', encoding="utf-8") as file:    
        json.dump(records, file)


def prepare_data_to_generating_statistics(raw_data, filter):
    """
    it prepares raw data for statistics generating
    """

    filtered_data = itertools.filterfalse(lambda record: record['project_name'] != filter, raw_data)
    sorted_data = sorted(filtered_data, key=lambda record: record['date'], reverse=True)
    
    return itertools.groupby(sorted_data, key=lambda record: record['date'])

def get_statistic_data_from_database(project_name='', days_count=0):
    """
    it collects statistical data per different periods
    """

    statistic_data = []    
    
    all_records_of_database = read_records_from_database()        
    cleared_records = prepare_data_to_generating_statistics(all_records_of_database, project_name)
        
    for group, group_records in itertools.islice(cleared_records, days_count):
            
        formated_date = group.split('-')[1] + '.' + group.split('-')[2]
            
        seconds = sum([record['min_count'] for record in group_records]) * 60
        formated_time = time.strftime("%Hh %Mm", time.gmtime(seconds))

        statistic_data.append({'date': formated_date, 'time': formated_time})

    return statistic_data