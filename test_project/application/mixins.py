from django.contrib.auth.mixins import AccessMixin

from application.constants import ADVANCED_AND_MORE, PRO


class SubscribtionLimitationMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if self.subscription_limitation == ADVANCED_AND_MORE:
            user = request.user
            if user.is_free_subscription:
                return self.handle_no_permission()
        if self.subscription_limitation == PRO:
            user = request.user
            if user.is_free_subscription or user.is_advanced_subscription:
                return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
