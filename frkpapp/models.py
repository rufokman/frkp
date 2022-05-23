from django.db import models


class Queries(models.Model):
    url = models.CharField(max_length=3000, verbose_name='Введите ссылку на документ')
    format = models.PositiveIntegerField(verbose_name='Выберите формат документа',
                                         choices=((0, 'MicrosoftOffice (.docx)'),
                                                  (1, 'LibreOffice (.odt)')
                                                  ),
                                         default=0
                                         )
    blank = models.PositiveIntegerField(verbose_name='Выберите бланк',
                                        choices=(
                                            (0, 'Служебная записка'),
                                            ),
                                        default=0
                                        )
    time_create = models.DateTimeField(auto_now_add=True)
    status = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
        managed = True
        db_table = "queries"
