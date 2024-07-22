from typing import Any
from blogapp.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    
      help="This commands inserts post data"
      
      def handle(self, *args: Any, **options: Any):
        #Delete Existing data
        Category.objects.all().delete()
        
        categories=['Sports','Technology','Science','Art','Food']
        
        for category_name in categories:
            Category.objects.create(name=category_name)
            
        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
