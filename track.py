import argparse
import database

from enum import Enum

class Action(Enum):
    track = 'track'
    stat = 'stat'

def init_parser():
    """
    parser initialization
    """
    parser = argparse.ArgumentParser(description="Трекинг времени на разные проекты")
    
    parser.add_argument('action', help='Возможные действия [track - для регистрации времени работы (указывается в параметре --min), stat - для вывода статистики за период (указывается в параметре --days)]', choices=list(Action), type=Action)
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
    
    args = parser.parse_args()
    if  args.action == Action.track:
        
        database.add_record_to_database(args.project, args.min)
    else:        
        statistic_data = database.get_statistic_data_from_database(args.project, args.days)
        show_statistic_data(statistic_data)