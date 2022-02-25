# Imagine you’re creating a footer with pagination to browse through the several pages of a given website.

# Let’s assume the usage of the following variables for the effect:

# - current_page
# - total_pages
# - boundaries: how many pages we want to link in the beginning, or end (meaning, how many pages starting at page 1 and how many leading up to the last page, inclusive)
# - around: how many pages we want to link before and after the current page, exclusive.

# For pages with no direct link we should use one set of three points (...) per set of pages hidden.

# Examples:
# 1) current_page = 4;
# total_pages = 5; 
# boundaries = 1; 
# around = 0 
# Expected result: 1 ... 4 5

# 2) current_page = 4;
# total_pages = 10; 
# boundaries = 2; 
# around = 2 
# Expectedresult: 123456...910


from itertools import chain

def pagination(current_page, total_pages, boundaries, around):
  print(f"{current_page=}  {total_pages=}  {boundaries=}  {around=}")

  total_pages+=1
  
  start_boundaries = boundaries
  end_boundaries = total_pages - boundaries

  # if not (0<(start_boundaries-end_boundaries)<total_pages):
  if not (0<=boundaries<total_pages):
    raise BaseException("make sure that boundaries are less than or equal to half of the total_pages")

  if not (0<current_page<total_pages):
    raise BaseException("make sure that 0 < current_page < total_pages")

  if (before_around:=current_page-around)<0:
    before_around = 0
  if (after_around:=current_page+around)>total_pages:
    after_around = total_pages
  
  last_page = 0

  for page_no in set(chain(
    range(1,start_boundaries+1), 
    range(before_around, after_around+1), 
    range(end_boundaries, total_pages))):

    if (page_no-last_page)>1:
      print('...', end=' ')
    print(f"{page_no}", end=' ')

    last_page = page_no
  
  else:
    if total_pages-1 not in (page_no, current_page):
      print('...', end='')
      
  print('\n')

pagination(current_page=4, total_pages=5, boundaries=1, around=0)
pagination(current_page=4, total_pages=10, boundaries=2, around=2)
pagination(current_page=2, total_pages=10, boundaries=3, around=0)
pagination(current_page=6, total_pages=12, boundaries=3, around=2)
pagination(current_page=2, total_pages=12, boundaries=0, around=0)
pagination(current_page=1, total_pages=12, boundaries=0, around=0)
pagination(current_page=12, total_pages=12, boundaries=0, around=0)
# pagination(current_page=13, total_pages=12, boundaries=0, around=0)
# pagination(current_page=0, total_pages=12, boundaries=0, around=0)
pagination(current_page=4, total_pages=12, boundaries=6, around=0)