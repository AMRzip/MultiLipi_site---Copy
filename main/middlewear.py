from django.utils.deprecation import MiddlewareMixin

class ReferralLinkCookieMiddleware(MiddlewareMixin):
    """
    If a ?via=XYZ is present in the URL, store it as a 'referral_link' cookie.
    """
    COOKIE_NAME = 'referral_link'
    COOKIE_MAX_AGE = 60 * 60 * 24 * 1  # 30 days

    def process_response(self, request, response):
        ref_code = request.GET.get('via')
        if ref_code:
            response.set_cookie(
                self.COOKIE_NAME,
                ref_code,
                max_age=self.COOKIE_MAX_AGE,
                httponly=False,
                samesite='Lax',
                secure=False,
                domain='.multilipi.com'
            )
        return response
