import cv2
import pandas as pd

# Função para processar uma imagem e extrair informações
def processar_imagem(imagem):
    # Carrega a imagem utilizando o pacote OpenCV
    img = cv2.imread(imagem)
    
    # Converte a imagem para escala de cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Calcula o valor médio de intensidade de pixel na imagem
    valor_medio = img_gray.mean()
    
    # Calcula a largura e altura da imagem
    altura, largura = img_gray.shape
    
    # Cria um dicionário com as informações extraídas da imagem
    info_imagem = {
        'Imagem': imagem,
        'Valor Médio': valor_medio,
        'Altura': altura,
        'Largura': largura
    }
    
    return info_imagem

# Lista de imagens para processar
imagens = ['imagem1.jpg', 'imagem2.jpg', 'imagem3.jpg']

# Lista para armazenar as informações de cada imagem
info_imagens = []

# Processa cada imagem da lista
for imagem in imagens:
    info = processar_imagem(imagem)
    info_imagens.append(info)

# Cria um DataFrame utilizando o Pandas para armazenar as informações
df = pd.DataFrame(info_imagens)

# Exibe o DataFrame
print(df)
