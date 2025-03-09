import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import KAKAO_API_TE, GOOGLE_API_TE
from .google_api import GooglePlace
from momogo.settings import KAKAO_API_KEY

gt = GooglePlace()

def start(request):
    context = {
        'kakao_api_key': KAKAO_API_KEY
    }
    return render(request, 'start.html', context)

@csrf_exempt  # CSRF 검증 비활성화 (테스트용)
def save_kakao_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            places = data.get("places", [])

            for item in places:
                KAKAO_API_TE.objects.update_or_create(
                    kakao_id=item["id"],
                    defaults={
                        "place_name": item["place_name"],
                        "road_address_name": item.get("road_address_name", ""),
                        "latitude": float(item["y"]),
                        "longitude": float(item["x"]),
                    }
                )

            return JsonResponse({"message": "데이터 저장 완료!"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "POST 요청만 허용됩니다."}, status=405)

@csrf_exempt  # CSRF 검증 비활성화 (테스트용)
def save_google_data(request):
    if request.method == "POST":
        try:
            # 클라이언트로부터 받은 데이터 파싱
            data = json.loads(request.body)
            places = data.get("places", [])

            for item in places:
                restaurant_name = item.get("place_name")
                if restaurant_name:
                    # 각 식당 이름으로 Google API에서 정보를 가져옴
                    restaurant_details = gt.get_restaurant_details(restaurant_name)
                    
                    if 'Error' in restaurant_details:
                        print(f'{restaurant_name}은 google map에 없습니다.')
                        continue  # API 호출 오류가 있을 경우 해당 식당은 건너뛰기

                    # Google API 정보 저장
                    try:
                        kakao_place = KAKAO_API_TE.objects.get(kakao_id=item['id'])  # Kakao API 데이터와 연결
                        
                        google_api_data = GOOGLE_API_TE(
                            kakao_id=kakao_place,  # KAKAO_API_TE와 연결
                            google_id=restaurant_details.get("place_id"),
                            name=restaurant_details.get("name"),
                            type=restaurant_details.get("type"),
                            rating=restaurant_details.get("rating"),
                            address=restaurant_details.get("address"),
                            latitude=restaurant_details.get("location", {}).get("lat"),
                            longitude=restaurant_details.get("location", {}).get("lng"),
                            open_now=restaurant_details.get("open_now"),
                            phone=restaurant_details.get("phone"),
                            price_level=restaurant_details.get("price_level"),
                            user_ratings_total=restaurant_details.get("user_ratings_total"),
                            pictures=restaurant_details.get("pictures"),
                            reviews=restaurant_details.get("reviews"),
                        )
                        google_api_data.save()  # 데이터 저장

                    except Exception as e:
                        return JsonResponse({"error": f"Failed to save to DB: {str(e)}"}, status=400)

            # 데이터 저장 완료 후 응답
            return JsonResponse({"message": "데이터 저장 완료!"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "POST 요청만 허용됩니다."}, status=405)

def invite(request):
    return render(request, 'invite.html')