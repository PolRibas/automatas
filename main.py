import argparse
from src.project_one.modulo import main as main1
from src.project_two.modulo import main as main2


def parse_args():
    parser = argparse.ArgumentParser(description='Choice your action.')
    parser.add_argument('accion', choices=['main1', 'main2'], help='Action to perform')
    
    return parser.parse_args()

def main():
    args = parse_args()
    
    if args.accion == 'main2':
        main2()
    elif args.accion == 'main1':
        main1()
    else:
        print("Invalid action")

if __name__ == "__main__":
    main()
