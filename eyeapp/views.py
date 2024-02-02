from django.shortcuts import render, get_object_or_404
from .models import Category, Icon, Service, Doctor, DoctorDetails, ServiceDetails, CategoryDetails, Gallery, Mizhi, Equipment, Blog, Review, ManagementTeam, ManagementTeamDetails
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.template import loader


def home_view(request):
    gallery = Gallery.objects.all()
    mizhi = Mizhi.objects.all()
    equipment = Equipment.objects.all()
    context = {
        'gallery': gallery,
        'mizhi': mizhi,
        'equipment': equipment,
    }
    return render(request, 'home1.html', context)


def gallery_view(request):
    return render(request, 'gallery.html')


def categories(request):
    categories = Category.objects.all()
    return render(request, 'category.html')


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    details = CategoryDetails.objects.get(category=category)
    other_categories = Category.objects.exclude(slug=slug)
    context = {
        'category_details': details,
        'category': category,
        'other_categories': other_categories,
    }

    return render(request, 'category_detail.html', context)


def services(request):
    all_services = Service.objects.all().order_by('id')
    items_per_page = 8

    paginator = Paginator(all_services, items_per_page)
    page_number = request.GET.get('page')

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Render template to string
        html_content = render_to_string(
            'services_ajax.html', {'all_services': page})
        return JsonResponse({'html': html_content})

    return render(request, 'services.html', {'all_services': page})


def service_detail(request, slug):
    service = Service.objects.get(slug=slug)
    details = ServiceDetails.objects.get(service=service)
    other_services = Service.objects.exclude(slug=slug)
    paginator = Paginator(other_services, 8)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'service_details': details,
        'service': service,
        'other_services': page,
    }

    return render(request, 'service_detail.html', context)


def about(request):
    return render(request, 'about.html')


def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors, })


def doctor_detail(request, slug):
    doctor = Doctor.objects.get(slug=slug)
    details = DoctorDetails.objects.get(doctor=doctor)
    other_doctors = Doctor.objects.exclude(slug=slug)

    context = {
        'details': details,
        'doctor': doctor,
        'other_doctors': other_doctors,
    }

    return render(request, 'doctor_detail.html', context)


def subpage1(request):
    services_with_diagnostic_testing = Service.objects.filter(
        icon__name="Diagnostic Testing")
    context = {
        'services_with_diagnostic_testing': services_with_diagnostic_testing,
    }
    return render(request, 'diagnostic_testing.html', context)


def subpage2(request):
    services_with_eye_condition_treatments = Service.objects.filter(
        icon__name="Eye Condition treatments")
    context = {
        'services_with_eye_condition_treatments': services_with_eye_condition_treatments,
    }
    return render(request, 'eye_condition_treatments.html', context)


def blog_view(request):
    all_blogs = Blog.objects.all()
    featured_blogs = Blog.objects.filter(featured=True)
    eye_health_blogs = Blog.objects.filter(category__name='Eye Health')
    technology_blogs = Blog.objects.filter(category__name='Technology')
    context = {
        'all_blogs': all_blogs,
        'featured_blogs': featured_blogs,
        'eye_health_blogs': eye_health_blogs,
        'technology_blogs': technology_blogs,
    }

    return render(request, 'blog.html', context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    other_blogs = Blog.objects.exclude(slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog, 'other_blogs': other_blogs})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})


def contact(request):
    return render(request, 'contact.html')


def robots_txt(request):
    content = loader.render_to_string('robots.txt')
    return HttpResponse(content, content_type='text/plain')


def sitemap_xml(request):
    content = loader.render_to_string('sitemap.xml')
    return HttpResponse(content, content_type='application/xml')


def management_team(request):
    team_members = ManagementTeam.objects.all()
    return render(request, 'management_team.html', {'team_members': team_members, })


def management_team_detail(request, slug):
    team_member = ManagementTeam.objects.get(slug=slug)
    details = ManagementTeamDetails.objects.get(team_member=team_member)
    other_team_members = ManagementTeam.objects.exclude(slug=slug)

    context = {
        'details': details,
        'team_member': team_member,
        'other_team_members': other_team_members,
    }

    return render(request, 'management_team_detail.html', context)
