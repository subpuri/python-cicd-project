import argparse
from app.system.cpu import cpu_usage
from app.system.memory import memory_usage
from app.system.disk import disk_usage


def main():
    parser = argparse.ArgumentParser(
        description="InfraOps Automator CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    # CPU usage command
    subparsers.add_parser("cpu", help="Get CPU usage information")

    # Memory usage command
    subparsers.add_parser("memory", help="Get Memory usage information")

    # Disk usage command
    disk_parser = subparsers.add_parser("disk", help="Get Disk usage information")
    disk_parser.add_argument(
        "--path", default="/", help="Path to check disk usage for"
    )

    args = parser.parse_args()

    if args.command == "cpu":
        data = cpu_usage()
        print("CPU Usage Information:")
        for key, value in data.items():
            print(f"{key}: {value}")
        return

    if args.command == "memory":
        data = memory_usage()
        print("Memory Usage Information:")
        for key, value in data.items():
            print(f"{key}: {value}")
        return

    if args.command == "disk":
        data = disk_usage(args.path)
        print("Disk Usage Information:")
        for key, value in data.items():
            print(f"{key}: {value}")
        return
    else:
        parser.print_help()


if __name__ == "__main__":
    main()