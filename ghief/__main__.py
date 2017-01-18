
import argparse
import logging
import sys
import yaml
from backup_git_repository import backup_git_repository


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', help='Specify repository list file', default='./ghieflist.yaml')
    parser.add_argument('-v', '--verbose', action='store_true', help='Be chatty')
    parser.add_argument('--debug', action='store_true', help='Enabled debugging output')
    args = parser.parse_args()
    # configure logging
    logger = logging.getLogger()
    if args.debug:
        logger.setLevel(logging.DEBUG)
    elif args.verbose:
        logger.setLevel(logging.INFO)
    # do action
    if args.list:
        try:
            with open(args.list, 'r') as stream:
                list_file = yaml.load(stream)
                repositories = list_file.get('repositories')
                for repository in repositories:
                    source = repository.get('source')
                    target = repository.get('target')
                    backup_git_repository(source, target)
        except IOError as e:
            logging.error('Could not read repository list file: ' + e.strerror)
            return 1
    else:
        logging.error("No action defined. Exiting.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
