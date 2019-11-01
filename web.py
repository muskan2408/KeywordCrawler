import pdfkit

config = pdfkit.configuration(wkhtmltopdf = "C:\\Program Files\\wkhtmltox\\bin\\wkhtmltopdf.exe")


pdfkit.from_url("https://google.com/url?q=https://www.edureka.co/blog/what-is-machine-learning/&sa=U&ved=2ahUKEwiJ5ceB38nlAhWMRo8KHdGdDJcQFjAeegQIAxAB&usg=AOvVaw37DygoIurLv6LFBuk8km1x","ml.pdf",configuration=config)