from django.shortcuts import render
from trydjango.apps.yrb.dbpostgres import dictfetchall
from .filters import PriceFilter, FilteredListView
import os
import psycopg2
import subprocess
from django_heroku import dj_database_url
database_url = os.getenv(
    'DATABASE_URL'
)

connection = psycopg2.connect(database_url)

# Create your views here.

def super_category_view(request):
 
   with connection.cursor() as cursor:
    cursor.execute("SELECT row_number() over (order by club) as index, club from yrb_club order by club;")
   
    all_clubs=dictfetchall(cursor)
    context={ 'all_clubs' : all_clubs
               }
    return render(request, 'supercategory.html', context)

  
def category_view(request, club):
    
 
   with connection.cursor() as cursor:
    cursor.execute("SELECT row_number() over (order by cat) as index, initcap(cat) as cat  from yrb_category order by cat;")
    
    all_categories=dictfetchall(cursor)
    context={ 'all_categories' : all_categories,
              'club': club
               }
    return render(request, 'category.html', context)


class BookView(FilteredListView):
  
  filterset_class = PriceFilter
  template_name='booklist.html'  
  paginate_by = 10
  def get_context_data(self,**kwargs):
    context= super().get_context_data(**kwargs)
    
    
   
    with connection.cursor() as cursor:
      cursor.execute("SELECT z.index from (SELECT row_number() over (order by club) as index, club from yrb_club) as z where z.club=%s;",[self.kwargs.get('club')])
      clubindex=dictfetchall(cursor)
      cursor.execute("SELECT initcap(cat) as cat  from yrb_category order by cat;")
      all_categories=dictfetchall(cursor)
      context['index']=clubindex
      context['all_categories']=all_categories
      context['club']=self.kwargs.get('club')
      context['cat']=self.kwargs.get('cat')
      return context

def book_detail_view(request,OfferID):
  
 
     with connection.cursor() as cursor:
     
      cursor.execute("SELECT yrb_offer.offerid, yrb_offer.title, yrb_offer.price, yrb_offer.club, yrb_offer.year, yrb_book.cat, yrb_book.language, yrb_book.weight  from yrb_offer, yrb_book where yrb_offer.title=yrb_book.title and yrb_offer.year=yrb_book.year and yrb_offer.OfferID=%s;", [OfferID])
      Book=dictfetchall(cursor)
      return render(request, 'book.html', {'book': Book})
    
 
    


    
  
