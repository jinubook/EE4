# Python Bash EE4 make C++ Making
import sys;
try:
  u = open("ee4.make", "r")
  arr = u.readlines();
  sr = ""
  for ln in arr:
    sr += ln
  msys = sr.split(';')
  b = False
  try:
    # Linux Syntax, If You're Using Windows, Change It To Your Installation Directory
    d = open("/usr/local/bin/gcc", "r");
  except:
    b = True
  if b:
    print("GCC Path Does Not Exist. Change It If You're Using Windows.")
  else:
    d = [""]
    f = 0
    isout = False;
    outstr = ""
    for s in msys:
      # Python 3.9 Syntax, If You're Using Older Versions, Upgrade It
      try:
        f = s.removesuffix("MK ");
      except:
        try:
          outstr = s.removesuffix("OUT ");
          isout = True
        except:
          print("Parser Error: Undefined Syntax")
      d[f] = f
      f += 1
    print("Making C Code To ee4_gen.....")
    s = ""
    for a in d:
      s += " " + a
    if isout:
      os.system("gcc " + s + " -o " + outstr)
    else:
      os.system("gcc " + s);
    print("Made ee4_gen")
except:
  print("ee4.make Does Not Exists.")
