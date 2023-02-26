// 予約リストのclass属性追加
// カテゴリーの宣言
const orderCategory = document.querySelector('.category').innerHTML;
// const orderCategoryHopeGender = document.getElementById("add-class-name").innerHTML;

// 目的・希望性別の条件分岐→classを追加
const p = document.querySelector('.category');
// 目的がコミュニケーションだったら
if (orderCategory === 'コミュニケーション'){
    p.classList.add('ComColor');
// 目的が開発目的だったら
} else if (orderCategory === "開発") {
    p.classList.add('developColor');
}








// 予約リストのclass属性追加
// カテゴリーの宣言
// const orderCategory = document.getElementById("addClassName").innerHTML;
// const orderCategoryHopeGender = document.getElementById("add-class-name").innerHTML;

// 目的・希望性別の条件分岐→classを追加
// const p = document.getElementById("addClassName");
// 目的がコミュニケーションだったら
// if (orderCategory === "コミュニケーション"){
//     p.classList.add("ComColor");
// 目的が開発目的だったら
// } else if (orderCategory === "開発") {
//     p.classList.add("developColor");
// }


// const p = document.getElementById("add-class-name");
    // 希望性別が男性だったら
// if (orderCategory === "男性") {
//     p.classList.add("gender-color");
    // 希望性別が女性だったら
// } else if (orderCategory === "女性") {
//     p.classList.add("gender-color");
// }


