from django.core.exceptions import PermissionDenied


class GroupRequiredMixin:
    required_groups = []

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            raise PermissionDenied
        if not request.user.groups:
            raise PermissionDenied
        user_group_names = [g.name for g in request.user.groups.all()]
        result = set(user_group_names).intersection(self.required_groups)
        if self.required_groups and not result:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)
