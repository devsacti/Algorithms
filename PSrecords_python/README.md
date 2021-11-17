# Coding Problem Solving step cycle : step 1 => 2 => 3 => 1
코딩 문제 풀이 단계 순환

## ps1 : Accurate Comprehension
정확한 문제 해석 

['정확한 문제 해석' 관련경험]()

### ps1.1 문제 눈으로 선그으면서 읽고, 개별 조건에 대한 명시적 이해
기본적인 input-process-output 과정 이해, 주로 주어진 예제를 중심으로 체크

특히 넘버링이 0부터인지 1부터인지, 입력값 범위 보고 시간복잡도 고려해야되나 확인(이진 탐색 필수 여부 등)

#### 참고사항
여집합, 역순 우선, 벤다이어그램도 필수

### ps1.2 조건들 간 함축적 관계 도출과 예외처리, 그리고 모듈화
조건들 간 함축적 관계 도출과 예외처리 : 서로 독립적으로 보이는 조건들 간의 함축적인 관계를 찾아 구조화하고, 이로 인한 새로운 패턴을 바탕으로 대체로 예외처리를 해준다.

*개인적으로 이 부분은 많은 경험이 쌓여야 능력이 성장하는 듯하다.

가령, 피보나치 규칙에 근거하여 수열을 구현하고 특정 인덱스의 값을 리턴하라고 할 때,
 
Condition1 : 주어진 1번째항과 2번째 항의 범위는 정수(+주어진 예제는 모두 자연수)

일 경우, 최초항이 -1,-2 인 경우도 고려하게 된다. 그러나,

Condition2 : 증가하는 수열에 한해서만 출력값 요구

라는 조건이 주어질 경우, -1,-2가 1,2번째항으로 주워지면 이 피보나치 규칙에 기반한 후속값들은 더욱 작은 음수값이 되므로 예외처리해야 한다.


모듈화 : 관련 종합 패턴을 참고하여 easy flowchart 만들기(그러나 컴퓨터로직화까진 not yet) 

만약, 문제를 이해하는 데 피보나치 수열이나 소수개념 등이 활용가능하다면 접목하여 '해석'


## ps2 : utilizations and Integrations of computer algorithms with Time Complexity
해석에 컴퓨터 알고리즘 활용 및 통합

컴퓨터 알고리즘이란, 대표적인 bfs,dfs뿐만 아니라 '프로그래밍 언어로 구현가능한'된 자료구나 라이브러리, 그리고 상황에 맞는 즉석모듈형태를 모두 포함

['컴퓨터 알고리즘 활용 및 통합' 관련경험]()


### ps2.1 utilizations of computer algorithms
한번에 다 만들려고 하지말고,퍼즐형태이든, 확장형태이든 Unit 단위로 쪼개서 모듈을 코드로 구현한다.

그리고 여유 시간 내에 에러체크 필수

* 주요 히든 케이스 처리 파트(step1 보다 인덱스나 길이 등 범주 설정 시 영감이 자주온다.)

### ps2.2 Integrations of computer algorithms

앞서 만든 모듈들을 이론상 종합하면서, 여유 시간 내 시간복잡도까지 산출

* 종합 시간복잡도도 도출

## ps3 : implemetation
정리된 모듈들은 코드로 구현

다만, 시간 상 대체로 ps3을 진행하면서 ps1,2를 하게되는데, 결과적으론 순환구조에 따른다.

 
['구현' 관련경험](https://github.com/devsacti/Algorithms_Query/blob/main/PSrecords_python/PS-concept/3.ImplementationErrorList.txt)

## 🥇 hidden case and steps
처음 문제이해와 알고리즘화에서 보이지 않는다면

정석적으론 테케 추가를 통해서 검증 => 홀수 대신 짝수 개, 주어진 범위의 양극단 값 like 0,1개, 음수와 양수 등

하지만 문제의 상황별로 히든케이스는 숨는 방법도 다른듯함...일단 위 기본방법들 기입


## [PS-WarmUp](https://github.com/devsacti/Algorithms_Query/tree/main/PSrecords_python/PS-WarmUp)
 practice
