from langchain_openai import ChatOpenAI

# 객체 생성
llm = ChatOpenAI(                   
    temperature=0.1,                # 창의성 (0.0 ~ 2.0)
    model_name="gpt-5.6-luna",      # 모델명
)
# 최신 버전 langChain1.0
llm = ChatOpenAI(                   
    temperature=0.1,                # 창의성 (0.0 ~ 2.0)
    model="gpt-5.6-luna",      # 모델명
)
# 질의 내용
question = "대한민국의 수도는?"             
# 질의
#print(f"[답변]: {llm.invoke(question)}")
# [답변]: content='대한민국의 수도는 **서울특별시**입니다.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 16, 'prompt_tokens': 12, 'total_tokens': 28, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0, 'text_tokens': None}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': 0, 'cached_tokens': 0, 'image_tokens': None, 'text_tokens': None}}, 'model_provider': 'openai', 'model_name': 'gpt-5.6-luna', 'system_fingerprint': None, 'id': 'chatcmpl-EMlxUBZ4MDDRqtUy0Au169q2RJlQ2', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--01a08e72-adb0-7871-b613-abc489f619d1-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 12, 'output_tokens': 16, 'total_tokens': 28, 'input_token_details': {'audio': 0, 'cache_read': 0, 'cache_creation': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

# 질의 저장
response = llm.invoke(question)

# 답변만보기
print(response.content)
# 대한민국의 수도는 서울특별시입니다.

# 메타데이터만 보기
print(response.response_metadata)
# {'token_usage': {'completion_tokens': 14, 'prompt_tokens': 12, 'total_tokens': 26, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0, 'text_tokens': None}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': 0, 'cached_tokens': 0, 'image_tokens': None, 'text_tokens': None}}, 'model_provider': 'openai', 'model_name': 'gpt-5.6-luna', 'system_fingerprint': None, 'id': 'chatcmpl-EMm54tEBGQPfXyYE7YcKS4BwJXzVb', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None}

# 메타데이터 중 토큰 사용량만 보기
print(response.response_metadata["token_usage"])
# {'completion_tokens': 14, 'prompt_tokens': 12, 'total_tokens': 26, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0, 'text_tokens': None}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': 0, 'cached_tokens': 0, 'image_tokens': None, 'text_tokens': None}}

# logprob 활성화하기
# LangChain 1.0에서는 bind() 대신 ChatOpenAI 생성자에서 직접 설정함.
# gpt-5.6-luna는 Chat Completions 방식의 logprobs를 지원하지 않으므로
# logprobs 테스트를 위해 지원 모델인 gpt-4o-mini 사용함.
llm_with_logprob = ChatOpenAI(
    temperature=0.1,
    max_tokens=2048,    # 최대 토큰 수 
    model_name="gpt-4o-mini",
    logprobs=True,
    top_logprobs=3,
)

# langchain 1.0 버전
llm_with_logprob = ChatOpenAI(
    temperature=0.1,
    max_completion_tokens=2048,    # 최대 토큰 수 
    model="gpt-4o-mini",
    logprobs=True
)
print(llm_with_logprob.logprobs)

# stream() 함수로 출력하기. 스트리밍 출력.
# stream 방식으로 질의하고 답변 결과를 받음. 
answer = llm.stream("천안 불당동 맛집 10곳 알려줘")

# streaming 방식으로 각 토큰 출력
# 재활용 불가
for token in answer:
    print(token.content, end="", flush=True)

# 천안 **불당동에서 많이 찾는 맛집 10곳**을 메뉴별로 정리해드릴게요. 매장 이전·폐업·영업시간 변동이 있을 수 있으니 방문 전 지도에서 확인하는 걸 추천합니다.

# 1. **고반식당 천안불당점**  
#    - 메뉴: 숙성 삼겹살·목살  
#    - 깔끔한 고깃집을 찾을 때 좋고, 직원이 구워주는 편이라 모임에도 적합합니다.

# 2. **멘야마쯔리 불당점**  
#    - 메뉴: 돈코츠라멘, 탄탄멘, 마제소바  
#    - 천안에서 유명한 라멘집으로, 진한 일본식 라멘을 좋아하면 추천합니다.

# 3. **미도인 천안불당점**  
#    - 메뉴: 스테이크 덮밥, 대창 덮밥, 파스타  
#    - 분위기 좋은 식당으로 데이트나 가벼운 식사에 잘 어울립니다.

# 4. **온기정 천안불당점**  
#    - 메뉴: 텐동, 스테키동, 연어덮밥  
#    - 바삭한 튀김과 덮밥류를 함께 먹고 싶을 때 좋습니다.

# 5. **백소정 천안불당점**  
#    - 메뉴: 돈카츠, 마제소바, 냉소바  
#    - 돈가스와 면 요리를 함께 먹기 좋아 점심 식사로 무난합니다.

# 6. **낙원타코 천안불당점**  
#    - 메뉴: 타코, 파히타, 퀘사디아  
#    - 멕시칸 음식과 이국적인 분위기를 즐기기 좋은 곳입니다.
# ...
# - 고기: **고반식당**
# - 라멘: **멘야마쯔리**
# - 데이트: **미도인·낙원타코**
# - 초밥: **스시린**
# - 가성비 점심: **백소정·온기정**

# 재활용 가능하도록 저장
final_answer = ""
for token in answer:
    final_answer += token.content
