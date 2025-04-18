 
    function updateCart(actionUrl, cartItemId, isAdd, csrf_token) {
        fetch(actionUrl, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrf_token ,
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            const quantityElement = document.querySelector(`#quantity-${cartItemId}`);
            const totalPriceElement = document.querySelector(`#total-price-${cartItemId}`);
            const overallTotalElement = document.querySelector('#overall-total');
    
            if (data.quantity > 0) {
                // Update quantity and total price for the cart item
                quantityElement.textContent = data.quantity;
                totalPriceElement.textContent = `${data.total_price.toFixed(1)}`;
            } else {
                // Remove the cart item from the DOM if quantity is 0
                const cartItemElement = document.querySelector(`#cart-item-${cartItemId}`);
                cartItemElement.remove();
            }
    
            // Update overall total price
            overallTotalElement.textContent = `${data.overall_total.toFixed(2)}`;
        })
        .catch(error => console.error('Error:', error));
    }
    
