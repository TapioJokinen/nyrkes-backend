from django.contrib import admin

from nyrkes.admin.organization import OrganizationAdmin
from nyrkes.admin.organizationmember import OrganizationMemberAdmin
from nyrkes.admin.user import UserAdmin
from nyrkes.models import Organization, OrganizationMember, User

admin.site.register(User, UserAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationMember, OrganizationMemberAdmin)
