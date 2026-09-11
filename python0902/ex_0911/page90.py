from langchain_openai import ChatOpenAI

# 객체 생성
llm = ChatOpenAI(                   
    temperature=0.1,                # 창의성 (0.0 ~ 2.0)
    model_name="gpt-5.6-luna",      # 모델명
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
llm_with_logprob = ChatOpenAI(
    temperature=0.1,
    max_tokens=2048,    # 최대 토큰 수 
    model_name="gpt-5.6-luna",
).bind(logprobs=True)