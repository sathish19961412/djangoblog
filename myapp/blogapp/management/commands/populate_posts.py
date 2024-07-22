from typing import Any
from blogapp.models import Post,Category
from django.core.management.base import BaseCommand
import random
class Command(BaseCommand):
    
      help="This commands inserts post data"
      
      def handle(self, *args: Any, **options: Any):
        #Delete Existing data
        Post.objects.all().delete()
        titles=[
        'The Future of AI',
        'Climate Change Solutions',
        'Remote Work Trends',
        'Renewable Enery Innovations',
        ]

        contents=[
            'Exploring the intersection of art,design,and technology in the digital age',
            'Exploring the intersection of art,design,and technology in the digital age is 25',
            'Exploring the intersection of art,design,and technology in the digital age is 28',
            'Exploring the intersection of art,design,and technology in the digital age is 30',
        ]

        img_urls=[
            "https://via.placeholder.com/300",
            "https://via.placeholder.com/300",
            "https://via.placeholder.com/300",
            "https://via.placeholder.com/300",
        ]

        categories=Category.objects.all()
        
        for title,content,img_url in zip(titles,contents,img_urls):
            category=random.choice(categories)
            Post.objects.create(title=title,content=content,img_url=img_url,category=category)
            
        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
