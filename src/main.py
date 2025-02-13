import sys, os; sys.path.append(os.path.join(os.path.dirname(__file__), '..')); import compile as ps

ps.fn("main", """
  pln("Hello from Pistud")

  // do "python compile.py src/main.py" to compile your PiStud file
""")
