from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

from tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30)
        Activity.objects.create(user=users[1], type='Cycling', duration=45)
        Activity.objects.create(user=users[2], type='Swimming', duration=60)
        Activity.objects.create(user=users[3], type='Yoga', duration=20)

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio workout for all heroes')
        Workout.objects.create(name='Strength Training', description='Strength workout for all heroes')

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=90)
        Leaderboard.objects.create(user=users[2], points=95)
        Leaderboard.objects.create(user=users[3], points=85)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
