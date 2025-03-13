from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import now
from django.core.exceptions import ObjectDoesNotExist
from .models import Coupon, CouponClaim
import datetime
import uuid

def get_client_ip(request):
    """ Get user IP address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def claim_coupon(request):
    """ Handles coupon distribution with abuse prevention """
    ip_address = get_client_ip(request)
    session_id = request.session.session_key or request.session.create()
    time_threshold = now() - datetime.timedelta(hours=1)

    # Check if user has already claimed within the restriction time
    last_claim = CouponClaim.objects.filter(ip_address=ip_address).order_by('-timestamp').first()
    if last_claim and last_claim.timestamp >= time_threshold:
        remaining_time = (last_claim.timestamp + datetime.timedelta(hours=1)) - now()
        minutes_left = round(remaining_time.total_seconds() / 60)
        return JsonResponse({"error": f"You have already claimed a coupon. Try again in {minutes_left} minutes."}, status=400)

    last_claim_session = CouponClaim.objects.filter(session_id=session_id).order_by('-timestamp').first()
    if last_claim_session and last_claim_session.timestamp >= time_threshold:
        remaining_time = (last_claim_session.timestamp + datetime.timedelta(hours=1)) - now()
        minutes_left = round(remaining_time.total_seconds() / 60)
        return JsonResponse({"error": f"You have already claimed a coupon from this browser. Try again in {minutes_left} minutes."}, status=400)

    # Fetch the next available coupon
    coupon = Coupon.objects.filter(is_claimed=False).first()
    
    if not coupon:
        # Auto-add unique coupons (optional)
        for _ in range(5):
            unique_code = f"AUTO_COUPON_{uuid.uuid4().hex[:6]}"  # Generate a unique coupon code
            Coupon.objects.create(code=unique_code)
        return JsonResponse({"error": "Coupons were empty, but new ones have been added. Try again!"}, status=400)

    # Mark as claimed
    coupon.is_claimed = True
    coupon.save()

    # Log claim
    CouponClaim.objects.create(ip_address=ip_address, session_id=session_id, coupon=coupon)

    return JsonResponse({"success": f"Coupon {coupon.code} claimed successfully!"})

# Add this function to render the HTML page
def coupon_page(request):
    return render(request, 'index.html')