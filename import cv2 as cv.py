import cv2 as cv

# ============================================
# Port number 
CAMERA_PORT = 1  # ELP Camera Port number (0, 1, 2 등)
# ============================================

print(f"📹 port {CAMERA_PORT} connecting camera...")

# 카메라 열기
capture = cv.VideoCapture(CAMERA_PORT)

if not capture.isOpened():
    print(f"❌ 포트 {CAMERA_PORT}에서 카메라를 열 수 없습니다!")
    print("다른 포트 번호를 시도해보세요 (0, 1, 2...)")
    exit()

# 카메라 설정
capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
capture.set(cv.CAP_PROP_FPS, 30)

print(f"✅ Port {CAMERA_PORT} camera connection success!")
print("ESC end")

while True:
    ret, frame = capture.read()
    
    if not ret:
        print("❌ 프레임을 읽을 수 없습니다!")
        break
    
    # 포트 번호 표시
    cv.putText(frame, f'Port: {CAMERA_PORT}', (10, 30),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv.imshow(f'ELP Camera - Port {CAMERA_PORT}', frame)
    
    if cv.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv.destroyAllWindows()
print("✅ 카메라 종료")