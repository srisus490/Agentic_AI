import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.create_agent_runtime(
    agentRuntimeName='strands_agent_test',
    agentRuntimeArtifact={
        'containerConfiguration': {
            'containerUri': '357171621133.dkr.ecr.us-west-2.amazonaws.com/my-strands-agent:latest'
        }
    },
    networkConfiguration={"networkMode": "PUBLIC"},
    roleArn='arn:aws:iam::357171621133:role/ETLlambdaAccessRole'
)

print(f"Agent Runtime created successfully!")
print(f"Agent Runtime ARN: {response['agentRuntimeArn']}")
print(f"Status: {response['status']}")