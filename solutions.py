'''
Question 1
Write a function that, given an epoch timestamp, returns a datetime object set to the beginning of that month (so midnight of the first day of the month).

For example, given the epoch time 12345678.9, your function should return:

datetime.datetime(1970, 5, 1, 0, 0)
Solution
First we'll need to import the datetime object:

from datetime import datetime
We can easily convert an epoch timestamp to a datetime object by using the fromtimestamp method.

dt = datetime.fromtimestamp(12345678.9)
dt
datetime.datetime(1970, 5, 23, 14, 21, 18, 900000)
Next, we could replace the day, hour, minutes, and seconds with 1 or 0 as needed, or we could create a new datetime object just picking up the year and month from this one:

dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
datetime.datetime(1970, 5, 1, 0, 0)
or alternatively:

datetime(year=dt.year, month=dt.month, day=1)
datetime.datetime(1970, 5, 1, 0, 0)
Let's package this up into a function:

def month_start(epoch):
    dt = datetime.fromtimestamp(epoch)
    return datetime(year=dt.year, month=dt.month, day=1)
And let's call it:

month_start(12345678)
datetime.datetime(1970, 5, 1, 0, 0)
Let's test it out with the current (UTC) date as well:

import time
month_start(time.time())
datetime.datetime(2021, 2, 1, 0, 0)
Question 2
Write a function that returns the difference in hours between two dates provided as Python standard ISO formatted strings, rounded to the nearest hour. For simplicity, assume that these dates do not contain fractional seconds.

For example, given these two dates:

2001-01-01T13:50:23
and

2001-06-12T14:23:50
your result should be 3889 hours.

Solution
Let's start with two dates:

dt1 = datetime.fromisoformat('2001-01-01T13:50:23')
dt2 = datetime.fromisoformat('2001-06-12T14:23:50')
To find the difference between the two objects:

delta = dt2 - dt1
delta
datetime.timedelta(days=162, seconds=2007)
We can also get the total delta in seconds:

delta.total_seconds()
13998807.0
We want to round this to the closest hour.

An hour is 60 * 60 seconds:

seconds_in_hour = 60 * 60
So, we want to round to the closest multiple of seconds_in_hour.

There are probably many different approaches to this, here I'll explain how I thought about the problem.

First thing is we'll want to make the total number of seconds into an integer (we are assuming no fractional seconds).

delta_seconds = int(delta.total_seconds())
Next, we'll calculate the number of whole hours in that:

complete_hours = delta_seconds // seconds_in_hour
complete_hours
3888
And the remaining number of seconds is:

remaining_seconds = delta_seconds % seconds_in_hour
remaining_seconds
2007
The number of (fractional) hours in these seconds is:

remaining_seconds / seconds_in_hour
0.5575
We can simply round this number to determine whether we are closer to 0 or 1 for the farctional hour:

round(remaining_seconds / seconds_in_hour)
1
Let's package this up into a function:

def num_hours(dt1, dt2):
    seconds_in_hour = 60 * 60
    dt1 = datetime.fromisoformat(dt1)
    dt2 = datetime.fromisoformat(dt2)
    delta_seconds = int((dt2 - dt1).total_seconds())
    complete_hours = delta_seconds // seconds_in_hour
    remaining_seconds = delta_seconds % seconds_in_hour
    return complete_hours + round(remaining_seconds / seconds_in_hour)
And we can call this function with a few values:

num_hours('2001-01-01T13:50:23', '2001-06-12T14:23:50')
3889
num_hours('2001-01-01T00:00:00', '2001-01-01T01:00:00')
1
num_hours('2001-01-01T00:00:00', '2001-01-02T01:50:00')
26
Question 3
Write a function that can be used to consistently format datetime objects into strings with some default format, but allows the caller to override the default format.

For example, the default format could be mm/dd/yyyy hh:mm:ss am/pm, but your function allows itself to be called with some argument that can override that format.

Solution
Let's write the function definition first:

def dt_to_string(dt, fmt='%m/%d/%y %I:%M:%S%p'):
    pass
Notice how I set the default format string in the parameter definition itself - this way if the function is called without that argument, then the default will be used.

For these types of parameters though, I prefer to force the function to specify that fmt argument as a keyword argument, so I can force that this way:

def dt_to_string(dt, *, fmt='%m/%d/%y %I:%M:%S%p'):
    pass
Let's implement the function itself:

def dt_to_string(dt,  *, fmt='%m/%d/%y %I:%M:%S%p'):
    return dt.strftime(fmt)
dt_to_string(datetime(2020, 2, 1, 13, 34, 5))
'02/01/20 01:34:05PM'
But, we can always specify an alternate format if we want to:

dt_to_string(datetime(2020, 2, 1, 13, 34, 5), fmt='%B %d, %Y')
'February 01, 2020'
'''