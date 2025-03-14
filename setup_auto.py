import os
import subprocess
import sys

# 필요한 라이브러리 리스트
REQUIRED_LIBS = ["streamlit", "pandas", "openpyxl"]

def install_packages():
    """필요한 패키지를 설치하는 함수"""
    for lib in REQUIRED_LIBS:
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", lib], check=True)
            print(f"{lib} 설치 완료 ✅")
        except subprocess.CalledProcessError:
            print(f"{lib} 설치 실패 ❌")

def run_streamlit():
    """Streamlit 앱 실행"""
    print("🚀 프로그램을 실행합니다...")
    subprocess.run(["streamlit", "run", "app.py"])

if __name__ == "__main__":
    print("📦 필수 패키지를 설치합니다...")
    install_packages()
    print("✅ 모든 패키지 설치 완료!")
    
    # app.py가 존재하는지 확인 후 실행
    if os.path.exists("app.py"):
        run_streamlit()
    else:
        print("⚠️ 'app.py' 파일이 존재하지 않습니다. 먼저 app.py를 생성해 주세요.")