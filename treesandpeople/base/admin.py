from django.contrib import admin


class InlineBase(admin.StackedInline):
    min_num = 0
    # Note: for some reason, extra > 0 gives "This field is required." for all
    # fields of the inline - making it effectively a required value.
    extra = 0
