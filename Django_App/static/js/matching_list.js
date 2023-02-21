// 予約リストのclass属性追加
// カテゴリーの宣言
const orderCategory = document.getElementById("add-class-name").innerHTML;
// const orderCategoryHopeGender = document.getElementById("add-class-name").innerHTML;

// 目的・希望性別の条件分岐→classを追加
const li = document.getElementById("add-class-name");
// 目的がコミュニケーションだったら
if (orderCategory === "コミュニケーション"){
    li.classList.add("develop-color");
// 目的が開発目的だったら
} else if (orderCategory === "開発") {
    li.classList.add("develop-color");
}

const p = document.getElementById("add-class-name");
    // 希望性別が男性だったら
if (orderCategory === "男性") {
    p.classList.add("gender-color");
    // 希望性別が女性だったら
} else if (orderCategory === "女性") {
    p.classList.add("gender-color");
}
    // 希望性別がどちらでもOKだったら

// if (orderCategory === "コミュニケーション" && orderCategory === "男性"){
//     li.classList.add("develop-color");
// } else if (orderCategory === "コミュニケーション" && orderCategory === "女性"){
//     li.classList.add("develop-color");
// } else if (orderCategory === "開発" && orderCategory === "男性"){
//     li.classList.add("develop-color");
// } else if (orderCategory === "開発" && orderCategory === "女性"){
//     li.classList.add("develop-color");
// }









// 予約のステータスの記述
// classを追加
// 予約のステータスがnullだったら
// 予約のステータスがnullでなかったら