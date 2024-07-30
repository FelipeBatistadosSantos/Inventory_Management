from django.db import models

class Product(models.Model):
    CATEGORIA_CHOICES = [
        ('nenhum', 'Nenhum'),
        ('construcao', 'Materiais de Construção'),
        ('madeira', 'Madeira e Produtos Relacionados'),
        ('ferragens', 'Ferragens e Ferramentas'),
        ('eletrica', 'Elétrica e Iluminação'),
        ('hidraulica', 'Hidráulica'),
        ('pintura', 'Pintura e Acabamento'),
        ('pisos', 'Pisos e Revestimentos'),
        ('banheiro_cozinha', 'Banheiro e Cozinha'),
        ('jardim', 'Jardim e Paisagismo'),
        ('isolamento', 'Material de Isolamento e Impermeabilização'),
    ]

    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=400)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, default='Nenhum', null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'main_product'
