// 現在のURLを取得
const href = location.href;
// ヘッダーの中のaタグを全部取得
let links = document.querySelectorAll(".header-list > ul > li > a");

// ループでURLと一致したaタグに current を付ける。
for (let i = 0; i < links.length; i++) {
    if (links[i].href == href) {
    document.querySelectorAll(".header-list > ul > li")[i].classList.add("current");
    }
}