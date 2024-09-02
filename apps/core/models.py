from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name="Nome",
        max_length=255
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        verbose_name="Nome",
        max_length=255
    )
    description = models.TextField(
        verbose_name="Descrição",
        blank=True,
        null=True
    )
    price = models.DecimalField(
        verbose_name="Preço",
        max_digits=10,
        decimal_places=2
    )
    stock_quantity = models.IntegerField(
        verbose_name="Quantidade atual no estoque"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name


class StockMovement(models.Model):
    IN="IN"
    OUT="OUT"

    MOVEMENT_TYPE = (
        (IN, "IN"),
        (OUT, "OUT")
    )
    product = models.ForeignKey(
        Product,
        verbose_name="Produto",
        on_delete=models.DO_NOTHING
    )
    movement_type = models.CharField(
        verbose_name="Tipo de Movimentação",
        choices=MOVEMENT_TYPE
    )
    quantity = models.IntegerField(
        verbose_name="Quantidade Movimentada"
    )
    reason = models.CharField(
        verbose_name="Motivo",
    )
    created_at = models.DateTimeField(
        verbose_name="Data de Movimentação",
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.product.name} - {self.movement_type}"
