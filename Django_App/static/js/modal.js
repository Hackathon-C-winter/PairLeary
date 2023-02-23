// tutorialのモーダルのJS指定
const modalBtns = document.querySelectorAll(".modalOpen");
modalBtns.forEach(function (btn) {
    btn.onclick = function () {
    const modal = btn.getAttribute('data-modal');
        document.getElementById(modal).style.display = "block";
    };
});

// 閉じるボタンを押したらモーダルを閉じる
const closeBtns = document.querySelectorAll(".modal-close");
closeBtns.forEach(function (btn) {
    btn.onclick = function () {
    const modal = btn.closest('.modal');
    modal.style.display = "none";
    };
});

// モーダル以外をクリックしたら閉じる
window.onclick = function (event) {
    if (event.target.className === "modal") {
    event.target.style.display = "none";
    }
};

