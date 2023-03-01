// モーダルのJS指定

// 予約編集・削除のモーダルを開く記述
const modalBtns = document.querySelectorAll(".modalOpen");
modalBtns.forEach(function (btn) {
    btn.onclick = function () {
    const modal = btn.getAttribute('data-modal');
        document.getElementById(`${modal}-${order_id}`).style.display = "block";
    };
});
// 上記以外のモーダルを開く記述
const openModalBtns = document.querySelectorAll(".listModalOpen");
modalBtns.forEach(function (btn) {
    btn.onclick = function () {
    const modal = btn.getAttribute('data-modal');
        document.getElementById(modal).style.display = "block";
    };
});


// Xボタンを押したらモーダルを閉じる
const closeBtns = document.querySelectorAll(".modalClose");
closeBtns.forEach(function (btn) {
    btn.onclick = function () {
    const modal = btn.closest('.modal');
    modal.style.display = "none";
    };
});

// キャンセルボタンを押したらモーダルを閉じる
const cancelBtns = document.querySelectorAll(".cancelButton");
cancelBtns.forEach(function (btn) {
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




// // Xボタンを押したらモーダルを閉じる
// const closeBtns = document.querySelectorAll(".modalClose");
// closeBtns.forEach(function (btn) {
//     btn.onclick = function () {
//     const modal = btn.closest('.modal');
//     modal.style.display = "none";
//     };
// });

// // キャンセルボタンを押したらモーダルを閉じる
// const cancelBtns = document.querySelectorAll(".cancelButton");
// cancelBtns.forEach(function (btn) {
//     btn.onclick = function () {
//     const modal = btn.closest('.modal');
//     modal.style.display = "none";
//     };
// });
// // モーダル以外をクリックしたら閉じる
// window.onclick = function (event) {
//     if (event.target.className === "modal") {
//     event.target.style.display = "none";
//     }
// };