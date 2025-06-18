import stripe

stripe.api_key = "sk_test_51NNNNNNNNNNNNNNNNNNNNNNNNNN"

def create_checkout_session(amount_cents):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': 'DockMate Service'},
                'unit_amount': amount_cents,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
    )
    return session.url
