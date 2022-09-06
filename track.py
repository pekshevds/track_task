import argparse
import json
import datetime, time
import itertools

parser = argparse.ArgumentParser(description="Трекинг времени на разные проекты")

def init_parser():
    """
    parser initialization
    """

    parser.add_argument('action', help='Возможные действия [track - для регистрации времени работы (указывается в параметре --min), stat - для вывода статистики за период (указывается в параметре --days)]')
    parser.add_argument('--project', help='Имя проекта')
    parser.add_argument('--min', type=int, help='Рабочее время потраченое на проект, в минутах', default=15)
    parser.add_argument('--days', type=int, help='Период вывода статистики, в днях (N-последних дней)', default=5)


def add_to_stat(project_name='', min_count=0):
    """
    it writes data in a file
    """

    with open('database.json', mode='+a', encoding="utf-8") as file:
        record = {
            'date': datetime.date.today().strftime('%Y-%m-%d'),
            'project_name': project_name,
            'min_count': min_count,
        }
        file.write(json.dumps(record) + "\n")        


def show_stat(project_name='', days_count=0):
    """
    it shows statistical data per different periods
    """
        
    with open('database.json', mode='r', encoding="utf-8") as file:
        #Фильтруем
        items = itertools.filterfalse(lambda item: item['project_name'] != project_name, [json.loads(line) for line in file.readlines()])
        #Сортируем
        items = sorted(items, key=lambda item: item['date'], reverse=True)
        #Группируем, берем первые N и выводим 
        for date, group_items in itertools.islice(itertools.groupby(items, key=lambda item: item['date']), days_count):
            
            str1 = date.split('-')[1] + '.' + date.split('-')[2]

            seconds = sum([item['min_count'] for item in group_items]) * 60
            str2 = time.strftime("%Hh %Mm", time.gmtime(seconds))

            print(f"{str1} {str2}")


if __name__ == "__main__":
    
    #Инициализируем парсер
    init_parser()

    args = vars(parser.parse_args())
    if args['action'] == 'track':
        
        add_to_stat(args['project'], args['min'])
    elif args['action'] == 'stat':
        
        show_stat(args['project'], args['days'])
    else:
        print('Не верное значение аргумента action')
        parser.print_help()