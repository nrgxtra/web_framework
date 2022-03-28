from django.template import Library

from templates_advanced.profiles.models import UserProfile

register = Library()


@register.inclusion_tag('tags/profile_complete_notification.html', takes_context=True)
def profile_complete_notification(context):
    user_id = context.request.user.id
    profile = UserProfile.objects.get(pk=user_id)
    if profile:
        return {
            'is_complete': profile.is_complete,
        }
