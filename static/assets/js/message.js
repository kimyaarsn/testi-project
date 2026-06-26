
document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        document.querySelectorAll(".alert").forEach(function (alert) {
            alert.style.transition = "all .1s ease";
            alert.style.opacity = "0";
            alert.style.transform = "translateY(-20px)";

            setTimeout(function () {
                alert.remove();
            }, 500);
        });
    }, 3000);
});