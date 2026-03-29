import os
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()
os.environ["PATH"] = os.path.dirname(driver_path) + os.pathsep + os.environ.get("PATH", "")
