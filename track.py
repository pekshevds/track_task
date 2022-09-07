import argparse
import database

def init_parser():
    """
    parser initialization
    """
    parser = argparse.ArgumentParser(description="Трекинг времени на разные проекты")

    parser.add_argument('action', help='Возможные действия [track - для регистрации времени работы (указывается в параметре --min), stat - для вывода статистики за период (указывается в параметре --days)]')
    parser.add_argument('--project', help='Имя проекта')
    parser.add_argument('--min', type=int, help='Рабочее время потраченое на проект, в минутах', default=15)
    parser.add_argument('--days', type=int, help='Период вывода статистики, в днях (N-последних дней)', default=5)
    return parser

def show_statistic_data(statistic_data = []):
    """
    it shows statistical data
    """

    for record in statistic_data:
        print(f"{record.get('date', '')} {record.get('time', '')}")


if __name__ == "__main__":
    
    parser = init_parser()

    args = vars(parser.parse_args())
    if args['action'] == 'track':
        
        database.add_record_to_database(args['project'], args['min'])
    elif args['action'] == 'stat':
        
        statistic_data = database.get_statistic_data_from_database(args['project'], args['days'])
        show_statistic_data(statistic_data)
    else:
        print('Не верное значение аргумента action')
        parser.print_help()