import streamlit as st
import requests

# URL da sua API FastAPI
API_URL = "http://127.0.0.1:8000"

st.title("API Client - HTTP Methods")

# Criando abas para cada método HTTP
tab1, tab2, tab3, tab4 = st.tabs(["GET Items", "POST Item", "PUT Item", "DELETE Item"])

# Tab GET - Obter todos os itens
with tab1:
    st.header("GET Items")
    if st.button("Obter todos os itens"):
        response = requests.get(f"{API_URL}/items/")
        if response.status_code == 200:
            items = response.json()
            st.write(items)
        else:
            st.error("Erro ao obter os itens")

# Tab POST - Inserir novo item
with tab2:
    st.header("POST Item")
    
    # Inputs para criar um novo item
    name = st.text_input("Nome do Item")
    price = st.number_input("Preço do Item", min_value=0.01, step=0.01)
    is_offer = st.selectbox("É uma oferta?", options=[True, False])

    if st.button("Criar Item"):
        # Dados a serem enviados
        data = {"name": name, "price": price, "is_offer": is_offer}
        
        response = requests.post(f"{API_URL}/items/", json=data)
        if response.status_code == 200:
            st.success("Item criado com sucesso!")
            st.write(response.json())
        else:
            st.error("Erro ao criar o item")

# Tab PUT - Atualizar item existente
with tab3:
    st.header("PUT Item")

    # Inputs para atualizar um item
    item_id = st.number_input("ID do Item", min_value=1, step=1)
    new_name = st.text_input("Novo Nome do Item")
    new_price = st.number_input("Novo Preço do Item", min_value=0.01, step=0.01)
    new_is_offer = st.selectbox("Nova oferta?", options=[True, False])

    if st.button("Atualizar Item"):
        # Dados a serem atualizados
        update_data = {"name": new_name, "price": new_price, "is_offer": new_is_offer}
        
        response = requests.put(f"{API_URL}/items/{item_id}", json=update_data)
        if response.status_code == 200:
            st.success("Item atualizado com sucesso!")
            st.write(response.json())
        else:
            st.error(f"Erro ao atualizar o item ID {item_id}")

# Tab DELETE - Excluir item existente
with tab4:
    st.header("DELETE Item")

    # Input para excluir um item pelo ID
    delete_item_id = st.number_input("ID do Item para Deletar", min_value=1, step=1)

    if st.button("Deletar Item"):
        response = requests.delete(f"{API_URL}/items/{delete_item_id}")
        if response.status_code == 200:
            st.success(f"Item ID {delete_item_id} deletado com sucesso!")
        else:
            st.error(f"Erro ao deletar o item ID {delete_item_id}")
