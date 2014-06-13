from annoying.decorators import render_to

@render_to('securities/index.html')
def index(request):
	return {}