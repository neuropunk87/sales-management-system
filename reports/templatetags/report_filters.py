from django import template


register = template.Library()


@register.filter
def format_report_name(value):
    if not value:
        return ""
    words = value.replace("_", " ").lower().split()
    minor_words = {"by", "for", "and", "of", "in", "on"}
    formatted_words = [
        word if word in minor_words and i != 0 else word.capitalize()
        for i, word in enumerate(words)
    ]
    return " ".join(formatted_words)
