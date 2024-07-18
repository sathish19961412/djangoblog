from typing import Any
from blogapp.models import Post
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    
      help="This commands inserts post data"
      
      def handle(self, *args: Any, **options: Any):
          
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

        for title,content,img_url in zip(titles,contents,img_urls):
            Post.objects.create(title=title,content=content,img_url=img_url)
            
        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
