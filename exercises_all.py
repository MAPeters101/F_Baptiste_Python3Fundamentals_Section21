'''
Question 1
Write a function that, given an epoch timestamp, returns a datetime object set to the beginning of that month (so midnight of the first day of the month).

For example, given the epoch time 12345678.9, your function should return:

datetime.datetime(1970, 5, 1, 0, 0)
Question 2
Write a function that returns the difference in hours between two dates provided as Python standard ISO formatted strings, rounded to the nearest hour. For simplicity, assume that these dates do not contain fractional seconds.

For example, given these two dates:

2001-01-01T13:50:23
and

2001-06-12T14:23:50
your result should be 3889 hours.

Question 3
Write a function that can be used to consistently format datetime objects into strings with some default format, but allows the caller to override the default format.

For example, the default format could be mm/dd/yyyy hh:mm:ss am/pm, but your function allows itself to be called with some argument that can override that format.
'''