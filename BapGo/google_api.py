import requests
import os

class GooglePlace():
    """
    아래 코드는 Google Places API를 활용하여 식당 정보를 검색하는 기능을 네 가지 책임으로 분리한 예시이다.
        _get_place_id: 식당 이름으로 place_id를 가져오는 함수
        _get_place_details: place_id로 장소 상세 정보를 가져오는 함수
        _parse_place_data: 가져온 상세 정보 JSON을 원하는 데이터 구조로 파싱하는 함수
        get_restaurant_details: 위 세 함수를 연계하여 최종 결과를 반환하는 함수
    """
    def __init__(self):
        # Google Places API 키를 인스턴스 변수로 저장
        self.APIKEY = "AIzaSyC-UiOG588zN5JeLzcU3mcnPn5nrT86sh4"
        print(os.getenv("GOOGLE_PLACES_API_KEY"))

    def _get_place_id(self, restaurant_name):
        """
        주어진 식당 이름을 이용해 Google Places의 Text Search API를 호출하여
        해당 식당의 place_id를 반환하는 함수.
        """
        # 텍스트 검색 엔드포인트
        endpoint_search = "https://maps.googleapis.com/maps/api/place/textsearch/json"

        # 요청 시 필요한 파라미터 설정
        search_params = {
            "query": restaurant_name,  # 검색할 식당 이름
            "key": self.APIKEY,  # API 키
            "language": "ko"  # 응답 언어(한국어)
        }

        # API 요청 및 응답 처리
        response = requests.get(endpoint_search, params=search_params)
        response_data = response.json()

        # 응답 상태 코드 및 결과 상태 확인
        if response.status_code == 200 and response_data.get('status') == "OK" and response_data.get('results'):
            # 결과 중 첫 번째 장소 정보 획득
            result = response_data['results'][0]
            # place_id 추출
            place_id = result.get("place_id")
            if place_id:
                return place_id
            else:
                # place_id가 없는 경우 None 반환
                return None
        else:
            # 검색 실패 또는 결과 없음
            return None

    def _get_place_details(self, place_id):
        """
        place_id를 이용해 Google Places의 상세 정보 API를 호출하고
        해당 장소의 상세 정보(결과 JSON)를 반환하는 함수.

        결과구조 참고:
        - https://developers.google.com/maps/documentation/places/web-service/details?hl=ko
        """
        # 장소 상세 정보 엔드포인트
        endpoint_details = "https://maps.googleapis.com/maps/api/place/details/json"

        # 상세 정보 요청 파라미터 설정
        details_params = {
            "place_id": place_id,
            "fields": "name,formatted_address,formatted_phone_number,rating,user_ratings_total,opening_hours,photos,reviews,price_level,geometry,types",
            "key": self.APIKEY,
            'language': 'ko'
        }

        # API 요청 및 응답 처리
        details_response = requests.get(endpoint_details, params=details_params)
        # 결과 데이터에서 "result" 키의 값을 반환 (없으면 빈 dict)
        return details_response.json().get("result", {})

    def _parse_place_data(self, details_data):
        """
        get_place_details로부터 받은 상세 정보 JSON 데이터를
        요구되는 형태의 딕셔너리 구조로 파싱하는 함수.

        파싱 결과의 데이터 구조
        {
            "place_id": str,                         # Unique identifier for the place
            "name": str,                             # Name of the restaurant
            "type": str,                             # A comma-separated list of place types
            "rating": float or None,                 # Average user rating (0.0 ~ 5.0), or None
            "address": str or None,                  # Formatted address of the place
            "location": {
                "lat": float,                        # Latitude of the place
                "lng": float                         # Longitude of the place
            } or None,
            "opening_hours": {
                "open_now": bool,                    # Indicates if the place is currently open
                "periods": [...],                    # Detailed periods when the place is open (if provided)
                "weekday_text": [...]                # Human-readable opening hours per weekday (if provided)
            } or None,
            "open_now": bool or None,                # Current open status extracted for convenience
            "phone": str or None,                    # Formatted phone number
            "price_level": int or None,              # Price level (0 ~ 4)
            "user_ratings_total": int or None,       # Total number of user ratings
            "pictures": [
                str,                                 # URL to the first picture
                str,                                 # URL to the second picture
                ... up to 5 pictures
            ],
            "reviews": [
                {
                    "date": str,                    # Relative time description (e.g., "a month ago")
                    "rate": int or float,           # Individual rating for that review
                    "text": str                     # Actual review text
                },
                ...
            ]
        }

        """

        # geometry 정보에서 위치 정보(location) 추출
        geometry = details_data.get('geometry', {})
        if not isinstance(geometry, dict):
            geometry = {}
        location = geometry.get('location', None)
        if not (isinstance(location, dict) and 'lat' in location and 'lng' in location):
            location = None

        # 영업시간 정보 추출
        opening_hours = details_data.get("opening_hours", {})
        if not isinstance(opening_hours, dict):
            opening_hours = {}
        open_now = opening_hours.get('open_now', None)
        if open_now is not None and not isinstance(open_now, bool):
            open_now = None

        # types 리스트를 콤마로 구분된 문자열로 변환
        types_data = details_data.get("types", [])
        if not isinstance(types_data, list):
            types_data = []
        valid_types = [t for t in types_data if isinstance(t, str)]
        type_str = ", ".join(valid_types)

        # 사진 정보 파싱: photo_reference를 이용해 사진 URL 생성
        pictures = []
        photos_data = details_data.get("photos", [])
        if isinstance(photos_data, list):
            for photo in photos_data[:5]:
                if isinstance(photo, dict) and 'photo_reference' in photo:
                    pictures.append(
                        f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo['photo_reference']}&key={self.APIKEY}"
                    )

        # 리뷰 정보 파싱
        reviews = []
        reviews_data = details_data.get("reviews", [])
        if isinstance(reviews_data, list):
            for review in reviews_data:
                if isinstance(review, dict):
                    date = review.get("relative_time_description")
                    rate = review.get("rating")
                    text = review.get("text")
                    # 타입 검증 (필요시)
                    if isinstance(date, str) and (isinstance(rate, (int, float)) or rate is None) and isinstance(text,
                                                                                                                 str):
                        reviews.append({"date": date, "rate": rate, "text": text})

        # 최종 반환할 식당 정보 딕셔너리 구성
        restaurant_details = {
            # 'place_id': details_data.get("reference"),
            "name": details_data.get("name"),
            "type": type_str,
            "rating": details_data.get("rating"),
            "address": details_data.get("formatted_address"),
            'location': location,
            "opening_hours": opening_hours if opening_hours else None,
            "open_now": open_now if open_now is not None else None,
            "phone": details_data.get("formatted_phone_number"),
            'price_level': details_data.get("price_level"),
            'user_ratings_total': details_data.get("user_ratings_total"),
            "pictures": pictures,
            "reviews": reviews,
        }
        return restaurant_details

    def get_restaurant_details(self, restaurant_name):
        """
        식당 이름을 받아 위 함수들을 순서대로 호출해
        최종적으로 파싱된 식당 상세 정보를 반환하는 함수.

        """
        try:
            # 식당 이름으로 place_id 획득
            place_id = self._get_place_id(restaurant_name)
            if not place_id:
                # place_id를 찾을 수 없는 경우 에러 반환
                return {"Error": "No valid place_id could be found for the given restaurant."}

            # place_id로 상세 정보 데이터 획득
            details_data = self._get_place_details(place_id)
            if not details_data:
                # 상세 정보가 없는 경우 에러 반환
                return {"Error": "No details found for the given place_id."}

            # 상세 정보 데이터를 파싱하여 최종 결과 반환
            restaurant_details = self._parse_place_data(details_data)
            restaurant_details['place_id'] = place_id
            return restaurant_details

        except Exception as e:
            # 예외 발생 시 에러 메시지 반환
            return {"Error": str(e)}


# Example usage

# restaurant_name = "더베이커스테이블"
# gp = GooglePlace()


# restaurant_data = gp.get_restaurant_details(restaurant_name)
# print(restaurant_data)
