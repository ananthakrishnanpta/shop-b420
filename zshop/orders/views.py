from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib import messages

from cart.models import CartItem
from .models import Order, OrderDetails, Address
from .forms import AddressForm, OrderForm

@login_required
def create_order(request):
    """Create an order from the user's cart items and redirect to the Select Address view."""
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

    if not cart_items.exists():
        # Redirect to an empty cart page if no items are in the cart
        context = {
            'error': 'Your cart is empty.'
            }
        return render(request, 'cart.html', context )

    # Calculate the total amount of the cart
    total_amount = sum(item.quantity * item.product.price for item in cart_items)

    # Create an order record
    order = Order.objects.create(
        user=user,
        total_amount=total_amount,
        order_date=now(),
        status='PENDING'
    )

    # Create order detail records for each cart item
    for item in cart_items:
        OrderDetails.objects.create(
            order=order,
            order_item=item.product,
            quantity=item.quantity,
            price=item.product.price * item.quantity
        )

    # Clear the cart after creating the order
    cart_items.delete()

    # Redirect to the Select Address view
    return redirect('select_address_for_order', order_id=order.id)

@login_required
def order_history(request):
    """Display the order history of the user."""
    orders = Order.objects.filter(user=request.user).prefetch_related('order_details').order_by('-order_date')
    return render(request, 'order_history.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    """Display details of a specific order."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_detail.html', {'order': order})

@login_required
def add_address(request):
    """Allow the user to add a new address."""
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            # Set default address if it's the first one
            if not Address.objects.filter(user=request.user).exists():
                address.is_default = True
            address.save()
            # Redirect to the referring page
            next_url = request.GET.get('next', 'homepage')
            return redirect(next_url)  # Redirect to the referring page (e.g., select_address)
    else:
        form = AddressForm()
    return render(request, 'add_address.html', {'form': form})

@login_required
def select_address_for_order(request, order_id):
    """Allow the user to select an address for the order and proceed to payment."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    addresses = request.user.addresses.all()

    if request.method == 'POST':
        # Get the selected address ID from the form
        address_id = request.POST.get('address')
        address = get_object_or_404(Address, id=address_id, user=request.user)
        
        # Associate the selected address with the order
        order.address = address
        order.save()
        
        # Redirect to the Razorpay order creation and payment page
        return redirect('payment:create_razorpay_order', order_id=order.id)

    return render(request, 'select_address.html', {'order': order, 'addresses': addresses})

@login_required
def update_order(request, order_id):
    """Allow the user to update order details."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm(instance=order)
    return render(request, 'update_order.html', {'form': form})


@login_required
def cancel_order(request, order_id):
    """Cancel an order and redirect the user."""
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # Check if the order is still pending
    if order.status == "PENDING":
        order.status = "CANCELLED"
        order.save()
        messages.success(request, "Your order has been cancelled.")
    else:
        messages.error(request, "This order cannot be cancelled.")

    return redirect("homepage") 