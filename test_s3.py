import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Configuração do cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_ACCESS_KEY'),
)

# Caminho correto da imagem
file_name = r'C:\Users\victor.rodrigues\Desktop\PROJETOS\Projeto Django\setup\static\assets\ícones\1x\twitter.png'
bucket_name = os.getenv('AWS_BUCKET_NAME')

try:
    # Faz o upload da imagem
    s3.upload_file(file_name, bucket_name, 'twitter.png')  # O segundo parâmetro é o nome do arquivo no S3
    print("Imagem enviada com sucesso!")
except Exception as e:
    print(f"Erro ao enviar imagem: {e}")
