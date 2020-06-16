from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Product, Category
from .models import Cart, Order


def add_to_cart(request, slug):
    # first get the product using slug info
    item = get_object_or_404(Product, slug=slug)

    # create the cart object
    # order_item will be the object returned and created will be a boolean
    order_item, created = Cart.objects.get_or_create(
        item=item, user=request.user)

    # find the orders that belong to a user AND still hasn't been ordered yet
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    # print(order_qs.exists())

    # if such a list exists,
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'This item quantity was updated.')
            # return redirect('mainapp:home')
            return redirect('mainapp:productpage', slug=slug)
        else:
            order.orderitems.add(order_item)
            messages.info(request, "This item was added to your cart.")
            # return redirect('mainapp:home')
            return redirect('mainapp:productpage', slug=slug)

    else:
        order=Order.objects.create(user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, "This item was added to your cart.")
        # return redirect('mainapp:home')
        return redirect('mainapp:productpage', slug=slug)



def remove_from_cart(request, slug):
    
    item=get_object_or_404(Product, slug=slug)

    cart_qs=Cart.objects.filter(user=request.user, item=item)

    if cart_qs.exists():
        cart=cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    
    order_qs=Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():       
        order=order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item=Cart.objects.filter(
                item=item,
                user=request.user)[0]
            order.orderitems.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            # return redirect("mainapp:home")
            return redirect('mainapp:productpage', slug=slug)

        else:
            messages.info(request, "This item was not in your cart")
            # return redirect("mainapp:home")
            return redirect('mainapp:productpage', slug=slug)

    else:
        messages.info(request, "You do not have an active order")
        # return redirect("core:home")
        return redirect('mainapp:productpage', slug=slug)



def order_summary(request):
    order = Order.objects.filter(user=request.user, ordered=False)
    context = {}
    return render(request, 'order-summary.html', context)


def checkout(request):
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    cartItems = order_qs[0].orderitems.all()

    totalPrice = sum([cart.item.price * cart.quantity for cart in cartItems])
    totalItemCount = sum(cart.quantity for cart in cartItems)
    context = {
        'cartItems': cartItems,
        'totalPrice': totalPrice,
        'totalItemCount': totalItemCount
    }
    return render(request, 'checkout-page.html', context)
