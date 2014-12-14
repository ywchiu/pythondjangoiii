from django.shortcuts import render

from .models import Join

from .forms import JoinForm
def home(request):
	form = JoinForm(request.POST or None)
	if form.is_valid():
	    new_join = form.save(commit=False)
	    email = form.cleaned_data['email']
	    new_join_old, created = Join.objects.get_or_create(email=email)
	context = {"form": form}
	template = "home.html"
	return render(request, template, context)


# def home(request):
# 	form = EmailForm(request.POST or None)
# 	if form.is_valid():
# 		email = form.cleaned_data['email']
# 		created = Join.objects.get_or_create(email=email)
# 	context = {"form": form}
# 	template = "home.html"
# 	return render(request, template, context)

# def home(request):
# 	print request.POST['email']
# 	form = EmailForm()
# 	context = {"form": form}
# 	template = "home.html"
# 	return render(request, template, context)

# def home2(request):
# 	form = EmailForm()
# 	context = {"form": form}
# 	template = "home.html"
# 	return render(request, template, context)
