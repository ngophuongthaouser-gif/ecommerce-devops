from decimal import Decimal
from django import template

register = template.Library()

@register.filter
def filter_status(orders, status):
    return [order for order in orders if order.status == status]

@register.filter
def has_review(order_items):
    return all(item.review for item in order_items)

@register.filter
def vnd(value):
    try:
        number = Decimal(str(value))
        if number < Decimal('1000'):
            number = number * Decimal('1000')
        return f"{number:,.0f} VNĐ"
    except Exception:
        return value