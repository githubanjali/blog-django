# -*- coding: utf-8 -*-
#from django.core.context_processors import csrf
#from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
# Create your views here.
from .forms import PostForm
from .models import Post

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		#print form.cleaned_data.get("title")
		instance.save()
		messages.success(request, "Sucessfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Successfully Created")
	context = {
		"form": form,
	}
	return render(request,"post_form.html",context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request,"post_detail.html", context)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item </a>saved", extra_tags='html_safe')
		#messages.success(request, "New Saved")
		#messages.success(request, "Whatever Saved")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request,"post_form.html",context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
		"title": "List"
	}
	return render(request,"post_list.html",context)

def post_delete(request):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Succeddfully")
	return redirect("posts:list")