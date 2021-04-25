How to run test:
1. Open the code in pycharm
2. Ensure you have python 3.8 installed
3. Check compatibility of chromedriver and your chrome, if not compatible please download your chrome compatible chromedriver version
4. Go to "File>Settings...>Project:>Project Interpreter" and check venv present selected & detected( not invalid). If not, please create new virtual env from there itself.
5. Activate virtualenv "venv" by hiting following cmd in terminal.
                   venv\Scripts\activate
6. Then hit command "pip install -r requirements.txt" to install all required plugins if not exists already.
7. There are 2 ways to run test:
	1. You can either edit configuration and add Pytest from python test and give test file path. Give additional arguments as "-vv -s --html=report.html". Also, check Interpreter option is configured properly.
	2. From terminal, You can hit below command by going inside the directory where test file exists.
					pytest -vv -s test.py --html=report.html
