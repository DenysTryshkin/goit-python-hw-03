from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        date_today = datetime.today().date()
        days_difference = date_today - date
        return days_difference.days
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD")
        return 0
        
    
print(get_days_from_today("2025-10-09"))