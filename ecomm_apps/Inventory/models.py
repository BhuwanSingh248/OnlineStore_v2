
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):

    name = models.CharField(
        max_length=255,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category name"),
        help_text=_("format:required, max = 255"),
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name=_("safe URL"),
    )
    is_active = models.BooleanField(default=True)

    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="child",
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("parent of category"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Product cateogry")
        verbose_name_plural = _("product_categories")

    def __str__(self) -> str:
        return self.name
