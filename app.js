// Telegram WebApp obyektini ulash
let tg = window.Telegram.WebApp;
tg.expand();

// Foydalanuvchi nomini chiqarish
if (tg.initDataUnsafe && tg.initDataUnsafe.user) {
    document.getElementById('username').innerText = tg.initDataUnsafe.user.first_name;
}

// Boshlang'ich namuna do'konlar
let shops = JSON.parse(localStorage.getItem('fikrhub_shops')) || [
    { name: "TechMarket Uz", category: "Elektronika", desc: "Noutbuklar, telefonlar va aksessuarlar eng arzon narxlarda.", contact: "@techmarket_admin" },
    { name: "FastBurger", category: "Ovqatlanish", desc: "Mazali burgerlar va fast-food mahsulotlari yetkazib berish.", contact: "@fastburger_uz" }
];

// Tablararo o'tish funksiyasi (event xatosi bo'lmasligi uchun to'g'irlandi)
function switchTab(tabId, event) {
    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
    
    document.getElementById(tabId + '-tab').classList.add('active');
    if (event && event.currentTarget) {
        event.currentTarget.classList.add('active');
    }
    
    if(tabId === 'shops') {
        renderShops();
    }
}

// Do'konlarni ekranga chiqarish
function renderShops(filteredList = shops) {
    let listContainer = document.getElementById('shops-list');
    if (!listContainer) return;
    listContainer.innerHTML = '';

    if (filteredList.length === 0) {
        listContainer.innerHTML = '<p style="text-align:center; color:#666;">Hozircha do\'konlar yo\'q. Birinchi bo\'lib qo\'shing!</p>';
        return;
    }

    filteredList.forEach(shop => {
        let card = document.createElement('div');
        card.className = 'shop-card';
        card.innerHTML = `
            <h3>${shop.name} <span class="category">${shop.category}</span></h3>
            <p>${shop.desc}</p>
            <a href="https://t.me/${shop.contact.replace('@', '')}" target="_blank" class="contact-btn">Bog'lanish: ${shop.contact}</a>
        `;
        listContainer.appendChild(card);
    });
}

// Yangi do'kon qo'shish
function addNewShop(event) {
    event.preventDefault();
    
    let newShop = {
        name: document.getElementById('shop-name').value,
        category: document.getElementById('shop-category').value,
        desc: document.getElementById('shop-desc').value,
        contact: document.getElementById('shop-contact').value
    };

    shops.push(newShop);
    localStorage.setItem('fikrhub_shops', JSON.stringify(shops));

    alert("Do'koningiz muvaffaqiyatli qo'shildi!");
    document.getElementById('shop-form').reset();
    
    // Do'konlar tabiga qaytish
    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
    document.getElementById('shops-tab').classList.add('active');
    document.querySelectorAll('.tab-btn')[0].classList.add('active');
    
    renderShops();
}

// Qidiruv funksiyasi
function filterShops() {
    let query = document.getElementById('search-input').value.toLowerCase();
    let filtered = shops.filter(s => s.name.toLowerCase().includes(query) || s.desc.toLowerCase().includes(query));
    renderShops(filtered);
}

// Obuna sotib olish tugmasi
function buySubscription(plan) {
    alert(`Tez kunda! ${plan} obunasi uchun to'lov tizimlari (Click/Payme/Telegram Stars) ulanadi.`);
}

// Sahifa ochilganda do'konlarni yuklash
renderShops();