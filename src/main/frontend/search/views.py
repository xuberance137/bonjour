from django.shortcuts import render
from django.http import HttpResponse
from .scraper.run_search import run_crawler, read_json

def search_form(request):
	return render(request, 'search/enter_search.html', {})

def search(request):
	if 'q' in request.GET:
		if request.GET['q'] == '':
			message = 'No searching keyword entered'
		else:
			search_string = request.GET['q']
			message = 'You searched for: %s' % request.GET['q']
	else:
		message = 'Form is not submitted properly.'

	jsonFileName = 'results.json'
	
	print('Running Crawler')
	run_crawler(search_string, jsonFileName)
	print('Reading JSON')
	link, desc, snip = read_json(jsonFileName)

	response = HttpResponse()

	response.write("<p>    </p>")
	response.write("<p>    </p>")

	for index in range(len(link)): 
		print(link[index], desc[index])

		response.write("<a href=" + link[index] + ">" + desc[index] + "</a>")
		response.write("<p>" + snip[index] + "</p>")
		response.write("<p>    </p>")

	return response
