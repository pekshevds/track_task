import argparse
import database

from enum import Enum

class Action(Enum):
    track = 'track'
    stat = 'stat'

    def __str__(self) -> str:
        return self.value

def init_parser():
    """
    parser initialization
    """
    parser = argparse.ArgumentParser(description="simple tracker for registration work time.")
    
    parser.add_argument('action', help="use 'track' - to registration work time, 'stat' - to view statistics", 
        choices=list(Action), type=Action)
    parser.add_argument('--project', type=str, help='project name')
    parser.add_argument('--min', type=int, help='spent time in minutes', default=15)
    parser.add_argument('--days', type=int, help='statistics period in days', default=5)
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