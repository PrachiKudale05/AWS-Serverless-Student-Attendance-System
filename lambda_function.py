import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentAttendanceinterviewQ')

s3 = boto3.client('s3')
polly = boto3.client('polly')

BUCKET_NAME = 'student-voice-bucket-interviewq'

def lambda_handler(event, context):

    try:
        body = json.loads(event['body'])

        student_id = body['s_id']
        student_name = body['s_name']

        # Save to DynamoDB
        table.put_item(
            Item={
                's_id': str(student_id),
                's_name': student_name
            }
        )

        # Generate speech
        speech_text = f"Student {student_name} has been marked present."
        response = polly.synthesize_speech(
            Text=speech_text,
            OutputFormat='mp3',
            VoiceId='Aditi'
        )

        audio_stream = response['AudioStream'].read()

        file_name = f"{student_id}_{student_name}.mp3"

        # Save MP3 to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=audio_stream,
            ContentType='audio/mpeg'
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'Student added successfully',
                'file_name': file_name
            })
        }

    except Exception as e:

        print("ERROR:", str(e))

        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }