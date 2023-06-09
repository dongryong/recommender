from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model


from cfehome import utils as cfehome_utils 

User = get_user_model()

class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("count", nargs='?', default=10, type=int)
        parser.add_argument("--show-total",action='store_true', default=False)


    def handle(self, *args, **options):
        count = options.get('count')
        show_total = options.get('show_total')
        profiles = cfehome_utils.get_fake_profiles(count=count)
        
        new_users = []
        for profile in profiles:
            new_users.append(
                User(**profile)
            )
            # User.objects.create(**profile)

        user_bulk = User.objects.bulk_create(new_users, ignore_conflicts=True)    
        print(f'new users are created {len(user_bulk)}')
        if show_total:
            print(f"Total users: {User.objects.count()}")
        # print(f'Hello there are {User.objects.count()}')
