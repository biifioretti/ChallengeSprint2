# Projeto de Troca de Produtos - SAC AI

Este projeto visa criar um portal de atendimento entre a Sanofi e as farmácias parceiras para comunicação de devoluções para seus clientes. Inclui um chatbot integrado ao SAC da empresa via WhatsApp e o portal SAC AI de comunicação entre a Sanofi e suas parceiras. A solução proporciona uma experiência superior para o consumidor, maior eficiência operacional e redução de custos para a Sanofi.

## Link vídeo apresentação do projeto: 
**https://youtu.be/5tvURfXvQd4**

## Tecnologias Utilizadas
- **Frontend:** React (HTML, CSS, JavaScript)
- **Backend:** Django (Python)
- **Banco de Dados:** Oracle DB
- **Chatbot:** Dialogflow ou Rasa
- **Notificações:** Twilio (WhatsApp) e SendGrid (Email)
- **Ferramentas de IA:** TensorFlow, Scikit-Learn, PyTorch

## Funcionalidades Principais
1. **Cadastro de Troca:**
   - Realizado manualmente pelo pessoal da Sanofi no portal.
2. **Extração de Solicitações:**
   - Transferência das solicitações para o portal "SAC AI".
3. **Verificação de Estoque Automática:**
   - Confirmação de estoque nas farmácias próximas ao endereço do cliente via IA treinada para prever as melhores opções de retirada.
4. **Confirmação de Estoque:**
   - Notificação através do portal após confirmação.
5. **Seleção da Farmácia pelo Cliente:**
   - Cliente seleciona a farmácia, que é avisada via WhatsApp.
6. **Retirada pelo Cliente:**
   - Cliente retira o produto e confirma a retirada no portal.

## Arquivos do projeto

### chatbot.py
**Versão beta do nosso chatbot**

    Nesta versão, nosso atendente virtual do chatbot ainda não tem nenhuma inteligência artificial integrada em si. Trata-se de um script base do que pretendemos fazer via whatsapp para o cliente.

### manage.py
**Interface Django**

    Neste arquivo, utilizamos o script chatbot.py como base para demonstrar como será feita a integração de nossos arquivos do banco de dados e nosso front-end com o back-end utilizando o Django.

    
