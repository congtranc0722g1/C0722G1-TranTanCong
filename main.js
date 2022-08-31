let sophantu = +prompt("Nhập vào số phân tử");
let phanTu = new Array(sophantu);
for (let i = 0; i < phanTu.length; i++) {
    phanTu[i] = +prompt("Nhập phân tử thứ" + i);
}
let sum = 0;
trungBinh = 0;
for (let i = 0; i < phanTu.length; i++) {
    if(phanTu[i] % 5 == 0 && i % 3 == 0){
        sum += phanTu[i]

    }

}
trungBinh = sum/3;
alert(trungBinh);