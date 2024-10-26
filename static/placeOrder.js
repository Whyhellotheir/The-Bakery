//Selects the empty div
const itemDesc = document.getElementById("itemPurchaseDesc");

//Selects toggle button
const dropDown = document.getElementsByClassName("dropdown-toggle")[0];

//Selects dropdown items
const dropdownItems = document.querySelectorAll(".dropdown-item");

//For each dropdown item, which is named item, it adds an event listener
dropdownItems.forEach(item => {
    item.addEventListener("click", function() {
        // Change the text of the dropdown toggle button to the selected item's text
        dropDown.textContent = item.textContent;

        //when the text is choose an item it does not add anything
        if(dropDown.textContent != "Choose an Item"){
            // Get the item details from data attributes
            const name = item.getAttribute("data-name");
            const price = item.getAttribute("data-price");
            const description = item.getAttribute("data-description");
    
            // Display the selected item details in the itemPurchaseDesc div
            //Displays inputs for the amount requested and name and button to place order
            //Once the button is pressed, the data is sent 
            itemDesc.innerHTML = `
                <h4>${name}</h4>
                <p><strong>Price:</strong> ${price}</p>
                <p>${description}</p>

                <form action="/submit" method="POST">
                    <div class="mb-3 mt-3">
                        <label for="number" class="form-label">Amount:</label>
                        <input type="number" class="form-control" id="number" placeholder="Enter Amount" name="amount" required>
                    </div>

                    <div class="mb-3 mt-3">
                        <label for="username" class="form-label">Name:</label>
                        <input type="text" class="form-control" id="username" placeholder="Enter Name" name="userName" required>
                    </div>

                    <input type="hidden" name="itemName" value="${name}">

                    <button type="submit" class="btn custom-button">Place Order</button>
                </form>

            `;

            // Scroll smoothly to the itemDesc section
            itemDesc.scrollIntoView({ behavior: 'smooth' });


        }
         
    });
});

