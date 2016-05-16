#!/usr/bin/env python
import socket


# Pring your machine name and IP Address
# Import socket module
# use the gethostname() function
def print_hostname():
  my_hostname=socket.gethostname()
  
if __name__ == '__main__':
  print_hostname()
