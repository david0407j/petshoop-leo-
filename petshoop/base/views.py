from django.shortcuts import render


def home(request):
    return render(request, "base/home.html")


def plano(request):
    planos = [
        {
            "tipo": "basico",
            "nome": "Básico",
            "descricao": "Ideal para manutenção regular",
            "preco": "R$ 49,90/mês",
            "imagem": "img/shoop.jpg",
            "mercado_pago_url": "https://mpago.la/EXEMPLO-BASICO",
            "beneficios": ["Banho e Tosa", "Higienização de Ouvidos", "Corte de Unhas"],
        },
        {
            "tipo": "intermediario",
            "nome": "Intermediário",
            "descricao": "Para pets que precisam de cuidados extras",
            "preco": "R$ 79,90/mês",
            "imagem": "img/banho.jpg",
            "mercado_pago_url": "https://mpago.la/EXEMPLO-INTERMEDIARIO",
            "beneficios": [
                "Banho e Tosa",
                "Higienização Completa",
                "Corte de Unhas",
                "Escovação de Dentes",
            ],
        },
        {
            "tipo": "premium",
            "nome": "Premium",
            "descricao": "O pacote mais completo para o bem-estar do seu pet",
            "preco": "R$ 109,90/mês",
            "imagem": "img/sho.jpg",
            "mercado_pago_url": "https://mpago.la/EXEMPLO-PREMIUM",
            "beneficios": [
                "Banho e Tosa Completa",
                "Higienização Completa",
                "Corte de Unhas",
                "Escovação de Dentes",
                "Massagem Relaxante",
            ],
        },
    ]
    return render(request, "base/plano.html", {"planos": planos})


def assinar_plano(request, tipo):
    return render(request, "base/assinar.html", {"tipo": tipo})
