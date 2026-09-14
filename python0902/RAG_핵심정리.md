# RAG 핵심 정리

## RAG란?

RAG(Retrieval-Augmented Generation)는 **질문과 관련된 외부 자료를 먼저 검색하고, 검색 결과를 Context로 LLM에 전달해 답변을 생성하는 방식**임.

```text
문서 준비: Load → Split → Embed → Store
질문 처리: 질문 → Retriever → Prompt → LLM → 답변
전체 흐름: Chain이 연결하고 제어
```

## 8단계

| 단계 | 핵심 역할 |
| --- | --- |
| 1. Load | PDF, 웹, DB 등의 문서와 출처 정보를 읽어옴. |
| 2. Split | 문맥이 끊기지 않도록 문서를 작은 Chunk로 나눔. |
| 3. Embed | Chunk와 질문의 의미를 비교 가능한 실수 Vector로 변환함. |
| 4. Store | Vector, 원문, 출처를 Vector DB에 영구 저장함. |
| 5. Retriever | 질문과 가장 관련 있는 Chunk를 검색함. |
| 6. Prompt | 질문, 검색된 Context, 답변 규칙을 하나의 입력으로 구성함. |
| 7. LLM | 주어진 Context를 근거로 자연어 답변을 생성함. |
| 8. Chain | 검색, 재시도, 생성, 출처 표시 등 전체 실행 순서를 연결함. |

## 꼭 구분할 개념

### Embedding과 Fine-tuning

- **Embedding**: 텍스트나 이미지의 의미를 Vector로 표현함.
- **Fine-tuning**: 특정 작업이나 말투에 맞도록 모델의 가중치를 추가 학습함.
- 문서를 임베딩하여 DB에 저장하는 것은 Fine-tuning이 아님.

### Retriever와 Retry

- **Retriever**는 관련 자료를 찾아오는 검색기임.
- 검색 결과가 부족하면 질문 재작성, 재검색, Reranking 같은 Retry 흐름을 추가할 수 있음.

### Context

Context는 Retriever가 찾아서 LLM이 답변할 때 참고하도록 Prompt에 넣은 자료임. 관련 없는 Context가 많으면 오히려 답변 품질이 낮아질 수 있음.

## Vector DB 선택

| 선택지 | 적합한 경우 |
| --- | --- |
| PostgreSQL + pgvector | 관계형 데이터와 Vector를 SQL로 함께 관리할 때 |
| Qdrant | 전용 Vector DB의 검색과 필터 기능을 학습할 때 |

PostgreSQL을 먼저 학습하고 있다면 `pgvector`로 RAG를 구현한 뒤, 같은 데이터를 Qdrant에도 넣어 결과와 사용 방식을 비교해 보는 것이 좋음.

## 왜 개발자가 필요한가?

RAG의 정확도는 LLM 하나가 아니라 모든 단계에 의해 결정됨.

```text
문서 품질 → Chunk 품질 → Embedding → 검색 결과 → Context → LLM 답변
```

개발자는 다음을 설계하고 검증해야 함.

- 문서 갱신과 접근 권한
- Chunk 크기와 검색 방식
- 검색 실패 시 재시도 과정
- 답변의 근거와 출처
- 개인정보와 Prompt Injection 방어
- 정확도, 응답 시간, 비용 평가

## 한 줄 정리

> RAG는 LLM이 더 많이 기억하게 만드는 기술이 아니라, **질문에 필요한 근거를 찾아서 정확하게 참고하도록 만드는 시스템**임.

