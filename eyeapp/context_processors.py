from .models import Category, Icon, Service, Doctor, Gallery, Mizhi, Equipment, Blog, Review, ManagementTeam


def category_context(request):
    categories = Category.objects.all()
    nav_service = Service.objects.filter(service_nav=True)
    featured_services = Service.objects.filter(featured=True)
    services = Service.objects.all()
    doctors = Doctor.objects.all()
    gallery = Gallery.objects.all()
    mizhi = Mizhi.objects.all()
    equipment = Equipment.objects.all()
    featured_blogs_all = Blog.objects.filter(featured=True)
    reviews_all = Review.objects.all()[:2]
    team_members_all = ManagementTeam.objects.all()
    return {'categories_all': categories, 'nav_service': nav_service, 'services_all': services, 'featured_services': featured_services, 'doctors_all': doctors, 'gallery_all': gallery, 'mizhi_all': mizhi, 'equipment_all': equipment, 'featured_blogs_all': featured_blogs_all, 'reviews_all': reviews_all, 'team_members_all': team_members_all, }
