from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext as _

from cinema.forms import EmployeeInline, ClientInline
from cinema.models import Client, EmployeeProfile, Editor, Director, Admin


class EmployeeAdmin(BaseUserAdmin):
    list_display = ('username', 'full_name', 'employee_profile')
    list_filter = ('employee_profile__cinema__name',)
    inlines = (EmployeeInline,)
    group = None
    GROUP_NAMES = {
        'EDITORS': 'Redaktorzy',
        'DIRECTORS': 'Kierownictwo',
        'ADMINS': 'Administratorzy'
    }

    def full_name(self, object):
        """
            Return full name of given user
        :param object: Client model
        :return: full name
        """
        return '{0} {1}'.format(object.first_name, object.last_name)

    full_name.short_description = _('Imię i nazwisko')

    def save_model(self, request, obj, form, change):
        """
            Set default settings to given role and save
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        obj.is_staff = True
        super(EmployeeAdmin, self).save_model(request, obj, form, change)

    def get_fieldsets(self, request, obj=None):
        """
            Restrict fieldsets depending on user group
        :param request:
        :param obj:
        :return:
        """
        fieldsets = super(EmployeeAdmin, self).get_fieldsets(request, obj)
        current_user = request.user
        user_groups = [v.name for v in current_user.groups.all()]
        if EmployeeAdmin.GROUP_NAMES['ADMINS'] not in user_groups and not current_user.is_superuser:
            fieldsets = filter(lambda fieldset: fieldset[0] != _('Permissions'), fieldsets)
        fieldsets = filter(lambda fieldset: fieldset[0] != _('Important dates'), fieldsets)
        return fieldsets


class EditorAdmin(EmployeeAdmin):
    group = EmployeeAdmin.GROUP_NAMES['EDITORS']
    inlines = ()

    def save_model(self, request, obj, form, change):
        """
            Set default settings to given role and save
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        obj.save()
        group = Group.objects.get(name=self.group)
        group.user_set.add(obj.pk)
        obj.is_staff = True
        if not hasattr(obj, 'employee_profile'):
            EmployeeProfile.objects.create(user=obj, cinema=request.user.employee_profile.cinema)
        super(EditorAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
            Return only employees assigned to specific cinema
        :param request:
        :return: filtered QuerySet
        """
        queryset = super(EditorAdmin, self).get_queryset(request)
        current_user = request.user
        user_groups = [v.name for v in current_user.groups.all()]
        if EmployeeAdmin.GROUP_NAMES['ADMINS'] not in user_groups and not current_user.is_superuser:
            queryset = queryset.prefetch_related().filter(
                is_staff=True,
                groups__name__in=[EmployeeAdmin.GROUP_NAMES['EDITORS']],
                employee_profile__cinema=current_user.employee_profile.cinema
            )
        else:
            queryset = queryset.prefetch_related().filter(
                is_staff=True,
                groups__name__in=[EmployeeAdmin.GROUP_NAMES['EDITORS']]
            )
        return queryset


class DirectorAdmin(EmployeeAdmin):
    group = EmployeeAdmin.GROUP_NAMES['DIRECTORS']
    inlines = (EmployeeInline,)

    def save_model(self, request, obj, form, change):
        """
            Set default settings to given role and save
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        obj.save()
        group = Group.objects.get(name=self.group)
        group.user_set.add(obj.pk)
        obj.is_staff = True
        super(DirectorAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
            Return only employees assigned to specific cinema
        :param request:
        :return: filtered QuerySet
        """
        queryset = super(DirectorAdmin, self).get_queryset(request)
        queryset = queryset.prefetch_related().filter(
            is_staff=True,
            groups__name__in=[self.group]
        )
        return queryset


class AdminAdmin(EmployeeAdmin):
    group = EmployeeAdmin.GROUP_NAMES['ADMINS']
    inlines = (EmployeeInline,)

    def save_model(self, request, obj, form, change):
        """
            Set default settings to given role and save
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        obj.save()
        group = Group.objects.get(name=self.group)
        group.user_set.add(obj.pk)
        obj.is_staff = True
        super(AdminAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
            Return only employees assigned to specific cinema
        :param request:
        :return: filtered QuerySet
        """
        queryset = super(AdminAdmin, self).get_queryset(request)
        queryset = queryset.prefetch_related().filter(
            is_staff=True,
            groups__name__in=[self.group]
        )
        return queryset


class ClientAdmin(admin.ModelAdmin):
    """
        User and cinema Client model with user profile form
    """
    inlines = (ClientInline,)
    list_display = ('username', 'full_name', 'email')
    fields = ('username', 'first_name', 'last_name', 'email')

    def full_name(self, object):
        """
            Return full name of given user
        :param object: Client model
        :return: full name
        """
        return '{0} {1}'.format(object.first_name, object.last_name)

    full_name.short_description = _('Imię i nazwisko')

    def get_queryset(self, request):
        """
            Return only client - is_staff flag not set
        :param request:
        :return: filtered QuerySet
        """
        queryset = super(ClientAdmin, self).get_queryset(request)
        return queryset.filter(is_staff=False)


admin.site.unregister(User)
admin.site.register(User, EmployeeAdmin)
admin.site.register(Editor, EditorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Client, ClientAdmin)
