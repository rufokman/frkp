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


class Document(models.Model):
    query = models.OneToOneField(Queries, models.DO_NOTHING, primary_key=True)
    kind = models.CharField(max_length=3000, verbose_name='Вид документа')
    content = models.CharField(max_length=3000, verbose_name='Краткое содержание')

    class Meta:
        managed = True
        db_table = "document"


class Signers(models.Model):
    document = models.OneToOneField(
        Document,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    fio = models.CharField(max_length=3000, verbose_name='Подписант')
    role = models.CharField(max_length=3000, verbose_name='Должность подписанта')
    dep = models.CharField(max_length=3000, verbose_name='Подразделение подписанта')

    class Meta:
        managed = True
        db_table = "signers"


class Performers(models.Model):
    document = models.OneToOneField(
        Document,
        on_delete=models.CASCADE,
        primary_key=True,
        default=0
    )
    fio = models.CharField(max_length=3000, verbose_name='Исполнитель')
    contacts = models.CharField(max_length=3000, verbose_name='Номер исполнителя')

    class Meta:
        managed = True
        db_table = "performers"


class Correspondents(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    fio = models.CharField(max_length=3000, verbose_name='Адресат')
    role = models.CharField(max_length=3000, verbose_name='Должность адресата')

    class Meta:
        managed = True
        db_table = "correspondents"
