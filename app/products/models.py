from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование", unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    volume = models.CharField(blank=True, null=True, max_length=30, verbose_name="Объём тары")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    stock = models.PositiveIntegerField(blank=True, null=True, verbose_name="Остатки")
    available = models.BooleanField(default=True, verbose_name="Доступность")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Feedback(models.Model):
    username = models.CharField(max_length=30, verbose_name="Имя")
    text = models.TextField(verbose_name="Текст")
    mark = models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
                                            null=True, blank=True, verbose_name="Оценка")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.username
