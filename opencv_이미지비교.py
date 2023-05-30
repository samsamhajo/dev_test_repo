import cv2

def calculate_image_similarity(image1_path, image2_path):
    # 이미지 파일을 로드
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # 이미지의 히스토그램 계산
    hist1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0, 256])

    # 히스토그램 유사도 계산
    similarity1 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    #잘라서 비교하기
    start_x = 100
    start_y = 100
    end_x = 300
    end_y = 400

    cropped_image1 = image1[start_y:end_y, start_x:end_x]
    cropped_image2 = image2[start_y:end_y, start_x:end_x]

    hist3 = cv2.calcHist([cropped_image1], [0], None, [256], [0, 256])
    hist4 = cv2.calcHist([cropped_image2], [0], None, [256], [0, 256])

    similarity2 = cv2.compareHist(hist3, hist4, cv2.HISTCMP_CORREL)
    
    return similarity1, similarity2
# 이미지 파일 경로 설정
image1_path = 'C:/Users/master/Desktop/aaa.png'
image2_path = 'C:/Users/master/Desktop/bbb.png'

# 이미지 일치율 계산
similarity = calculate_image_similarity(image1_path, image2_path)

# 결과 출력
print(f"이미지 일치율: {similarity}")
