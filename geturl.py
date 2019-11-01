# import requests, sys, webbrowser, bs4

# res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))
# try:
# 	res.raise_for_status()
# except HTTPError as e:
# 	if res.text:
# 		raise HTTPError('{} Error Message: {}'.format(str(e.message), res.text))
# 	else:
# 		raise e
# soup = bs4.BeautifulSoup(res.text, "html.parser")
# linkElements = soup.select('.r a')
# print(linkElements)


# # Windows
# chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
# webbrowser.register('chrome', 1,webbrowser.BackgroundBrowser(chrome_path))
# webbrowser.get('chrome').open_new_tab('https://google.com/search?q="quantum"')
# #webbrowser.get(chrome_path).open('https://google.com')
# linkToOpen = min(5, len(linkElements))
#for i in range(linkToOpen):

from flask import Flask,render_template,request,jsonify,redirect,url_for


import webbrowser
import sys
import pyperclip
import requests
import bs4
import pdfkit


app = Flask(__name__,  static_url_path='/static')

@app.route("/")
def home():
	return render_template("index.html")

@app.route('/search',methods=['POST'])
def start():
	if len(sys.argv) > 1:
		keyword = ' '.join(sys.argv[1:])
	else:
		# if no keyword is entered, the script would 
		# search for the keyword copied in the clipboard
		keyword = pyperclip.paste()
	key=request.form.get('search')
	res = requests.get(key)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text,'html.parser')
	links = soup.select('div#main > div > div > div > a')
	#print(links)
	# chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	# webbrowser.register('chrome', 1,webbrowser.BackgroundBrowser(chrome_path))
	# webbrowser.get('chrome').open_new_tab('https://google.com' + links[0].get('href'))
	List=[]
	tab_counts = min(30, len(links))
	for i in range(tab_counts):
		# chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
		# webbrowser.register('chrome', 1,webbrowser.BackgroundBrowser(chrome_path))
		# webbrowser.get('chrome').open_new_tab('https://google.com' + links[i].get('href'))
		List.append(links[i].get('href'))
	#session['my_list'] = List
	r=requests.post('http://127.0.0.1:5000/download',json={'Result':List})
    return r.text
	#return jsonify({'keyword':key,'Result':List})
	#return redirect(url_for('download'))

@app.route('/download' , method=['POST'])
def download():
	res=request.get_json()
	config = pdfkit.configuration(wkhtmltopdf = "C:\\Program Files\\wkhtmltox\\bin\\wkhtmltopdf.exe")
	pdfkit.from_url(res[Result][3],"yy.pdf",configuration=config)
	# i=0;
	# for item in session.pop('my_list', [])
	# 	pdfkit.from_url(item,"abc"+(i++)+".pdf",configuration=config)
	# endfor
	return "True"

#yahoo.in https://in.search.yahoo.com/search?p=
#bing.com https://www.bing.com/search?q=
#duckduckgo https://duckduckgo.com/?q=
#wiki.com http://www.wiki.com/results1.htm?cx=009420061493499222400%3Ae8sof1xaq-u&q=
#ask.com https://www.ask.com/web?q=
#AOI https://search.aol.com/aol/search?s_chn=prt_bon&q=
#archieve.org https://archive.org/search.php?query=

#start()

	
if __name__ == '__main__':
	app.run(debug = "true")
