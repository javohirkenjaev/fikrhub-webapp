// Telegram Web App obyekti
const tg = window.Telegram.WebApp;

// Sahifa yuklanganda Web App ni butun ekranga yoyish
tg.expand();

// Asosiy tugma rangini moslash (ixtiyoriy)
tg.MainButton.color = "#00d2ff";

// Tugma bosilganda Telegram orqali xabar yuborish
document.getElementById('connectBtn').addEventListener('click', function() {
    // Tugma animatsiyasi
    this.innerText = "So'rov yuborilmoqda...";
    this.style.opacity = "0.7";
    
    setTimeout(() => {
        // Haptic Feedback (Telefonda vibratsiya qiladi - premium his uchun)
        tg.HapticFeedback.notificationOccurred("success");
        
        // Botga xabar yuborish va oynani yopish
        tg.sendData("B2B_CONNECT_SMARTSTAFF");
    }, 1000);
});