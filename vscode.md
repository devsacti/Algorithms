# vscode
visual studio 같은 종합 ide보단  가볍게 그리고 취사선택가능한 개발환경으로

유연한 만큼, 개발환경 extension, 컴파일러 등의 추가 설치가 요구된다.

## example1.vscode 상 c/c++ extension외에도 c/c++ 컴파일러 설치

MinGW는 c/c++ 컴파일러이다.
추가로 launch.json,tasks.json을 편집하고, 실행 버튼을 별도로 설정했다.
https://www.youtube.com/watch?v=3-PD_AUSOLM
-사용자 단축키
ctrl alt c, r

## example2.vscode 상 python extension외에도 python interpreter select

python ide 설치하면 자동으로 인터프레터 딸려오고, anaconda 가상환경별로도 제공

어떤 인터프레터를 쓰든 상관없는데 전자로 설정 시 setting.json이 안생겨서 환경설정 불편
그래서 가상환경껄로 쓰고

example2.1
내 개인 패키지 import시 (실제로는 잘 작동함에도 import에 빨간줄 그어지는 현상)을
없애기 위해서는 그냥 아나콘다 인터프레터로 설정해서 생긴 setting.json에 아래 코드 삽입

"python.linting.pylintArgs": [
"--init-hook",
"import sys; sys.path.append('<path to folder your module is in>')"
]
