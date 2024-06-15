from django.shortcuts import render, redirect
import time

def inicio():
    return "Olá! Bem-vindo ao sistema de troca de produtos da Sanofi."

def solicitacao(solicitation_number):
    sample_data = {
        "012": {"status": "Confirmando estoque", "detalhes": "Produto X aguardando confirmação de estoque."},
        "345": {"status": "Estoque confirmado", "detalhes": "Produto X disponível na Farmácia Y."},
        "678": {"status": "Aguardando retirada no ponto de troca", "detalhes": "Produto X disponível na Farmácia Y. Código de retirada: ABC123"},
        "910": {"status": "Troca finalizada", "detalhes": "Produto X retirado com sucesso."}
    }
    return sample_data.get(solicitation_number, None)

def cancelar_solicitacao(solicitation_number):
    return f"Solicitação {solicitation_number} foi cancelada com sucesso."

def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        context = request.session.get('context', {
            'messages': [inicio()]
        })
        
        if 'name' not in context:
            context['name'] = user_input
            context['messages'].append(f"Olá {context['name']}, como posso ajudá-lo hoje?")
            context['messages'].append("1. Consultar status da solicitação de troca")
            context['messages'].append("2. Cancelar uma solicitação")
            context['messages'].append("3. Sair")
        else:
            if 'awaiting_input' in context:
                if context['awaiting_input'] == 'consult':
                    solicitation_number = user_input
                    result = solicitacao(solicitation_number)
                    if result:
                        context['messages'].append(f"O status da sua solicitação ({solicitation_number}) é: {result['status']}")
                        context['messages'].append(f"Detalhes: {result['detalhes']}")
                    else:
                        context['messages'].append("Número de solicitação não encontrado.")
                    del context['awaiting_input']
                elif context['awaiting_input'] == 'cancel':
                    solicitation_number = user_input
                    result = solicitacao(solicitation_number)
                    if result:
                        context['messages'].append(cancelar_solicitacao(solicitation_number))
                    else:
                        context['messages'].append("Número de solicitação não encontrado.")
                    del context['awaiting_input']
            else:
                if user_input == '1':
                    context['messages'].append("Por favor, digite o número da sua solicitação de troca:")
                    context['awaiting_input'] = 'consult'
                elif user_input == '2':
                    context['messages'].append("Por favor, digite o número da sua solicitação que deseja cancelar:")
                    context['awaiting_input'] = 'cancel'
                elif user_input == '3':
                    context['messages'].append("Obrigado por usar o sistema de troca de produtos da Sanofi. Até logo!")
                    request.session.flush()  # Clear the session to start a new conversation
                    return redirect('chat')
                else:
                    context['messages'].append("Opção inválida. Por favor, tente novamente.")
        
        request.session['context'] = context
        return redirect('chat')

    context = request.session.get('context', {
        'messages': [inicio()]
    })
    return render(request, 'chat.html', context)
