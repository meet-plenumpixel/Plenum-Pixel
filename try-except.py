def bare_except():
  while True:
    try:
      exit()
      s = input("input a number: ")
      x = int(s)
      break
    except Exception: # it would throw KeyboardInterrupt error when Ctrl + C press
      # except: it would not throw KeyboardInterrupt when Ctrl + C press
      print("error")

bare_except()