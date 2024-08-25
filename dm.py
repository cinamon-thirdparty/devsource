import re

# 정규표현식 패턴
pattern = r'https?:\/\/([a-zA-Z0-9-]+\.)*naver\.com\/.*'
#https?:\/\/([a-zA-Z0-9-]+\.)?naver\.com\/[^\s]*
#https?:\/\/([a-zA-Z0-9-]+\.)*naver\.com\/.*


# 테스트할 문장 리스트
sentences = [
    "네이버 홈 : https://www.naver.com/",
    "네이버 카페 : https://section.cafe.naver.com/ca-fe/",
    "네이버 블로그 : https://section.blog.naver.com/BlogHome.naver",
    "네이버 지도 : https://map.naver.com/p/",
    "네이버 웹툰 : https://comic.naver.com/index",
    "네이버 부동산 : https://land.naver.com/",
    "네이버 쇼핑 : https://shopping.naver.com/home",
    "다음 홈 : https://www.daum.net/"
]

# URL을 추출하는 함수
def find_urls(sentences):
    for sentence in sentences:
        urls = re.findall(pattern, sentence)
        if urls:
            #print(f"Found URL in sentence: {sentence}")
            print("URL:", re.search(pattern, sentence).group())

# 함수 호출
find_urls(sentences)
