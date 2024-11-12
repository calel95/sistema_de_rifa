import streamlit as st
import pandas as pd
import requests
import random
from datetime import datetime
import time

# Configuração da página
st.set_page_config(page_title="Sistema de Rifas", layout="wide")

if 'lista_ganhadores' not in st.session_state:
    st.session_state.lista_ganhadores = []

def realizar_sorteio(numeros_preenchidos):
    if not numeros_preenchidos.empty:
        numero_sorteado = random.choice(numeros_preenchidos["numero"].tolist())
        ganhador = numeros_preenchidos[numeros_preenchidos["numero"] == numero_sorteado].iloc[0]
        return ganhador

def main():
    st.title("🎫 Sistema de Rifas")
    
    # Sidebar com opções
    st.sidebar.title("Opções")
    opcao = st.sidebar.radio(
        "Escolha uma opção:",
        ["Visualizar Números", "Comprar/Atualizar Número","Remover Comprador", "Realizar Sorteio","Visualizar Ganhadores"]
    )
    
    #BASE_URL = "http://localhost:8000/numeros/"
    BASE_URL = "http://backend:8000/numeros/"
    BASE_URL = "https://sistema-de-rifa.onrender.com/numeros/"
    
    if opcao == "Visualizar Números":
        st.header("Visualização de Números")
        
        tab1, tab2, tab3 = st.tabs(["Todos os Números", "números disponíveis", "Números comprados"])
        
        with tab1:
            try:
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
            df_disp = df[df['nome'].isna() | (df['nome'] == "")]
            if df_disp.all:               
                st.dataframe(df_disp, use_container_width=True)
            else:
                st.info("Há números disponíveis")
        
        with tab3:
            st.write("Números Comprados")
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
    
    
    elif opcao == "Comprar/Atualizar Número":
        st.header("Comprar/Atualizar Número")
        
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

    elif opcao == "Realizar Sorteio":
        st.header("Realizar Sorteio")

        try:
            response = requests.get(BASE_URL)
            if response.status_code == 200:
                dados = response.json()
                df = pd.DataFrame(dados)

                numeros_preenchidos = df[df['nome'].notna() & (df['nome'] != "")]
                st.write(f"Total de números participando do sorteio: {len(numeros_preenchidos)}")

                if st.button("Realizar Sorteio"):
                    if not numeros_preenchidos.empty:
                        with st.spinner("Realizando sorteio..."):                            
                            time.sleep(2)
                                                        
                            ganhador = realizar_sorteio(numeros_preenchidos)                                                        
                            resultado = st.container()
                            with resultado:
                                st.balloons()  # Efeito visual
                                st.markdown("## 🎉 Resultado do Sorteio!")
                                st.markdown(f"""
                                    ### Número Sorteado: {ganhador['numero']}
                                    ### Ganhador(a): {ganhador['nome']}
                                    #### Data e Hora do Sorteio: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
                                """)
                                novo_ganhador = {"Número Sorteado": ganhador['numero'], "Ganhador(a)": ganhador['nome']}
                                st.session_state.lista_ganhadores.append(novo_ganhador)                                

                    else:
                        st.error("Não há números participando do sorteio!")
                
                with st.expander("Ver Lista de Participantes"):
                    st.dataframe(
                        numeros_preenchidos,
                        column_config={
                            "numero": "Número",
                            "nome": "Nome do Participante"
                        },
                        use_container_width=True
                    )
            else:
                st.error("Erro ao obter dados da API")
        except Exception as e:
            st.error(f"Erro ao carregar dados para o sorteio: {e}")

    elif opcao == "Visualizar Ganhadores":
        st.header("🏆 Lista de Ganhadores")
        df_ganhadores = pd.DataFrame(st.session_state.lista_ganhadores)
        # st.dataframe(
        #             df_ganhadores,
        #             use_container_width=True
        #         )
        st.markdown(df_ganhadores.to_html(index=False), unsafe_allow_html=True)




if __name__ == "__main__":
    main()