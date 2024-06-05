import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go


# Configuração da pg
st.set_page_config(
    page_title="Tecnologia Médica Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# sidebar
with st.sidebar:
    st.title('⚕️Índice de Tecnologia Médica por País')
    selected_year = st.selectbox("Selecione o ano:", [2019, 2020, 2021, 2022, 2023])
    metric = st.selectbox ("Selecione o Métrico:", ['Acesso a Tecnologia', 'Infraestrutura Médica', 'Resultados de Saúde'])
    st.markdown("Autora: Ghabriela de Oliveira Santos Luminato") 
    st.markdown("#PDITA 472") 
 
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    

# Dados
data = {
    'País': ['Estados Unidos', 'Alemanha', 'Japão', 'Reino Unido', 'França', 'China', 'Brasil', 'Índia', 'Rússia', 'África do Sul'],
    2019: {
        'Acesso a Tecnologia': [90, 85, 88, 83, 80, 70, 55, 50, 45, 40],
        'Infraestrutura Médica': [88, 85, 87, 82, 78, 72, 60, 55, 50, 45],
        'Resultados de Saúde': [85, 84, 86, 80, 75, 70, 65, 60, 55, 50]
    },
    2020: {
        'Acesso a Tecnologia': [91, 86, 89, 84, 81, 71, 56, 51, 46, 41],
        'Infraestrutura Médica': [89, 86, 88, 83, 79, 73, 61, 56, 51, 46],
        'Resultados de Saúde': [86, 85, 87, 81, 76, 71, 66, 61, 56, 51]
    },
    2021: {
        'Acesso a Tecnologia': [92, 87, 90, 85, 82, 72, 57, 52, 47, 42],
        'Infraestrutura Médica': [90, 87, 89, 84, 80, 74, 62, 57, 52, 47],
        'Resultados de Saúde': [87, 86, 88, 82, 77, 72, 67, 62, 57, 52]
    },
    2022: {
        'Acesso a Tecnologia': [93, 88, 91, 86, 83, 73, 58, 53, 48, 43],
        'Infraestrutura Médica': [91, 88, 90, 85, 81, 75, 63, 58, 53, 48],
        'Resultados de Saúde': [88, 87, 89, 83, 78, 73, 68, 63, 58, 53]
    },
    2023: {
        'Acesso a Tecnologia': [94, 89, 92, 87, 84, 74, 59, 54, 49, 44],
        'Infraestrutura Médica': [92, 89, 91, 86, 82, 76, 64, 59, 54, 49],
        'Resultados de Saúde': [89, 88, 90, 84, 79, 74, 69, 64, 59, 54]
    },
}
# Converter as chaves para inteiros
data = {int(key) if isinstance(key, str) and key.isdigit() else key: value for key, value in data.items()}

# Converter os dados em DataFrame
records = []


for year, metrics in data.items():
    if year != 'País':
        for i, country in enumerate(data['País']):
            record = {
                'Ano': year,
                'País': country,
                'Acesso a Tecnologia': metrics['Acesso a Tecnologia'][i],
                'Infraestrutura Médica': metrics['Infraestrutura Médica'][i],
                'Resultados de Saúde': metrics['Resultados de Saúde'][i]
            }
            records.append(record)

df = pd.DataFrame(records)


# Filtrar o DataFrame pelo ano selecionado
df_selected_year = df[df['Ano'] == selected_year].drop(columns=['Ano'])




# Layout com duas colunas
col1, col2 , col3, = st.columns(3)

#TABELA
with col3: 
  st.write(df_selected_year, height=100)


# Gráfico de barras para comparar as métricas entre os países selecionados
fig_bar = px.bar(df_selected_year, x='País', y=metric, color='País', title=f'{metric} Países (Ano {selected_year})')
fig_bar.update_layout(width=800, height=400,)
with col1:
    st.plotly_chart(fig_bar, use_container_width=True)
    
# Gráfico de pizza baseado na métrica selecionada
with col3:
    fig = px.pie(df, names='País', values=metric, title=f'Evolução de {metric} por País')
    # Ajustar o tamanho do gráfico
    fig.update_layout(height=400, width=200,)
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersão para visualizar a relação entre duas métricas
    metrics_to_compare = ['Infraestrutura Médica', 'Resultados de Saúde',] if metric == 'Acesso a Tecnologia' else ['Acesso a Tecnologia', 'Infraestrutura Médica','Resultados de Saúde']
    fig_scatter = px.scatter(df_selected_year, x=metrics_to_compare[0], y=metrics_to_compare[1], color='País', title=f'Relação entre {metrics_to_compare[0]} e {metrics_to_compare[1]} (Ano {selected_year})')
    fig_scatter.update_layout(width=700, height=400,)
    with col1:
        st.plotly_chart(fig_scatter, use_container_width=False)
        
         
   
