from django.shortcuts import render
from calendar import HTMLCalendar
from datetime import date

def index(request, year=None, month=None):
    # If no year/month provided, use current date
    today = date.today()
    year = year or today.year
    month = month or today.month

    # Create the calendar HTML
    cal = HTMLCalendar().formatmonth(year, month)

    context = {
        "calendar": cal,
        "year": year,
        "month": month
    }
    return render(request, "base.html", context)
