from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Remove all occurrences of "s" and "ss" from verbose names in all models'

    def handle(self, *args, **kwargs):
        for model in apps.get_models():
            meta = model._meta  

            # Remove 's' and 'ss' from verbose_name
            if meta.verbose_name:
                corrected_name = meta.verbose_name.replace("ss", "").replace("s", "")
                meta.verbose_name = corrected_name
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Updated verbose_name for '{model.__name__}': '{corrected_name}'"
                    )
                )

            # Remove 's' and 'ss' from verbose_name_plural
            if meta.verbose_name_plural:
                corrected_plural_name = meta.verbose_name_plural.replace("ss", "").replace("s", "")
                meta.verbose_name_plural = corrected_plural_name
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Updated verbose_name_plural for '{model.__name__}': '{corrected_plural_name}'"
                    )
                )

        self.stdout.write(self.style.SUCCESS("All 's' and 'ss' removed from verbose names successfully!"))
