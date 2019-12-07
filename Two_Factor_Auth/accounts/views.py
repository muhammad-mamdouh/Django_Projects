from rest_framework                     import status
from rest_framework.views               import APIView
from rest_framework.permissions         import IsAuthenticated
from rest_framework.response            import Response
from rest_framework.authtoken           import views as auth_views
from django_otp                         import devices_for_user
from django_otp.plugins.otp_totp.models import TOTPDevice


def get_user_totp_device(self, user, confirmed=None):
    devices = devices_for_user(user, confirmed=confirmed)
    for device in devices:
        if isinstance(device, TOTPDevice):
            return device


class TOTPCreateView(APIView):
    """
    Use this endpoint to set up a new TOTP device
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user   = request.user
        device = get_user_totp_device(self, user)
        if not device:
            device = user.totpdevice_set.create(confirmed=False)
        url = device.config_url
        return Response(url, status=status.HTTP_201_CREATED)


class TOTPVerfiyView(APIView):
    """
    Use this endpoint to verfiy/enable a TOTP device
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, token, format=None):
        user   = request.user
        device = get_user_totp_device(self, user)

        if not device:
            return Response(dict(errors=["This user has not setup two factor authentication"]), status=status.HTTP_400_BAD_REQUEST)

        if not device == None and device.verify_token(token):
            if not device.confirmed:
                device.confirmed = True
                device.save()
                user.is_two_factor_enabled = True
                user.save()
            return Response(True, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
