from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/')
    image_500 = models.ImageField(upload_to='category_images_500/', blank=True)
    image_800 = models.ImageField(upload_to='category_images_800/', blank=True)
    image_1080 = models.ImageField(
        upload_to='category_images_1080/', blank=True)
    image_1920 = models.ImageField(
        upload_to='category_images_1920/', blank=True)

    def save(self, *args, **kwargs):
        # Save the original image first
        if not self.id:  # Only process if it's a new object
            super(Category, self).save(*args, **kwargs)

        # Create different image resolutions
        resolutions = {
            '500': self.image_500,
            '800': self.image_800,
            '1080': self.image_1080,
            '1920': self.image_1920
        }

        try:
            with Image.open(self.image) as img:
                for res, image_field in resolutions.items():
                    output_size = self._calculate_new_dimensions(img, int(res))
                    # Updated line
                    img.thumbnail(output_size, Image.Resampling.LANCZOS)
                    temp_thumb = BytesIO()
                    img.save(temp_thumb, img.format, quality=90)
                    temp_thumb.seek(0)
                    image_field.save(
                        f'{self.name}_{res}.{img.format.lower()}',
                        ContentFile(temp_thumb.read()),
                        save=False
                    )
                    temp_thumb.close()
        except IOError:
            raise ValidationError("Error processing image")

        # Save the object again with all the images
        super(Category, self).save(*args, **kwargs)

    def _calculate_new_dimensions(self, image, base_width):
        w_percent = (base_width / float(image.size[0]))
        h_size = int((float(image.size[1]) * float(w_percent)))
        return (base_width, h_size)

    def __str__(self):
        return self.name


class CategoryDetails(models.Model):
    category = models.OneToOneField(
        Category, related_name='details', on_delete=models.CASCADE)
    category_content = models.TextField()

    def __str__(self):
        return f"{self.category.name}'s Details"


class Icon(models.Model):
    category = models.ForeignKey(
        Category, related_name='icons', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    image = models.FileField(upload_to='category_icons/')

    def __str__(self):
        return self.name


class Service(models.Model):
    icon = models.ForeignKey(
        Icon, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/')
    image_500 = models.ImageField(upload_to='service_images_500/', blank=True)
    image_800 = models.ImageField(upload_to='service_images_800/', blank=True)
    image_1080 = models.ImageField(
        upload_to='service_images_1080/', blank=True)
    image_1920 = models.ImageField(
        upload_to='service_images_1920/', blank=True)
    featured = models.BooleanField(default=False)
    service_nav = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Save the original image first
        if not self.id:  # Only process if it's a new object
            super(Service, self).save(*args, **kwargs)

        # Create different image resolutions
        resolutions = {
            '500': self.image_500,
            '800': self.image_800,
            '1080': self.image_1080,
            '1920': self.image_1920
        }

        try:
            with Image.open(self.image) as img:
                for res, image_field in resolutions.items():
                    output_size = self._calculate_new_dimensions(img, int(res))
                    img.thumbnail(output_size, Image.Resampling.LANCZOS)
                    temp_thumb = BytesIO()
                    img.save(temp_thumb, img.format, quality=100)
                    temp_thumb.seek(0)
                    image_field.save(
                        f'{self.name}_{res}.{img.format.lower()}',
                        ContentFile(temp_thumb.read()),
                        save=False
                    )
                    temp_thumb.close()
        except IOError:
            raise ValidationError("Error processing image")

        # Save the object again with all the images
        super(Service, self).save(*args, **kwargs)

    def _calculate_new_dimensions(self, image, base_width):
        w_percent = (base_width / float(image.size[0]))
        h_size = int((float(image.size[1]) * float(w_percent)))
        return (base_width, h_size)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='doctor_images/')
    image_500 = models.ImageField(upload_to='doctor_images_500/', blank=True)
    image_800 = models.ImageField(upload_to='doctor_images_800/', blank=True)
    image_1018 = models.ImageField(upload_to='doctor_images_1018/', blank=True)

    def save(self, *args, **kwargs):
        # Save the original image first
        if not self.id:  # Only process if it's a new object
            super(Doctor, self).save(*args, **kwargs)

        # Create different image resolutions
        resolutions = {
            '500': self.image_500,
            '800': self.image_800,
            '1018': self.image_1018
        }

        try:
            with Image.open(self.image) as img:
                for res, image_field in resolutions.items():
                    output_size = self._calculate_new_dimensions(img, int(res))
                    img.thumbnail(output_size, Image.Resampling.LANCZOS)
                    temp_thumb = BytesIO()
                    img.save(temp_thumb, img.format, quality=100)
                    temp_thumb.seek(0)
                    image_field.save(
                        f'{self.name}_{res}.{img.format.lower()}',
                        ContentFile(temp_thumb.read()),
                        save=False
                    )
                    temp_thumb.close()
        except IOError:
            raise ValidationError("Error processing image")

        # Save the object again with all the images
        super(Doctor, self).save(*args, **kwargs)

    def _calculate_new_dimensions(self, image, base_width):
        w_percent = (base_width / float(image.size[0]))
        h_size = int((float(image.size[1]) * float(w_percent)))
        return (base_width, h_size)

    def __str__(self):
        return self.name


class DoctorDetails(models.Model):
    doctor = models.OneToOneField(
        Doctor, related_name='details', on_delete=models.CASCADE)
    main_description = models.TextField(blank=True)
    about_description = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    expertise = models.TextField(blank=True)
    practice = models.TextField(blank=True)

    def __str__(self):
        return f"{self.doctor.name}'s Details"


class ServiceDetails(models.Model):
    service = models.OneToOneField(
        Service, related_name='details', on_delete=models.CASCADE)
    service_content = models.TextField()

    def __str__(self):
        return f"{self.service.name}'s Details"


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')
    image_500 = models.ImageField(upload_to='gallery_images_500/', blank=True)
    image_800 = models.ImageField(upload_to='gallery_images_800/', blank=True)
    image_1080 = models.ImageField(
        upload_to='gallery_images_1080/', blank=True)
    image_1920 = models.ImageField(
        upload_to='gallery_images_1920/', blank=True)

    def save(self, *args, **kwargs):
        # Save the original image first
        if not self.id:  # Only process if it's a new object
            super(Gallery, self).save(*args, **kwargs)

        # Create different image resolutions
        resolutions = {
            '500': self.image_500,
            '800': self.image_800,
            '1080': self.image_1080,
            '1920': self.image_1920
        }

        try:
            with Image.open(self.image) as img:
                for res, image_field in resolutions.items():
                    output_size = self._calculate_new_dimensions(img, int(res))
                    # Updated line
                    img.thumbnail(output_size, Image.Resampling.LANCZOS)
                    temp_thumb = BytesIO()
                    img.save(temp_thumb, img.format, quality=90)
                    temp_thumb.seek(0)
                    image_field.save(
                        f'{self.name}_{res}.{img.format.lower()}',
                        ContentFile(temp_thumb.read()),
                        save=False
                    )
                    temp_thumb.close()
        except IOError:
            raise ValidationError("Error processing image")

        # Save the object again with all the images
        super(Gallery, self).save(*args, **kwargs)

    def _calculate_new_dimensions(self, image, base_width):
        w_percent = (base_width / float(image.size[0]))
        h_size = int((float(image.size[1]) * float(w_percent)))
        return (base_width, h_size)

    def __str__(self):
        return self.name


class Mizhi(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='mizhi_images/')
    image_500 = models.ImageField(upload_to='mizhi_images_500/', blank=True)
    image_800 = models.ImageField(upload_to='mizhi_images_800/', blank=True)
    image_1080 = models.ImageField(upload_to='mizhi_images_1080/', blank=True)
    image_1920 = models.ImageField(upload_to='mizhi_images_1920/', blank=True)

    def save(self, *args, **kwargs):
        # Save the original image first
        if not self.id:  # Only process if it's a new object
            super(Mizhi, self).save(*args, **kwargs)

        # Create different image resolutions
        resolutions = {
            '500': self.image_500,
            '800': self.image_800,
            '1080': self.image_1080,
            '1920': self.image_1920
        }

        try:
            with Image.open(self.image) as img:
                for res, image_field in resolutions.items():
                    output_size = self._calculate_new_dimensions(img, int(res))
                    # Updated line
                    img.thumbnail(output_size, Image.Resampling.LANCZOS)
                    temp_thumb = BytesIO()
                    img.save(temp_thumb, img.format, quality=90)
                    temp_thumb.seek(0)
                    image_field.save(
                        f'{self.name}_{res}.{img.format.lower()}',
                        ContentFile(temp_thumb.read()),
                        save=False
                    )
                    temp_thumb.close()
        except IOError:
            raise ValidationError("Error processing image")

        # Save the object again with all the images
        super(Mizhi, self).save(*args, **kwargs)

    def _calculate_new_dimensions(self, image, base_width):
        w_percent = (base_width / float(image.size[0]))
        h_size = int((float(image.size[1]) * float(w_percent)))
        return (base_width, h_size)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='equipment_images/')
    image_500 = models.ImageField(
        upload_to='equipment_images_500/', blank=True)
    image_800 = models.ImageField(
        upload_to='equipment_images_800/', blank=True)
    image_1080 = models.ImageField(
        upload_to='equipment_images_1080/', blank=True)
    image_1920 = models.ImageField(
        upload_to='equipment_images_1920/', blank=True)

    def save(self, *args, **kwargs):
        # Save the original image first
        if not self.id:  # Only process if it's a new object
            super(Equipment, self).save(*args, **kwargs)

        # Create different image resolutions
        resolutions = {
            '500': self.image_500,
            '800': self.image_800,
            '1080': self.image_1080,
            '1920': self.image_1920
        }

        try:
            with Image.open(self.image) as img:
                for res, image_field in resolutions.items():
                    output_size = self._calculate_new_dimensions(img, int(res))
                    # Updated line
                    img.thumbnail(output_size, Image.Resampling.LANCZOS)
                    temp_thumb = BytesIO()
                    img.save(temp_thumb, img.format, quality=90)
                    temp_thumb.seek(0)
                    image_field.save(
                        f'{self.name}_{res}.{img.format.lower()}',
                        ContentFile(temp_thumb.read()),
                        save=False
                    )
                    temp_thumb.close()
        except IOError:
            raise ValidationError("Error processing image")

        # Save the object again with all the images
        super(Equipment, self).save(*args, **kwargs)

    def _calculate_new_dimensions(self, image, base_width):
        w_percent = (base_width / float(image.size[0]))
        h_size = int((float(image.size[1]) * float(w_percent)))
        return (base_width, h_size)

    def __str__(self):
        return self.name

#  blogs


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    content = models.TextField()

    # Add any other fields or methods as needed

    def __str__(self):
        return self.title


class Review(models.Model):
    patient_name = models.CharField(max_length=255)
    content = models.TextField()
    what_doctor = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Review_images/')

    def __str__(self):
        return self.patient_name


class ManagementTeam(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='management_team_images/')
    image_500 = models.ImageField(
        upload_to='management_team_images_500/', blank=True)
    image_800 = models.ImageField(
        upload_to='management_team_images_800/', blank=True)
    image_1018 = models.ImageField(
        upload_to='management_team_images_1018/', blank=True)

    def save(self, *args, **kwargs):
        # Save the original image first
        if not self.id:  # Only process if it's a new object
            super(ManagementTeam, self).save(*args, **kwargs)

        # Create different image resolutions
        resolutions = {
            '500': self.image_500,
            '800': self.image_800,
            '1018': self.image_1018
        }

        try:
            with Image.open(self.image) as img:
                for res, image_field in resolutions.items():
                    output_size = self._calculate_new_dimensions(img, int(res))
                    img.thumbnail(output_size, Image.Resampling.LANCZOS)
                    temp_thumb = BytesIO()
                    img.save(temp_thumb, img.format, quality=100)
                    temp_thumb.seek(0)
                    image_field.save(
                        f'{self.name}_{res}.{img.format.lower()}',
                        ContentFile(temp_thumb.read()),
                        save=False
                    )
                    temp_thumb.close()
        except IOError:
            raise ValidationError("Error processing image")

        # Save the object again with all the images
        super(ManagementTeam, self).save(*args, **kwargs)

    def _calculate_new_dimensions(self, image, base_width):
        w_percent = (base_width / float(image.size[0]))
        h_size = int((float(image.size[1]) * float(w_percent)))
        return (base_width, h_size)

    def __str__(self):
        return self.name


class ManagementTeamDetails(models.Model):
    team_member = models.OneToOneField(
        ManagementTeam, related_name='details', on_delete=models.CASCADE)
    main_description = models.TextField(blank=True)
    about_description = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    expertise = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True)

    def __str__(self):
        return f"{self.team_member.name}'s Details"
