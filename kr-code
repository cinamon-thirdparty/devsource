import re
import hashlib

def hash_resident_number(resident_number):
    # 입력받은 주민번호를 인코딩하여 바이트로 변환
    encoded_number = resident_number.encode('utf-8')
    
    # SHA256 해시 객체 생성
    sha256 = hashlib.sha256()
    
    # 해시 객체에 인코딩된 주민번호 업데이트
    sha256.update(encoded_number)
    
    # 해시값을 16진수 문자열로 변환하여 반환
    hash_value = sha256.hexdigest()
    
    return hash_value

def replace_resident_number_with_hash(text):
    # 주민번호 패턴 (예: 123456-1234567)
    pattern = r'\d{6}-\d{7}'
    
    # 주어진 텍스트에서 주민번호 찾기
    match = re.search(pattern, text)
    
    if match:
        # 찾은 주민번호를 해시값으로 변환
        resident_number = match.group()
        hashed_value = hash_resident_number(resident_number)
        
        # 주민번호를 해시값으로 대체
        new_text = text.replace(resident_number, hashed_value)
        return new_text
    else:
        # 주민번호가 없을 경우 원본 텍스트 반환
        return text

# 예시 사용법
original_text = "사용자의 주민번호는 123456-1234567 이오니 참고하세요"
modified_text = replace_resident_number_with_hash(original_text)
print(f"Original: {original_text}\nModified: {modified_text}")
