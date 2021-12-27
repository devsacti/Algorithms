# Coding Problem Solving step cycle : step 1 => 2 => 3 => 1
코딩 문제 풀이 단계 순환

## ps1 : Comprehension about Problem
['정확한 문제 해석' 관련 경험들](https://github.com/devsacti/Algorithms_Query/blob/main/PSrecords_python/PS_major_experience/ps1.md)
*실제 코딩 테스트에서는 시간 제약상 ps1에선 핵심적인 부분,특히 ps1.2,만 기록할 수 있다.

### ps1.1 Analysis
문제 눈으로 선그으면서 상황 및 개별 조건에 대한 명시적 이해

문제로부터 

설명/조건1 : ~

설명/조건2 : ~

설명/조건3 : ~

...

특히 넘버링이 0부터인지 1부터인지, 단방향 또는 양방향(무방향), 입력값 범위 보고 시간복잡도 고려해야되나 확인(greedy or binary search 등), "비례,반비례"는 기입

#### 참고사항
여집합, 역순 우선, 벤다이어그램도 필수

### ps1.2 drawing pattern, exception and easy flowchart
패턴 찾기와 예외처리, 그리고 구조화

패턴 찾기와 예외처리 :

예제의 함정(위 링크의 Error and Solution2에 설명)을 주의하되,

주로 입력-출력 예시를 바탕으로,

상황 및 조건들 간 함축적 관계에서 특정패턴을 도출하거나 관련 이론을 통한 문제 해석 후속값들은 주로 이에 근거하여 예외처리한다. 

*개인적으로 이 부분은 많은 경험이 쌓여야 능력이 성장하는 듯하다.

구조화 : 관련 종합 패턴을 참고하여 easy flowchart 만들기(그러나 컴퓨터로직화까진 not yet) 
*시간상 주로 머릿속으로만 하고, ps2.2에서 모듈 간 연결관계를 '대략적으로' 명시화하는 것이 일반적

## ps2 : utilizations and Integrations of computer algorithms for Comprehension
['(해석에) 컴퓨터 알고리즘 활용 및 통합' 관련 경험들](https://github.com/devsacti/Algorithms_Query/blob/main/PSrecords_python/PS_major_experience/ps2.md)

내가 생각하는 컴퓨터 알고리즘이란, '프로그래밍 언어로 구현가능한'된 자료구조, bfs같은 알고리즘, 그리고 주어진 상황 맞춤형 알고리즘 모두를 포함

그리고 이를 앞선 문제에 대한 해석에 접목하여 컴퓨터 언어로 시뮬레이션화하는 것을 ps과정이라고 이해

### ps2.1 utilizations of computer algorithms
한번에 다 만들려고 하지말고,퍼즐형태이든, 확장형태이든 Unit 단위로 쪼개서 모듈을 구상한다.

그리고 여유 시간 내에 에러체크 필수

* 주요 히든 케이스 처리 파트(충분한 ps1.1 후 구체적으로 인덱스나 길이 등 범주 설정 시 영감이 자주온다.)

### ps2.2 Integration of computer algorithms (with Time Complexity)

앞서 만든 모듈들을 종합하면서, 여유 시간 내 종합적인시간복잡도까지 산출
*단, 초기 구상모듈 1개로 충분할 경우, Integration은 생략가능

### ps2.3🥇 sincere solution about hidden case
히든케이스는 안보여서 히든케이스이고, 앞선 단계에서 보이지 않는 히든히든케이스의 경우

이론적으론 별개의 개인적인 테케 추가 통해서 검증 => 홀수 대신 짝수 개, 주어진 범위의 양극단 값 like 0,1개, 음수와 양수 등

하지만 문제의 상황별로 히든히든케이스는 숨는 방법이 무한가지인듯함...일단 위 기본방법들은 시도하되,중요한 것은 시간관리이므로 빠르게 다음문제로 넘어간다.

## ps3 : implemetation
['구현' 관련 경험들](https://github.com/devsacti/Algorithms_Query/blob/main/PSrecords_python/PS_major_experience/ps3.md)

정리된 모듈들은 라이브러리 등을 바탕으로 코드로 구현

다만, 시간 상 대체로 ps3을 진행하면서 ps1,2를 하게되는데, 결과적으론 순환구조에 따른다.


## major PS practice
[PS-WarmUp](https://github.com/devsacti/Algorithms_Query/tree/main/PSrecords_python/PS-WarmUp)