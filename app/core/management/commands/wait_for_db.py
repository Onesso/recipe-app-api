"""
command to wait for the database to be available
"""

from django.core.managent.base import BaseCommand

class Command(BaseCommand):
    """django command to wait of database"""
    def handle(self,*args,**options):
        pass
