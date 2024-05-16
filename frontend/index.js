const productContainer = document.querySelector('#productContainer');
const backendUrl = 'http://localhost:3000';

const getProuductCard = (
    name,
    price,
    img,
    id,
    description
) => {
    return `
    <div class="product-card">
            <img src="${img}"
                alt="${name}" class="product-image">
            <h2 class="product-title">${name}</h2>
            <p class="product-description">${description}</p>
            <div class="product-price">Rs.${price}</div>
            <div class="product-actions">
                <button class="btn-add" onclick="printme('${id}')">Add</button>
                <button class="btn-remove">Remove</button>
            </div>
        </div>
    `
}

const renderProducts = (products) => {
    productContainer.innerHTML = products.map((product) => getProuductCard(product.name, product.price, product.img, product.id, product.description)).join('');
}
