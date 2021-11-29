from datetime import datetime
from time_pkg.get_time_pkg.get_time_module import  get_time
#from time_pkg. import get_time

def print_time_pretty(unixtime):
  formatted_time=datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')
  print(formatted_time)

def main():
  unixtime = get_time()
  print_time_pretty(unixtime)


if __name__=='__main__':
  main()
