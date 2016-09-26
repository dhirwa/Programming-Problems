import datetime as dt

def time_difference(s,e):
    start_dt = dt.datetime.strptime(s, '%H:%M')
    end_dt = dt.datetime.strptime(e, '%H:%M')
    return end_dt - start_dt

start = "09:35"
end = "11:00"

print time_difference(start,end)

start = "10:45"
end = "11:00"

print time_difference(start,end)
 
