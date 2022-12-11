from apps.migrations.migration import Migrations
from apps.processing.menu import Menu

class Main:

    def main(self):
        # Migrations().make_migrate()
        Menu().processing()

if __name__ == "__main__":
    Main().main()
