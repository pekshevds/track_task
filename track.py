import argparse
import json
import datetime, time
import itertools

parser = argparse.ArgumentParser(description="Трекинг времени на разные проекты")
database_file = 'database.json'

def init_parser():
    """
    parser initialization
    """

    parser.add_argument('action', help='Возможные действия [track - для регистрации времени работы (указывается в параметре --min), stat - для вывода статистики за период (указывается в параметре --days)]')
    parser.add_argument('--project', help='Имя проекта')
    parser.add_argument('--min', type=int, help='Рабочее время потраченое на проект, в минутах', default=15)
    parser.add_argument('--days', type=int, help='Период вывода статистики, в днях (N-последних дней)', default=5)


def add_record_to_database(project_name='', min_count=0):
    """
    it writes data in a file
    """

    with open(database_file, mode='+a', encoding="utf-8") as file:
        
        record = {
            'date': datetime.date.today().strftime('%Y-%m-%d'),
            'project_name': project_name,
            'min_count': min_count,
        }
        
        file.write(json.dumps(record) + "\n")        


def get_statistic_data_from_database(project_name='', days_count=0):
    """
    it collects statistical data per different periods
    """

    statistic_data = []    
    with open(database_file, mode='r', encoding="utf-8") as file:
        
        all_records_of_database = [json.loads(line) for line in file.readlines()]
        filtered_records = itertools.filterfalse(lambda record: record['project_name'] != project_name, all_records_of_database)
        sorted_records = sorted(filtered_records, key=lambda record: record['date'], reverse=True)
        groupted_records = itertools.groupby(sorted_records, key=lambda record: record['date'])
        
        for group, group_records in itertools.islice(groupted_records, days_count):
            
            formated_date = group.split('-')[1] + '.' + group.split('-')[2]
            
            seconds = sum([record['min_count'] for record in group_records]) * 60
            formated_time = time.strftime("%Hh %Mm", time.gmtime(seconds))

            statistic_data.append({'date': formated_date, 'time': formated_time})

    return statistic_data


def show_statistic_data(statistic_data = []):
    """
    it shows statistical data
    """

    for record in statistic_data:
        print(f"{record.get('date', '')} {record.get('time', '')}")


if __name__ == "__main__":
    
    init_parser()

    args = vars(parser.parse_args())
    if args['action'] == 'track':
        
        add_record_to_database(args['project'], args['min'])
    elif args['action'] == 'stat':
        
        statistic_data = get_statistic_data_from_database(args['project'], args['days'])
        show_statistic_data(statistic_data)
    else:
        print('Не верное значение аргумента action')
        parser.print_help()