import streamlit as st
import pandas as pd
import requests

# Configuração da página
st.set_page_config(page_title="Sistema de Rifas", layout="wide")

def main():
    st.title("🎫 Sistema de Rifas")
    
    # Sidebar com opções
    st.sidebar.title("Opções")
    opcao = st.sidebar.radio(
        "Escolha uma opção:",
        ["Visualizar Números", "Comprar Número","Remover Comprador"]
    )
    
    # URL base da sua API FastAPI
    BASE_URL = "http://localhost:8000/numeros/"
    
    if opcao == "Visualizar Números":
        st.header("Visualização de Números")
        
        # Tabs para diferentes visualizações
        tab1, tab2, tab3 = st.tabs(["Todos os Números", "números disponíveis", "Números comprados"])
        
        with tab1:
            try:
                # Aqui você faria a chamada real para sua API
                response = requests.get(BASE_URL)
                rifa = response.json()
                

                
                df = pd.DataFrame(rifa)
                st.dataframe(
                    df,
                    column_config={
                        "numero": "Número",
                        "nome": "Nome do Comprador"
                    },
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"Erro ao carregar os dados: {e}")
        
        with tab2:
            # Filtrar apenas números disponíveis
            df_disp = df[df['nome'].isna() | (df['nome'] == "")]
            if df_disp.all:               
                st.dataframe(df_disp, use_container_width=True)
            else:
                st.info("Há números disponíveis")
        
        with tab3:
            # Filtrar apenas números indisponíveis
            st.write("Números Comprados")
                    # Filtrar números indisponíveis (nome preenchido)
            df_indisp = df[df['nome'].notna() & (df['nome'] != "")]
            if not df_indisp.empty:
                st.dataframe(df_indisp, use_container_width=True)
            else:
                st.info("Não há números indisponíveis")
    
    # elif opcao == "Adicionar Número":
    #     st.header("Adicionar Novo Número")
        
    #     with st.form("adicionar_numero"):
    #         numero = st.text_input("Número da Rifa")
    #         nome = st.text_input("Nome do Comprador")
    #         submitted = st.form_submit_button("Adicionar")
            
    #         if submitted:
    #             if numero and nome:
    #                 try:
    #                     # Aqui você faria a chamada real para sua API
    #                     response = requests.post(
    #                     BASE_URL,
    #                     json={"numero": numero, "nome": nome}
    #                     )
    #                     st.success(f"Número {numero} adicionado com sucesso!")
    #                 except Exception as e:
    #                     st.error(f"Erro ao adicionar número: {e}")
    #             else:
    #                 st.warning("Por favor, preencha todos os campos")
    
    
    elif opcao == "Comprar Número":
        st.header("Comprar Número")
        
        with st.form("comprar_numero"):
            numero_atualizar = st.text_input("Número da Rifa")
            novo_nome = st.text_input("Novo Nome do Comprador")
            submitted = st.form_submit_button("Comprar")
            
            if submitted:
                if numero_atualizar and novo_nome:
                    try:
                        # Aqui você faria a chamada real para sua API
                        response = requests.put(
                        f"{BASE_URL}{numero_atualizar}",
                        json={"nome": novo_nome}
                        )
                        st.success(f"Número {numero_atualizar} comprado com sucesso!")
                    except Exception as e:
                        st.error(f"Erro ao comprar número: {e}")
                else:
                    st.warning("Por favor, preencha todos os campos")

    elif opcao == "Remover Comprador":
        st.header("Remover Comprador")
        
        with st.form("remover_comp"):
            numero_atualizar = st.text_input("Número da Rifa")
            submitted = st.form_submit_button("Atualizar")
            
            if submitted:
                if numero_atualizar:
                    try:
                        # Aqui você faria a chamada real para sua API
                        response = requests.put(
                        f"{BASE_URL}{numero_atualizar}",
                        json={"nome": None}
                        )
                        st.success(f"comprador do numero {numero_atualizar} removido com sucesso!")
                    except Exception as e:
                        st.error(f"Erro ao remover comprador: {e}")
                else:
                    st.warning("Por favor, preencha todos os campos")

if __name__ == "__main__":
    main()