from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostpostApp.models import ghostpost
from ghostpostApp.forms import submit_ghostpost
from django.db.models import F, Count


def index_view(request):
    if request.method == "POST":
        if 'Boast' in request.POST:
            return render(request, "index.html", {"ghostpost": ghostpost.objects.all().order_by('-ghostpost_choice')})
        if 'Roast' in request.POST:
            return render(request, "index.html", {"ghostpost": ghostpost.objects.all().order_by('ghostpost_choice')})
        if 'Date' in request.POST:
            return render(request, "index.html", {"ghostpost": ghostpost.objects.all().order_by('creation_date')})
        if 'Score' in request.POST:
            return render(request, "index.html", {"ghostpost": ghostpost.objects.annotate(
                vote_score=F('upvotes') - F('downvotes')).order_by("-vote_score")})

    return render(request, "index.html", {"ghostpost": ghostpost.objects.all()})


def add_ghostpost(request):
    if request.method == "POST":
        form = submit_ghostpost(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = submit_ghostpost()
    return render(request, "add_ghostpost.html", {"form": form})


def upvote_view(request, post_id):
    if request.method == "POST":
        post = ghostpost.objects.get(pk=post_id)
        post.upvotes += 1
        post.save()
        return HttpResponseRedirect(reverse("homepage"))


def downvote_view(request, post_id):
    if request.method == "POST":
        post = ghostpost.objects.get(pk=post_id)
        post.downvotes += 1
        post.save()
        return HttpResponseRedirect(reverse("homepage"))
