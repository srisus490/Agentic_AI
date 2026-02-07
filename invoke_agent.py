import boto3
import json

agent_core_client = boto3.client('bedrock-agentcore', region_name='us-west-2')
payload = json.dumps({
    "input": {"prompt": "Explain how does it rains"}
})

response = agent_core_client.invoke_agent_runtime(
    agentRuntimeArn='arn:aws:bedrock-agentcore:us-west-2:357171621133:runtime/strands_agent_test-UpqRwVEzuY',
    runtimeSessionId='dfmeoagmreaklgmrkleafremoigrmtesogmtrskhmtkrlshmt',  # Must be 33+ chars
    payload=payload,
    qualifier="DEFAULT"
)

response_body = response['response'].read()
response_data = json.loads(response_body)
print("Agent Response:", response_data)