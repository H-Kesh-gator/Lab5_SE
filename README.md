# Lab5_SE
1. Which issues were the easiest to fix, and which were the hardest? Why?
2. Did the static analysis tools report any false positives? If so, describe one example.
3. How would you integrate static analysis tools into your actual software development
workflow? Consider continuous integration (CI) or local development practices.
4. What tangible improvements did you observe in the code quality, readability, or potential
robustness after applying the fixes?

# Answers

1) The issues which were the formatting issues as these were just grammar issues could fix them easliy.
2) Yes pylint detected the global variable "stock_data = {}" however this was not a problem.
3) I would run the tools (Pylint, Bandit, Flake8) locally before committing code and integrate them into your Continuous Integration  pipeline to automatically check quality before allowing a code merge.
4) The code now looks more readible , more understandable and more pleasing to look at, quality has increased as indicated by the pylint score , it is more robust after fixing the mutable default argument was handled , the evaluation error was handled and no bare except clause was handled using KeyError this makes it less unpredictable and more easier to work with.