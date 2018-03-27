# polyrun.py



def main():
    arg_parser = argparse.ArgumentParser(description='A Utility to convert Natural Language to SQL query')
    arg_parser.add_argument('-d', '--database', help='Path to SQL dump file', required=True)
    arg_parser.add_argument('-l', '--language', help='Path to language configuration file', required=True)
    arg_parser.add_argument('-i', '--sentence', help='Input sentence to parse', required=True)
    arg_parser.add_argument('-j', '--json_output', help='path to JSON output file', default=None)
    arg_parser.add_argument('-t', '--thesaurus', help='path to thesaurus file', default=None)
    arg_parser.add_argument('-s', '--stopwords', help='path to stopwords file', default=None)

    args = arg_parser.parse_args()

    ln2sql = Ln2sql(
        database_path=args.database,
        language_path=args.language,
        json_output_path=args.json_output,
        thesaurus_path=args.thesaurus,
        stopwords_path=args.stopwords,
    ).get_query(args.sentence) 
    
    
    
def get_args():
    """
    Parse the CLI arguments
    """
    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                            description=PROG_DESCRIPTION)

    parser.add_argument("mastervol", help="Master Volume Name",
                        metavar="MASTERVOL")
    parser.add_argument("slave",
                        help="Slave, HOSTNAME or root@HOSTNAME::SLAVEVOL "
                        "or user@HOSTNAME::SLAVEVOL",
                        metavar="SLAVE")
    parser.add_argument("--force", help="Force",
                        action="store_true")
    parser.add_argument("--no-color", help="No Terminal Colors",
                        action="store_true")

    return parser.parse_args() 

def _parse_args(args):
    parser = argparse.ArgumentParser()

    if any([arg == '--version' for arg in args]):
        return argparse.Namespace(version=True)

    parser.add_argument('script', help='Script to run')
    parser.add_argument('target', nargs='?', default='build', help='Target object to build; defaults to \'build\'')

    parser.add_argument('--version', action='store_true', help='Print version info and exit')
    parser.add_argument('--clear', action='store_true', help='Clear output directory')
    parser.add_argument('--clear-cache', action='store_true', help='Clear cache before compiling')

    parser.add_argument('--threads', '-t', type=int, help='Set thread count; defaults to cores*2')
    parser.add_argument('--no-threading', '-nt', action='store_true', help='Disable multithreaded compiling')

    # TODO: Make target '*' instead of '?' so multiple targets could be ran from the same command

    return parser.parse_args(args) 


def parse_min_args():
    # Parse arguments
    parser = ArgumentParser()
    parser.add_argument('--expname', '-e', dest='exp', metavar='e', type=str,
                        default='dev', help='Name of the experiment to be run.')
    parser.add_argument('--n_steps', dest='n_steps', type=int,
                        default=300, help='Number of updates to be performed.')
    parser.add_argument('--n_test_iter', dest='n_test_iter', type=int,
                        default=100, help='Number of episodes to test on.')
    parser.add_argument('--update_frequency', dest='update_frequency', type=int,
                        default=1500, help='Number of steps before updating parameters.')
    parser.add_argument('--max_path_length', dest='max_path_length', type=int,
                        default=15000, help='Max length for a trajectory/episode.')
    parser.add_argument('--print_interval', dest='print_interval', type=int,
                        default=1000, help='Number of steps between each print summary.')
    parser.add_argument('--record', dest='record', type=bool,
                        default=False, help='Whether to record videos at test time.')
    parser.add_argument('--render', dest='render', type=bool,
                        default=False, help='Whether to render display at train time.')
    return parser.parse_args() 


def parse_args():
    parser = argparse.ArgumentParser(description='Backup Block Device')
    parser.add_argument('--backup', required=True,
                        help='Path to backup file or device')
    parser.add_argument('--manifest', required=True,
                        help='manifest file')
    parser.add_argument('--cbt', required=False,
                        help='change block tracking info')
    parser.add_argument('--backend', required=False, default='raw',
                        choices=['raw'], help='backend driver')
    parser.add_argument('--storage', required=False, default='local',
                        choices=['local'], help='storage driver')
    parser.add_argument('--location', required=True, help='storage path')
    parser.add_argument('--driver', required=False, default='sqlite',
                        choices=['osdk', 'sqlite'], help='manifest driver')
    return parser.parse_args() 

